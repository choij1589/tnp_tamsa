#!/usr/bin/env python3
"""
Script to submit condor jobs for refitting problematic bins identified by check_fit_status.py
"""

import os
import sys
import subprocess
import tempfile
import argparse
import time
import re
from collections import defaultdict

def get_results_dir(config_path, config_name):
    """Construct results directory from config path and name"""
    # Extract config file name from path (e.g., config/TopHNT_Electron_Run3_v0.py -> TopHNT_Electron_Run3_v0)
    config_file = os.path.basename(config_path).replace('.py', '')
    results_dir = f"results/{config_file}/{config_name}"
    return results_dir

def get_problematic_bins(results_dir):
    """Run checkFitStatus.py and extract problematic bins"""
    try:
        # Run the check script and capture output
        cmd = f"source setup.sh && python3 python/checkFitStatus.py {results_dir}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, executable='/bin/bash')
        
        if result.stderr:
            print("Error running check_fit_status.py:")
            print(result.stderr)
            return {}, {}
        
        # Parse the output to extract bins to refit
        lines = result.stdout.split('\n')
        data_bins = {}
        sim_bins = {}
        current_section = None
        
        for line in lines:
            line = line.strip()
            if "DATA bins to refit" in line:
                current_section = "data"
                continue
            elif "SIM bins to refit" in line:
                current_section = "sim"
                continue
            elif line.startswith('bin') and '/' in line:
                # Parse bin/systematic format
                parts = line.split('/')
                if len(parts) == 2:
                    bin_name = parts[0]
                    systematic = parts[1]
                    bin_num = int(bin_name.replace('bin', ''))
                    
                    if current_section == "data":
                        if systematic not in data_bins:
                            data_bins[systematic] = []
                        data_bins[systematic].append(bin_num)
                    elif current_section == "sim":
                        if systematic not in sim_bins:
                            sim_bins[systematic] = []
                        sim_bins[systematic].append(bin_num)
        
        # Sort bins for each systematic
        for systematic in data_bins:
            data_bins[systematic].sort()
        for systematic in sim_bins:
            sim_bins[systematic].sort()
        
        return data_bins, sim_bins
        
    except Exception as e:
        print(f"Error: {e}")
        return {}, {}

def create_condor_job(results_dir, config_path, config_name, systematic, bin_list, is_data=True):
    """Create condor job files for a specific systematic and bin list"""
    
    data_or_sim = "data" if is_data else "sim"
    job_dir = os.path.join(results_dir, f"refit_{data_or_sim}.d", systematic)
    
    # Create job directory
    os.makedirs(job_dir, exist_ok=True)
    
    # Create run script
    run_script = os.path.join(job_dir, "run.sh")
    with open(run_script, 'w') as f:
        f.write(f"""#!/bin/bash
cd $TNP_BASE
source setup.sh
python3 tnp_tamsa.py {config_path} {config_name} --step fit --set {systematic[1:2]} --member {systematic[3:4]} {"--data" if is_data else "--sim"} --bin $1 --no-condor
exit $?
""")
    os.chmod(run_script, 0o755)
    
    # Create condor job description file
    condor_file = os.path.join(job_dir, "condor.jds")
    job_name = f"{config_name}_refit_{data_or_sim}_{systematic}"
    
    with open(condor_file, 'w') as f:
        f.write(f"""executable = {run_script}
arguments = $(Process)
output = {job_dir}/job$(Process).out
error = {job_dir}/job$(Process).err
log = {job_dir}/condor.log
concurrency_limits = n300.{os.getenv('USER', 'user')}
jobbatchname = {job_name}
getenv = True
queue arguments from (
""")
        
        # Add bin numbers
        for bin_num in bin_list:
            f.write(f"{bin_num}\n")
        f.write(")\n")
    
    return condor_file, job_name

def get_job_status(job_names):
    """Check status of submitted condor jobs"""
    try:
        # Use condor_q with format to get cleaner output
        result = subprocess.run(['condor_q', '-format', '%s ', 'JobBatchName', '-format', '%s\n', 'JobStatus'], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            # Fallback to basic condor_q
            result = subprocess.run(['condor_q'], capture_output=True, text=True)
            if result.returncode != 0:
                return {}
        
        status_dict = {}
        for job_name in job_names:
            status_dict[job_name] = {"running": 0, "idle": 0, "held": 0, "completed": 0}
        
        # Parse condor_q output
        lines = result.stdout.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Try formatted output first (JobBatchName JobStatus)
            parts = line.split()
            if len(parts) >= 2:
                batch_name = parts[0]
                try:
                    job_status = int(parts[1])
                    for job_name in job_names:
                        if job_name in batch_name:
                            if job_status == 1:  # Idle
                                status_dict[job_name]["idle"] += 1
                            elif job_status == 2:  # Running
                                status_dict[job_name]["running"] += 1
                            elif job_status == 5:  # Held
                                status_dict[job_name]["held"] += 1
                            elif job_status == 4:  # Completed
                                status_dict[job_name]["completed"] += 1
                            break
                except ValueError:
                    # Not formatted output, try string matching
                    for job_name in job_names:
                        if job_name in line:
                            if " R " in line or " 2 " in line:  # Running
                                status_dict[job_name]["running"] += 1
                            elif " I " in line or " 1 " in line:  # Idle
                                status_dict[job_name]["idle"] += 1
                            elif " H " in line or " 5 " in line:  # Held
                                status_dict[job_name]["held"] += 1
                            elif " C " in line or " 4 " in line:  # Completed
                                status_dict[job_name]["completed"] += 1
                            break
        
        return status_dict
    except Exception as e:
        print(f"Error checking job status: {e}")
        return {}

def wait_for_jobs(job_names, check_interval=30):
    """Wait for all condor jobs to complete"""
    if not job_names:
        return True
    
    print(f"\nMonitoring {len(job_names)} job batches...")
    print(f"Job status will be checked every {check_interval} seconds.")
    print("Press Ctrl+C to stop monitoring (jobs will continue running)")
    print()
    
    # Check if jobs are actually submitted first
    initial_check = get_job_status(job_names)
    if not initial_check:
        print("⚠️  No jobs found in condor queue. They may have completed already or failed to submit.")
        return True
    
    # Check if all jobs are already done
    total_active = sum(s["running"] + s["idle"] for s in initial_check.values())
    if total_active == 0:
        print("✅ All jobs appear to be completed already!")
        return True
    
    try:
        check_count = 0
        while True:
            status_dict = get_job_status(job_names)
            check_count += 1
            
            if not status_dict:
                print(f"\n⚠️  Unable to check job status (attempt {check_count}). Retrying...")
                time.sleep(min(check_interval, 10))  # Don't wait too long on errors
                continue
            
            total_running = sum(s["running"] for s in status_dict.values())
            total_idle = sum(s["idle"] for s in status_dict.values())
            total_held = sum(s["held"] for s in status_dict.values())
            total_completed = sum(s["completed"] for s in status_dict.values())
            total_active = total_running + total_idle
            
            # Show detailed status every 10 checks (5 minutes at default interval)
            if check_count % 10 == 1:
                print(f"\n🔍 Detailed status check #{check_count}:")
                for job_name, status in status_dict.items():
                    if any(status.values()):
                        print(f"   {job_name}: R:{status['running']} I:{status['idle']} H:{status['held']} C:{status['completed']}")
                print()
            
            # Check if all jobs are done (no running or idle jobs)
            if total_active == 0:
                if total_held > 0:
                    print(f"\n⚠️  All jobs completed, but {total_held} jobs are held!")
                    print("Check held jobs with: condor_q -held")
                    print("Check log files for error details.")
                else:
                    print(f"\n✅ All jobs completed successfully!")
                break
            
            # Show running status
            status_msg = f"📊 Jobs - Running: {total_running}, Idle: {total_idle}"
            if total_held > 0:
                status_msg += f", Held: {total_held}"
            if total_completed > 0:
                status_msg += f", Completed: {total_completed}"
            
            print(f"\r{status_msg}", end="", flush=True)
            time.sleep(check_interval)
    
    except KeyboardInterrupt:
        print(f"\n\n⏸️  Monitoring stopped by user. Jobs are still running.")
        print("Check status with: condor_q")
        print("Wait for completion with: condor_wait <logfile>")
        return False
    
    return True

def run_local_fits(config_path, config_name, data_bins, sim_bins, args):
    """Run fits locally instead of submitting to condor"""
    print("="*60)
    print("RUNNING FITS LOCALLY")
    print("="*60)
    
    total_fits = 0
    successful_fits = 0
    failed_fits = 0
    
    # Run data fits
    if data_bins and not args.sim_only:
        print(f"\nRunning DATA fits locally...")
        for systematic in sorted(data_bins.keys()):
            bins = data_bins[systematic]
            if args.max_jobs and len(bins) > args.max_jobs:
                print(f"Warning: {systematic} has {len(bins)} bins, limiting to first {args.max_jobs}")
                bins = bins[:args.max_jobs]
            
            print(f"  {systematic}: {len(bins)} bins")
            set_num = systematic[1:2]
            member_num = systematic[3:4]
            
            for bin_num in bins:
                total_fits += 1
                cmd = f"source setup.sh && python3 tnp_tamsa.py {config_path} {config_name} --step fit --set {set_num} --member {member_num} --data --bin {bin_num} --no-condor"
                
                print(f"    Running bin {bin_num}...", end=" ", flush=True)
                try:
                    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, executable='/bin/bash')
                    if result.returncode == 0:
                        print("✅")
                        successful_fits += 1
                    else:
                        print("❌")
                        failed_fits += 1
                        print(f"      Error: {result.stderr.strip()[:100]}...")
                except Exception as e:
                    print("❌")
                    failed_fits += 1
                    print(f"      Exception: {e}")
    
    # Run sim fits
    if sim_bins and not args.data_only:
        print(f"\nRunning SIM fits locally...")
        for systematic in sorted(sim_bins.keys()):
            bins = sim_bins[systematic]
            if args.max_jobs and len(bins) > args.max_jobs:
                print(f"Warning: {systematic} has {len(bins)} bins, limiting to first {args.max_jobs}")
                bins = bins[:args.max_jobs]
            
            print(f"  {systematic}: {len(bins)} bins")
            set_num = systematic[1:2]
            member_num = systematic[3:4]
            
            for bin_num in bins:
                total_fits += 1
                cmd = f"source setup.sh && python3 tnp_tamsa.py {config_path} {config_name} --step fit --set {set_num} --member {member_num} --sim --bin {bin_num} --no-condor"
                
                print(f"    Running bin {bin_num}...", end=" ", flush=True)
                try:
                    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, executable='/bin/bash')
                    if result.returncode == 0:
                        print("✅")
                        successful_fits += 1
                    else:
                        print("❌")
                        failed_fits += 1
                        print(f"      Error: {result.stderr.strip()[:100]}...")
                except Exception as e:
                    print("❌")
                    failed_fits += 1
                    print(f"      Exception: {e}")
    
    print("\n" + "="*60)
    print("LOCAL EXECUTION SUMMARY")
    print("="*60)
    print(f"Total fits attempted: {total_fits}")
    print(f"Successful fits: {successful_fits}")
    print(f"Failed fits: {failed_fits}")
    
    if failed_fits > 0:
        print(f"⚠️  {failed_fits} fits failed. Check the error messages above.")
    else:
        print("✅ All fits completed successfully!")
    
    return failed_fits == 0

def run_post_job_analysis(results_dir):
    """Run checkFitStatus.py after jobs complete to show improvements"""
    print("\n" + "="*60)
    print("POST-REFIT ANALYSIS")
    print("="*60)
    print("Running fit status check to see improvements...")
    
    try:
        # Run the check script (updated filename)
        cmd = f"source setup.sh && python3 python/checkFitStatus.py {results_dir}"
        result = subprocess.run(cmd, shell=True, text=True, executable='/bin/bash')
        
        if result.returncode == 0:
            print("✅ Post-refit analysis completed successfully!")
        else:
            print("⚠️  Post-refit analysis completed with warnings.")
            
    except Exception as e:
        print(f"❌ Error running post-refit analysis: {e}")
        print(f"You can manually run: python3 python/checkFitStatus.py {results_dir}")

def main():
    parser = argparse.ArgumentParser(description='Submit condor jobs for refitting problematic bins')
    parser.add_argument('config_path', help='Config file path (e.g., config/TopHNT_Electron_Run3_v0.py)')
    parser.add_argument('config_name', help='Config name (e.g., TopHNT_2022EE)')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without submitting jobs')
    parser.add_argument('--no-condor', action='store_true', help='Run fits locally instead of submitting to condor')
    parser.add_argument('--data-only', action='store_true', help='Only submit data refitting jobs')
    parser.add_argument('--sim-only', action='store_true', help='Only submit sim refitting jobs')
    parser.add_argument('--systematic', help='Only submit jobs for specific systematic (e.g., s0m0, s1m0)')
    parser.add_argument('--max-jobs', type=int, default=None, help='Maximum number of concurrent jobs per systematic')
    parser.add_argument('--no-wait', action='store_true', help='Do not wait for jobs to complete (submit and exit)')
    parser.add_argument('--check-interval', type=int, default=30, help='Job status check interval in seconds (default: 30)')
    
    args = parser.parse_args()
    
    # Verify config file exists
    if not os.path.exists(args.config_path):
        print(f"Config file {args.config_path} does not exist!")
        sys.exit(1)
    
    # Construct results directory
    results_dir = get_results_dir(args.config_path, args.config_name)
    
    if not os.path.exists(results_dir):
        print(f"Results directory {results_dir} does not exist!")
        sys.exit(1)
    
    print(f"Configuration: {args.config_path}")
    print(f"Config name: {args.config_name}")
    print(f"Results directory: {results_dir}")
    print()
    
    # Get problematic bins
    print("Analyzing fit status...")
    data_bins, sim_bins = get_problematic_bins(results_dir)
    
    if not data_bins and not sim_bins:
        print("No problematic bins found!")
        return
    
    print(f"Found problematic bins:")
    if data_bins:
        total_data_bins = sum(len(bins) for bins in data_bins.values())
        print(f"  DATA: {total_data_bins} bins across {len(data_bins)} systematics")
    if sim_bins:
        total_sim_bins = sum(len(bins) for bins in sim_bins.values())
        print(f"  SIM: {total_sim_bins} bins across {len(sim_bins)} systematics")
    print()
    
    # Filter by systematic if specified
    if args.systematic:
        if args.systematic in data_bins:
            data_bins = {args.systematic: data_bins[args.systematic]}
        else:
            data_bins = {}
        if args.systematic in sim_bins:
            sim_bins = {args.systematic: sim_bins[args.systematic]}
        else:
            sim_bins = {}
    
    # Handle different execution modes
    if args.dry_run:
        # Dry run mode - show what would be done
        print("="*60)
        print("DRY RUN - SHOWING WHAT WOULD BE DONE")
        print("="*60)
        
        if data_bins and not args.sim_only:
            print("\nDATA refitting jobs that would be created:")
            for systematic in sorted(data_bins.keys()):
                bins = data_bins[systematic]
                if args.max_jobs and len(bins) > args.max_jobs:
                    bins = bins[:args.max_jobs]
                print(f"  {systematic}: {len(bins)} bins ({', '.join(map(str, bins))})")
        
        if sim_bins and not args.data_only:
            print("\nSIM refitting jobs that would be created:")
            for systematic in sorted(sim_bins.keys()):
                bins = sim_bins[systematic]
                if args.max_jobs and len(bins) > args.max_jobs:
                    bins = bins[:args.max_jobs]
                print(f"  {systematic}: {len(bins)} bins ({', '.join(map(str, bins))})")
        
        print("\n" + "="*60)
        print("DRY RUN COMPLETE")
        print("="*60)
        print("Remove --dry-run flag to actually execute the fits.")
        print("\nExecution mode options:")
        print(f"  python3 python/submitRefitJobs.py {args.config_path} {args.config_name}  # Submit to condor (default)")
        print(f"  python3 python/submitRefitJobs.py {args.config_path} {args.config_name} --no-condor  # Run locally")
        print(f"  python3 python/submitRefitJobs.py {args.config_path} {args.config_name} --dry-run  # Show what would be done")
        
    elif args.no_condor:
        # Local execution mode
        success = run_local_fits(args.config_path, args.config_name, data_bins, sim_bins, args)
        if success:
            run_post_job_analysis(results_dir)
        
    else:
        # Condor submission mode (default)
        submitted_jobs = []
        
        # Submit data jobs
        if data_bins and not args.sim_only:
            print("PREPARING DATA REFITTING JOBS:")
            print("-" * 40)
            
            for systematic in sorted(data_bins.keys()):
                bins = data_bins[systematic]
                if args.max_jobs and len(bins) > args.max_jobs:
                    print(f"Warning: {systematic} has {len(bins)} bins, limiting to first {args.max_jobs}")
                    bins = bins[:args.max_jobs]
                
                condor_file, job_name = create_condor_job(
                    results_dir, args.config_path, args.config_name, 
                    systematic, bins, is_data=True
                )
                
                print(f"  {systematic}: {len(bins)} bins -> {condor_file}")
                
                try:
                    result = subprocess.run(['condor_submit', condor_file], 
                                          capture_output=True, text=True)
                    if result.returncode == 0:
                        print(f"    ✓ Submitted successfully")
                        submitted_jobs.append(job_name)
                    else:
                        print(f"    ✗ Failed to submit: {result.stderr}")
                except Exception as e:
                    print(f"    ✗ Error submitting: {e}")
            print()
        
        # Submit sim jobs
        if sim_bins and not args.data_only:
            print("PREPARING SIM REFITTING JOBS:")
            print("-" * 40)
            
            for systematic in sorted(sim_bins.keys()):
                bins = sim_bins[systematic]
                if args.max_jobs and len(bins) > args.max_jobs:
                    print(f"Warning: {systematic} has {len(bins)} bins, limiting to first {args.max_jobs}")
                    bins = bins[:args.max_jobs]
                
                condor_file, job_name = create_condor_job(
                    results_dir, args.config_path, args.config_name, 
                    systematic, bins, is_data=False
                )
                
                print(f"  {systematic}: {len(bins)} bins -> {condor_file}")
                
                try:
                    result = subprocess.run(['condor_submit', condor_file], 
                                          capture_output=True, text=True)
                    if result.returncode == 0:
                        print(f"    ✓ Submitted successfully")
                        submitted_jobs.append(job_name)
                    else:
                        print(f"    ✗ Failed to submit: {result.stderr}")
                except Exception as e:
                    print(f"    ✗ Error submitting: {e}")
            print()
        
        # Summary and monitoring
        print("="*60)
        print("CONDOR SUBMISSION SUMMARY")
        print("="*60)
        if submitted_jobs:
            print(f"Successfully submitted {len(submitted_jobs)} job batches:")
            for job in submitted_jobs:
                print(f"  - {job}")
            print()
            
            if args.no_wait:
                print("Monitor jobs with:")
                print("  condor_q")
                print("  watch condor_q")
                print("Jobs submitted without monitoring. Use without --no-wait to monitor automatically.")
            else:
                # Wait for jobs to complete and run analysis (default behavior)
                jobs_completed = wait_for_jobs(submitted_jobs, args.check_interval)
                if jobs_completed:
                    run_post_job_analysis(results_dir)
        else:
            print("No jobs were submitted successfully.")

if __name__ == "__main__":
    main()
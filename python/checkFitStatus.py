#!/usr/bin/env python3
"""
Script to check fit status and identify bins that need to be refitted.

Criteria:
For sim:
- Status 0,1,3 are okay. Other status should be refitted.
- For systematics, efficiency values should not differ more than 0.01 from nominal (s0m0) fit.

For data:
- For the nominal fit, only status 0 is permitted.
- For the other systematics, status 0,1,3 are permitted.
- For systematics, efficiency values should not differ more than 0.03 from nominal fit.
"""

import os
import sys
import glob
import math
import ROOT as rt
from collections import defaultdict

def calc_efficiency(numPass, numFail, errPass=0, errFail=0):
    """Calculate efficiency and propagate errors"""
    if numPass + numFail == 0:
        return 0.0, 0.0
    
    eff = numPass / (numPass + numFail)
    if errPass == 0 and errFail == 0:
        return eff, 0.0
    
    # Error propagation from fitUtils.py
    total = numPass + numFail
    err = math.sqrt(errPass*errPass*numFail*numFail + errFail*errFail*numPass*numPass) / (total*total)
    return eff, err

def get_fit_results(filepath, systematic):
    """Extract fit results from ROOT file"""
    if not os.path.exists(filepath):
        return None
    
    try:
        f = rt.TFile(filepath)
        if not f or f.IsZombie():
            return None
        
        dir_obj = f.Get(systematic)
        if not dir_obj:
            return None
        
        # Find the status and result objects
        keys = [k.GetName() for k in dir_obj.GetListOfKeys()]
        statusP_key = next((k for k in keys if k.endswith('_statusP')), None)
        statusF_key = next((k for k in keys if k.endswith('_statusF')), None)
        resP_key = next((k for k in keys if k.endswith('_resP')), None)
        resF_key = next((k for k in keys if k.endswith('_resF')), None)
        
        if not all([statusP_key, statusF_key, resP_key, resF_key]):
            return None
        
        # Get status
        statusP = dir_obj.Get(statusP_key)[0]
        statusF = dir_obj.Get(statusF_key)[0]
        
        # Get fit results
        resP = dir_obj.Get(resP_key)
        resF = dir_obj.Get(resF_key)
        
        # Extract signal yields
        numPass, errPass = 0, 0
        numFail, errFail = 0, 0
        
        params = resP.floatParsFinal()
        for i in range(params.getSize()):
            param = params.at(i)
            if 'numSignalPass' in param.GetName():
                numPass = param.getVal()
                errPass = param.getError()
        
        params = resF.floatParsFinal()
        for i in range(params.getSize()):
            param = params.at(i)
            if 'numSignalFail' in param.GetName():
                numFail = param.getVal()
                errFail = param.getError()
        
        efficiency, eff_err = calc_efficiency(numPass, numFail, errPass, errFail)
        
        return {
            'statusP': int(statusP),
            'statusF': int(statusF),
            'fitStatusP': resP.status(),
            'fitStatusF': resF.status(),
            'covQualP': resP.covQual(),
            'covQualF': resF.covQual(),
            'numPass': numPass,
            'numFail': numFail,
            'errPass': errPass,
            'errFail': errFail,
            'efficiency': efficiency,
            'eff_error': eff_err
        }
        
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None
    finally:
        if 'f' in locals() and f:
            f.Close()

def check_status_ok(status, is_data=False, is_nominal=False):
    """Check if fit status is acceptable according to criteria"""
    if is_data and is_nominal:
        # Data nominal: only status 0 permitted
        return status == 0
    else:
        # Data systematics or sim: status 0,1,3 are okay
        return status in [0, 1, 3]

def main():
    if len(sys.argv) != 2:
        print("Usage: python check_fit_status.py <results_directory>")
        print("Example: python check_fit_status.py results/TopHNT_Electron_Run3_v0/TopHNT_2022EE")
        sys.exit(1)
    
    results_dir = sys.argv[1]
    
    if not os.path.exists(results_dir):
        print(f"Directory {results_dir} does not exist!")
        sys.exit(1)
    
    print(f"Checking fit status in: {results_dir}")
    print("=" * 60)
    print("FIT STATUS CRITERIA:")
    print("For SIM:")
    print("  - Status 0,1,3 are okay. Other status should be refitted.")
    print("  - For systematics, efficiency values should not differ more than 0.05 from nominal (s0m0) fit.")
    print("For DATA:")
    print("  - For the nominal fit, only status 0 is permitted.")
    print("  - For the other systematics, status 0,1,3 are permitted.")
    print("  - For systematics, efficiency values should not differ more than 0.1 from nominal fit.")
    print("=" * 60)
    
    # Initialize counters
    problems = defaultdict(list)
    
    # Check data fits
    data_dir = os.path.join(results_dir, "fits_data.d")
    if os.path.exists(data_dir):
        print("@@@@@@ CHECKING DATA FITS")
        
        # Get all systematics
        systematics = [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d)) and d.startswith('s')]
        systematics.sort()
        
        # Get nominal results first
        nominal_results = {}
        nominal_sys = 's0m0'
        nominal_dir = os.path.join(data_dir, nominal_sys)
        
        if os.path.exists(nominal_dir):
            bin_files = glob.glob(os.path.join(nominal_dir, "bin*.root"))
            for bin_file in sorted(bin_files):
                bin_name = os.path.basename(bin_file).replace('.root', '')
                results = get_fit_results(bin_file, nominal_sys)
                if results:
                    nominal_results[bin_name] = results
        
        # Check all systematics
        for systematic in systematics:
            sys_dir = os.path.join(data_dir, systematic)
            if not os.path.exists(sys_dir):
                continue
                
            is_nominal = (systematic == 's0m0')
            bin_files = glob.glob(os.path.join(sys_dir, "bin*.root"))
            
            for bin_file in sorted(bin_files):
                bin_name = os.path.basename(bin_file).replace('.root', '')
                results = get_fit_results(bin_file, systematic)
                
                if not results:
                    problems['data_missing'].append(f"{bin_name}/{systematic}")
                    continue
                
                # Check fit status
                statusP_ok = check_status_ok(results['fitStatusP'], is_data=True, is_nominal=is_nominal)
                statusF_ok = check_status_ok(results['fitStatusF'], is_data=True, is_nominal=is_nominal)
                
                if not statusP_ok or not statusF_ok:
                    problems['data_bad_status'].append(f"{bin_name}/{systematic} (P:{results['fitStatusP']}, F:{results['fitStatusF']})")
                
                # Check efficiency difference from nominal (for systematics)
                if not is_nominal and bin_name in nominal_results:
                    nominal_eff = nominal_results[bin_name]['efficiency']
                    sys_eff = results['efficiency']
                    eff_diff = abs(sys_eff - nominal_eff)
                    
                    if eff_diff > 0.03:
                        problems['data_large_eff_diff'].append(f"{bin_name}/{systematic} (diff: {eff_diff:.3f})")
    
    # Check sim fits
    sim_dir = os.path.join(results_dir, "fits_sim.d")
    if os.path.exists(sim_dir):
        print("@@@@@@ CHECKING SIM FITS")
        
        # Get all systematics
        systematics = [d for d in os.listdir(sim_dir) if os.path.isdir(os.path.join(sim_dir, d)) and d.startswith('s')]
        systematics.sort()
        
        # Get nominal results first
        nominal_results = {}
        nominal_sys = 's0m0'
        nominal_dir = os.path.join(sim_dir, nominal_sys)
        
        if os.path.exists(nominal_dir):
            bin_files = glob.glob(os.path.join(nominal_dir, "bin*.root"))
            for bin_file in sorted(bin_files):
                bin_name = os.path.basename(bin_file).replace('.root', '')
                results = get_fit_results(bin_file, nominal_sys)
                if results:
                    nominal_results[bin_name] = results
        
        # Check all systematics
        for systematic in systematics:
            sys_dir = os.path.join(sim_dir, systematic)
            if not os.path.exists(sys_dir):
                continue
                
            is_nominal = (systematic == 's0m0')
            bin_files = glob.glob(os.path.join(sys_dir, "bin*.root"))
            
            for bin_file in sorted(bin_files):
                bin_name = os.path.basename(bin_file).replace('.root', '')
                results = get_fit_results(bin_file, systematic)
                
                if not results:
                    problems['sim_missing'].append(f"{bin_name}/{systematic}")
                    continue
                
                # Check fit status (0,1,3 are okay for sim)
                statusP_ok = check_status_ok(results['fitStatusP'], is_data=False, is_nominal=is_nominal)
                statusF_ok = check_status_ok(results['fitStatusF'], is_data=False, is_nominal=is_nominal)
                
                if not statusP_ok or not statusF_ok:
                    problems['sim_bad_status'].append(f"{bin_name}/{systematic} (P:{results['fitStatusP']}, F:{results['fitStatusF']})")
                
                # Check efficiency difference from nominal (for systematics)
                if not is_nominal and bin_name in nominal_results:
                    nominal_eff = nominal_results[bin_name]['efficiency']
                    sys_eff = results['efficiency']
                    eff_diff = abs(sys_eff - nominal_eff)
                    
                    if eff_diff > 0.01:
                        problems['sim_large_eff_diff'].append(f"{bin_name}/{systematic} (diff: {eff_diff:.3f})")
    
    # Print summary
    print("="*60)
    print("SUMMARY OF PROBLEMS")
    print("="*60)
    
    total_problems = sum(len(v) for v in problems.values())
    
    if total_problems == 0:
        print("✓ No problems found! All fits pass the criteria.")
    else:
        print(f"Found {total_problems} problems that need attention:\n")
        
        # Sort function to sort by bin number
        def sort_by_bin_number(item):
            bin_part = item.split('/')[0]  # get binX part
            return int(bin_part.replace('bin', ''))

        if problems['data_missing']:
            print(f"DATA - Missing fit results ({len(problems['data_missing'])} bins):")
            for item in sorted(problems['data_missing'], key=sort_by_bin_number):
                print(f"  - {item}")
            print()

        if problems['data_bad_status']:
            print(f"DATA - Bad fit status ({len(problems['data_bad_status'])} bins):")
            for item in sorted(problems['data_bad_status'], key=sort_by_bin_number):
                print(f"  - {item}")
            print()

        if problems['data_large_eff_diff']:
            print(f"DATA - Large efficiency difference from nominal ({len(problems['data_large_eff_diff'])} bins):")
            print("  (difference > 0.1)")
            for item in sorted(problems['data_large_eff_diff'], key=sort_by_bin_number):
                print(f"  - {item}")
            print()

        if problems['sim_missing']:
            print(f"SIM - Missing fit results ({len(problems['sim_missing'])} bins):")
            for item in sorted(problems['sim_missing'], key=sort_by_bin_number):
                print(f"  - {item}")
            print()

        if problems['sim_bad_status']:
            print(f"SIM - Bad fit status ({len(problems['sim_bad_status'])} bins):")
            for item in sorted(problems['sim_bad_status'], key=sort_by_bin_number):
                print(f"  - {item}")
            print()

        if problems['sim_large_eff_diff']:
            print(f"SIM - Large efficiency difference from nominal ({len(problems['sim_large_eff_diff'])} bins):")
            print("  (difference > 0.05)")
            for item in sorted(problems['sim_large_eff_diff'], key=sort_by_bin_number):
                print(f"  - {item}")
            print()
    
    print("="*60)
    print("Bins to be re-checked and refitted:")
    print("="*60)
    
    # Collect unique bins that need refitting, separated by data/sim
    data_recheck_bins = set()
    sim_recheck_bins = set()
    
    # Collect data problems
    for problem_type in ['data_missing', 'data_bad_status', 'data_large_eff_diff']:
        if problem_type in problems:
            for item in problems[problem_type]:
                bin_info = item.split(' ')[0]  # Remove extra info in parentheses
                data_recheck_bins.add(bin_info)
    
    # Collect sim problems
    for problem_type in ['sim_missing', 'sim_bad_status', 'sim_large_eff_diff']:
        if problem_type in problems:
            for item in problems[problem_type]:
                bin_info = item.split(' ')[0]  # Remove extra info in parentheses
                sim_recheck_bins.add(bin_info)
    
    total_bins = len(data_recheck_bins) + len(sim_recheck_bins)
    
    if total_bins == 0:
        print("No bins need to be refitted.")
    else:
        print(f"Total unique bins to recheck: {total_bins}")
        
        # Sort function to sort by bin number
        def sort_by_bin_number(bin_info):
            bin_part = bin_info.split('/')[0]  # get binX part
            return int(bin_part.replace('bin', ''))
        
        if data_recheck_bins:
            print(f"\nDATA bins to refit ({len(data_recheck_bins)} bins):")
            for bin_info in sorted(data_recheck_bins, key=sort_by_bin_number):
                print(f"  {bin_info}")
        
        if sim_recheck_bins:
            print(f"\nSIM bins to refit ({len(sim_recheck_bins)} bins):")
            for bin_info in sorted(sim_recheck_bins, key=sort_by_bin_number):
                print(f"  {bin_info}")

if __name__ == "__main__":
    main()
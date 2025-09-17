#!/usr/bin/env python3

import os
import sys
sys.path.insert(0, '/data9/Users/choij/Sync/workspace/tnp_tamsa/python')

import ROOT

def detailed_systematic_check():
    base_path = "/data9/Users/choij/Sync/workspace/tnp_tamsa/results/TopHNT_Electron_Run3_v0/TopHNT_2023"
    eff_file_path = os.path.join(base_path, "efficiency.root")
    
    print("="*80)
    print("DETAILED SYSTEMATIC VARIATION CHECK")
    print("="*80)
    
    # Open efficiency file
    eff_file = ROOT.TFile.Open(eff_file_path)
    if not eff_file or eff_file.IsZombie():
        print(f"ERROR: Cannot open {eff_file_path}")
        return
    
    # Get all systematic variations
    syst_variations = []
    for key in eff_file.GetListOfKeys():
        name = key.GetName()
        if name.startswith("data_s") and "m" in name:
            syst_variations.append(name)
    
    syst_variations.sort()
    print(f"Found {len(syst_variations)} systematic variations:")
    for var in syst_variations:
        print(f"  - {var}")
    
    # Get nominal efficiency
    nominal = eff_file.Get("data_s0m0")
    if not nominal:
        print("ERROR: Cannot find nominal efficiency (data_s0m0)")
        eff_file.Close()
        return
    
    print(f"\nNominal efficiency histogram:")
    print(f"  Bins: {nominal.GetNbinsX()}")
    print(f"  Dimension: {nominal.GetDimension()}D")
    
    if nominal.GetDimension() == 2:
        print(f"  X-axis bins: {nominal.GetNbinsX()}")
        print(f"  Y-axis bins: {nominal.GetNbinsY()}")
        total_bins = nominal.GetNbinsX() * nominal.GetNbinsY()
    else:
        total_bins = nominal.GetNbinsX()
    
    print(f"  Total physics bins: {total_bins}")
    
    print(f"\nX-axis: {nominal.GetXaxis().GetTitle()}")
    print(f"Y-axis: {nominal.GetYaxis().GetTitle()}")
    
    # Print bin ranges
    print(f"\nBin ranges:")
    if nominal.GetDimension() == 2:
        print("X-axis (eta) bins:")
        for i in range(1, nominal.GetNbinsX() + 1):
            low = nominal.GetXaxis().GetBinLowEdge(i)
            high = nominal.GetXaxis().GetBinUpEdge(i)
            print(f"  Bin {i}: [{low:.2f}, {high:.2f}]")
        
        print("Y-axis (pt) bins:")
        for i in range(1, nominal.GetNbinsY() + 1):
            low = nominal.GetYaxis().GetBinLowEdge(i)
            high = nominal.GetYaxis().GetBinUpEdge(i)
            print(f"  Bin {i}: [{low:.1f}, {high:.1f}]")
    
    print("\n" + "="*60)
    print("BIN-BY-BIN SYSTEMATIC ANALYSIS")
    print("="*60)
    
    large_syst_bins = []
    zero_eff_bins = []
    
    # Check each bin
    if nominal.GetDimension() == 2:
        # 2D histogram
        print("Bin  Eta Range    Pt Range     Efficiency  Stat%   Max_Syst%")
        print("-" * 65)
        
        for ix in range(1, nominal.GetNbinsX() + 1):
            for iy in range(1, nominal.GetNbinsY() + 1):
                bin_idx = nominal.GetBin(ix, iy)
                
                eta_low = nominal.GetXaxis().GetBinLowEdge(ix)
                eta_high = nominal.GetXaxis().GetBinUpEdge(ix)
                pt_low = nominal.GetYaxis().GetBinLowEdge(iy)
                pt_high = nominal.GetYaxis().GetBinUpEdge(iy)
                
                nom_eff = nominal.GetBinContent(bin_idx)
                nom_err = nominal.GetBinError(bin_idx)
                
                if nom_eff == 0:
                    zero_eff_bins.append((ix, iy, bin_idx))
                    print(f"{bin_idx:3d}  [{eta_low:+.1f},{eta_high:+.1f}]  [{pt_low:3.0f},{pt_high:3.0f}]   ZERO_EFF")
                    continue
                
                # Calculate systematic variations
                max_syst_rel = 0
                variations = []
                
                for syst_name in syst_variations:
                    if syst_name == "data_s0m0":
                        continue
                    
                    syst_hist = eff_file.Get(syst_name)
                    if syst_hist:
                        syst_eff = syst_hist.GetBinContent(bin_idx)
                        if syst_eff > 0:
                            syst_rel = abs(syst_eff - nom_eff) / nom_eff * 100
                            variations.append(syst_rel)
                            if syst_rel > max_syst_rel:
                                max_syst_rel = syst_rel
                
                stat_rel = (nom_err / nom_eff) * 100 if nom_eff > 0 else 0
                
                print(f"{bin_idx:3d}  [{eta_low:+.1f},{eta_high:+.1f}]  [{pt_low:3.0f},{pt_high:3.0f}]   {nom_eff:.4f}   {stat_rel:5.2f}   {max_syst_rel:6.2f}")
                
                if max_syst_rel > 2.0:
                    large_syst_bins.append((bin_idx, ix, iy, max_syst_rel, variations))
    
    else:
        # 1D histogram
        print("Bin  Range        Efficiency  Stat%   Max_Syst%")
        print("-" * 50)
        
        for i in range(1, nominal.GetNbinsX() + 1):
            low = nominal.GetXaxis().GetBinLowEdge(i)
            high = nominal.GetXaxis().GetBinUpEdge(i)
            
            nom_eff = nominal.GetBinContent(i)
            nom_err = nominal.GetBinError(i)
            
            if nom_eff == 0:
                zero_eff_bins.append((i, 0, i))
                print(f"{i:3d}  [{low:.2f},{high:.2f}]   ZERO_EFF")
                continue
            
            # Calculate systematic variations
            max_syst_rel = 0
            variations = []
            
            for syst_name in syst_variations:
                if syst_name == "data_s0m0":
                    continue
                
                syst_hist = eff_file.Get(syst_name)
                if syst_hist:
                    syst_eff = syst_hist.GetBinContent(i)
                    if syst_eff > 0:
                        syst_rel = abs(syst_eff - nom_eff) / nom_eff * 100
                        variations.append(syst_rel)
                        if syst_rel > max_syst_rel:
                            max_syst_rel = syst_rel
            
            stat_rel = (nom_err / nom_eff) * 100 if nom_eff > 0 else 0
            
            print(f"{i:3d}  [{low:.2f},{high:.2f}]   {nom_eff:.4f}   {stat_rel:5.2f}   {max_syst_rel:6.2f}")
            
            if max_syst_rel > 2.0:
                large_syst_bins.append((i, 0, 0, max_syst_rel, variations))
    
    print("\n" + "="*60)
    print("SUMMARY AND RECOMMENDATIONS")
    print("="*60)
    
    print(f"Total physics bins: {total_bins}")
    print(f"Bins with zero efficiency: {len(zero_eff_bins)}")
    print(f"Bins with systematic variations > 2%: {len(large_syst_bins)}")
    
    if zero_eff_bins:
        print(f"\n⚠️  ZERO EFFICIENCY BINS (potential fit failures):")
        for bin_info in zero_eff_bins:
            if nominal.GetDimension() == 2:
                bin_idx, ix, iy = bin_info
                eta_low = nominal.GetXaxis().GetBinLowEdge(ix)
                eta_high = nominal.GetXaxis().GetBinUpEdge(ix)
                pt_low = nominal.GetYaxis().GetBinLowEdge(iy)
                pt_high = nominal.GetYaxis().GetBinUpEdge(iy)
                print(f"  Bin {bin_idx}: eta=[{eta_low:+.1f},{eta_high:+.1f}], pt=[{pt_low:.0f},{pt_high:.0f}]")
            else:
                bin_idx = bin_info[0]
                low = nominal.GetXaxis().GetBinLowEdge(bin_idx)
                high = nominal.GetXaxis().GetBinUpEdge(bin_idx)
                print(f"  Bin {bin_idx}: [{low:.2f},{high:.2f}]")
    
    if large_syst_bins:
        print(f"\n⚠️  LARGE SYSTEMATIC VARIATIONS (>2%):")
        for bin_info in large_syst_bins:
            if nominal.GetDimension() == 2:
                bin_idx, ix, iy, max_syst, variations = bin_info
                eta_low = nominal.GetXaxis().GetBinLowEdge(ix)
                eta_high = nominal.GetXaxis().GetBinUpEdge(ix)
                pt_low = nominal.GetYaxis().GetBinLowEdge(iy)
                pt_high = nominal.GetYaxis().GetBinUpEdge(iy)
                print(f"  Bin {bin_idx}: eta=[{eta_low:+.1f},{eta_high:+.1f}], pt=[{pt_low:.0f},{pt_high:.0f}], max_syst={max_syst:.2f}%")
            else:
                bin_idx, _, _, max_syst, variations = bin_info
                low = nominal.GetXaxis().GetBinLowEdge(bin_idx)
                high = nominal.GetXaxis().GetBinUpEdge(bin_idx)
                print(f"  Bin {bin_idx}: [{low:.2f},{high:.2f}], max_syst={max_syst:.2f}%")
    
    if len(zero_eff_bins) == 0 and len(large_syst_bins) == 0:
        print("\n✅ ALL FITS LOOK GOOD!")
        print("   - No zero efficiency bins")
        print("   - All systematic variations < 2%")
        print("   - Fits appear to be converging properly")
    else:
        print(f"\n📋 RECOMMENDATIONS:")
        if zero_eff_bins:
            print("   - Check fit convergence for zero efficiency bins")
            print("   - Review input data statistics for these bins")
        if large_syst_bins:
            print("   - Investigate large systematic variations")
            print("   - May indicate fit instability or model dependence")
            print("   - Consider tighter fit constraints or alternative models")
    
    eff_file.Close()

if __name__ == "__main__":
    detailed_systematic_check()
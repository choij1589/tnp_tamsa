#!/usr/bin/env python3

import os
import argparse
import json
import ROOT
import numpy as np
from itertools import product

parser = argparse.ArgumentParser()
parser.add_argument("--era", type=str, required=True)
args = parser.parse_args()

def main():
    # Setup paths
    root_file = f"results/POGMuon_Run3_v0/NUM_POGMedium_DEN_TrackerMuons_{args.era}/efficiency.root"
    json_file = f"ref_POG/Muon/ScaleFactors_Muon_Z_ID_ISO_{args.era}_schemaV2.json"
    if args.era == "2022EE":
        json_file = f"ref_POG/Muon/ScaleFactors_Muon_Z_ID_ISO_2022_EE_schemaV2.json"
    if args.era == "2023BPix":
        json_file = f"ref_POG/Muon/ScaleFactors_Muon_Z_ID_ISO_2023_BPix_schemaV2.json"

    print(f"Comparing POG Muon Medium ID efficiencies for {args.era}")
    print("=" * 60)

    # Load JSON data
    with open(json_file, 'r') as f:
        json_data = json.load(f)

    # Find MediumID correction
    medium_id_corr = None
    for corr in json_data['corrections']:
        if corr['name'] == 'NUM_MediumID_DEN_TrackerMuons':
            medium_id_corr = corr
            break

    if medium_id_corr is None:
        print("ERROR: Could not find NUM_MediumID_DEN_TrackerMuons in JSON")
        return

    # Extract binning from JSON
    eta_edges = medium_id_corr['data']['edges']
    print(f"Eta edges from JSON: {eta_edges}")

    # Extract pt edges from first eta bin
    first_eta_content = medium_id_corr['data']['content'][0]
    pt_edges = first_eta_content['edges']
    print(f"Pt edges from JSON: {pt_edges}")

    # Create TH2D histogram from JSON data
    n_eta_bins = len(eta_edges) - 1
    n_pt_bins = len(pt_edges) - 1

    h_pog_json = ROOT.TH2D("h_pog_json", "POG JSON;|#eta|;p_{T} [GeV]",
                           n_eta_bins, np.array(eta_edges, dtype=float),
                           n_pt_bins, np.array(pt_edges, dtype=float))

    # Fill histogram with nominal values from JSON
    for eta_idx, eta_bin_content in enumerate(medium_id_corr['data']['content']):
        for pt_idx, pt_bin_content in enumerate(eta_bin_content['content']):
            # Find nominal value
            nominal_value = None
            for item in pt_bin_content['content']:
                if item['key'] == 'nominal':
                    nominal_value = item['value']
                    break

            if nominal_value is not None:
                # ROOT histogram bins are 1-indexed
                h_pog_json.SetBinContent(eta_idx + 1, pt_idx + 1, nominal_value)

    # Load ROOT file with our results
    f_root = ROOT.TFile.Open(root_file)
    h_tnp = f_root.Get("data")
    h_tnp.SetDirectory(0)  # Detach from file

    print(f"\nHistogram comparison:")
    print(f"JSON TH2D: {h_pog_json.GetNbinsX()} x {h_pog_json.GetNbinsY()} bins")
    print(f"TNP ROOT: {h_tnp.GetNbinsX()} x {h_tnp.GetNbinsY()} bins")

    # Load scale factors instead of data efficiencies
    h_tnp_sf = f_root.Get("sf")  # Use scale factors
    h_tnp_sf.SetDirectory(0)

    # Create difference histogram for scale factors
    h_diff = h_tnp_sf.Clone("h_diff")
    h_diff.Add(h_pog_json, -1)
    h_diff.Divide(h_pog_json)

    # Print bin-by-bin comparison
    print(f"\nBin-by-bin comparison:")
    print(f"{'Bin':<4} {'Eta':<8} {'Pt':<8} {'POG':<8} {'TNP':<8} {'Diff%':<8}")
    print("-" * 50)

    bin_count = 0
    for eta_idx in range(1, h_pog_json.GetNbinsX() + 1):
        for pt_idx in range(1, h_pog_json.GetNbinsY() + 1):
            eta_center = h_pog_json.GetXaxis().GetBinCenter(eta_idx)
            pt_center = h_pog_json.GetYaxis().GetBinCenter(pt_idx)

            pog_val = h_pog_json.GetBinContent(eta_idx, pt_idx)
            tnp_val = h_tnp_sf.GetBinContent(eta_idx, pt_idx)

            if pog_val > 0 and tnp_val > 0:  # Only compare non-zero bins
                diff_percent = (tnp_val - pog_val) / pog_val * 100
                print(f"{bin_count:<4} {eta_center:<8.2f} {pt_center:<8.1f} {pog_val:<8.4f} {tnp_val:<8.4f} {diff_percent:<8.3f}")
                bin_count += 1

    # Create and save comparison plot
    ROOT.gStyle.SetPaintTextFormat(".3f")
    
    text = ROOT.TLatex()
    def setCOMText():
        text.SetTextSize(0.035)
        text.SetTextFont(42)
    
    def setCMSText():
        text.SetTextSize(0.04)
        text.SetTextFont(61)
    
    def setWIPText():
        text.SetTextSize(0.036)
        text.SetTextFont(52)
   
    c = ROOT.TCanvas("c_comparison", "Efficiency Comparison", 1300, 1200)
    c.cd()
    
    h_diff.SetTitle("(TNP - POG) / POG")
    h_diff.Draw("colz text")
    
    setCOMText(); text.DrawLatexNDC(0.74, 0.91, f"{args.era}, 13.6 TeV")
    setCMSText(); text.DrawLatexNDC(0.11, 0.91, "CMS")
    setWIPText(); text.DrawLatexNDC(0.18, 0.91, "Preliminary")

    c.SaveAs(f"muon_scalefactor_comparison_{args.era}.png")
    print(f"\nComparison plot saved as: muon_scalefactor_comparison_{args.era}.png")

    f_root.Close()

if __name__ == "__main__":
    main()

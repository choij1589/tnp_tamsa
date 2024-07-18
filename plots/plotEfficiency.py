import os
import argparse
import tdrstyle
import ROOT
tdrstyle.setTDRStyle(square=False)
ROOT.gStyle.SetErrorX(0.5)

parser = argparse.ArgumentParser()
parser.add_argument("--key", required=True, type=str, help="which efficiency to plot")
parser.add_argument("--era", required=True, type=str, help="era")
args = parser.parse_args()

# lumi
lumiinfo = {"2016a": 19517,
            "2016b": 16812,
            "2017": 41477,
            "2018": 59827}
lumi = lumiinfo[args.era]

# hist arguments
x_range = (10., 200.)
y_range = (0.6, 1.02)
sf_range = (0.9, 1.1)
if "Mu17Leg1" in args.key:
    x_range = (17., 200.)
    y_range = (0.3, 1.02)
    sf_range = (0.6, 1.4)

# get histograms
f = ROOT.TFile.Open(f"{os.environ['TNP_BASE']}/results/TopHNT_Muon_v1/{args.key}_{args.era}/efficiency.root")
h_data = f.Get("data"); h_data.SetDirectory(0)
h_sim  = f.Get("sim"); h_sim.SetDirectory(0)
h_sf = f.Get("sf"); h_sf.SetDirectory(0)
f.Close()

# projections
# TODO: automate based on pt/eta-binning?
# data projection
h_data_projy1 = h_data.ProjectionY("data_py1", 1, 1)
h_data_projy2 = h_data.ProjectionY("data_py2", 2, 2)
h_data_projy3 = h_data.ProjectionY("data_py3", 3, 3)
h_data_projy4 = h_data.ProjectionY("data_py4", 4, 4)

# mc projection
h_sim_projy1 = h_sim.ProjectionY("sim_py1", 1, 1)
h_sim_projy2 = h_sim.ProjectionY("sim_py2", 2, 2)
h_sim_projy3 = h_sim.ProjectionY("sim_py3", 3, 3)
h_sim_projy4 = h_sim.ProjectionY("sim_py4", 4, 4)

# sf projection
h_sf_projy1 = h_sf.ProjectionY("sf_py1", 1, 1)
h_sf_projy2 = h_sf.ProjectionY("sf_py2", 2, 2)
h_sf_projy3 = h_sf.ProjectionY("sf_py3", 3, 3)
h_sf_projy4 = h_sf.ProjectionY("sf_py4", 4, 4)

# color configuration
h_data_projy1.SetLineStyle(1)
h_data_projy1.SetLineColor(ROOT.kBlack)
h_data_projy1.SetLineWidth(2)
h_data_projy1.SetMarkerStyle(8)
h_data_projy1.SetMarkerColor(ROOT.kBlack)
h_data_projy1.SetMarkerSize(2)

h_sim_projy1.SetLineStyle(2)
h_sim_projy1.SetLineColor(ROOT.kBlack)
h_sim_projy1.SetLineWidth(2)
h_sim_projy1.SetMarkerStyle(8)
h_sim_projy1.SetMarkerColor(ROOT.kBlack)
h_sim_projy1.SetMarkerSize(2)

h_sf_projy1.SetLineStyle(1)
h_sf_projy1.SetLineColor(ROOT.kBlack)
h_sf_projy1.SetLineWidth(2)
h_sf_projy1.SetMarkerStyle(8)
h_sf_projy1.SetMarkerColor(ROOT.kBlack)
h_sf_projy1.SetMarkerSize(2)


h_data_projy2.SetLineStyle(1)
h_data_projy2.SetLineColor(ROOT.kBlue)
h_data_projy2.SetLineWidth(2)
h_data_projy2.SetMarkerStyle(8)
h_data_projy2.SetMarkerColor(ROOT.kBlue)
h_data_projy2.SetMarkerSize(2)

h_sim_projy2.SetLineStyle(2)
h_sim_projy2.SetLineColor(ROOT.kBlue)
h_sim_projy2.SetLineWidth(2)
h_sim_projy2.SetMarkerStyle(8)
h_sim_projy2.SetMarkerColor(ROOT.kBlue)
h_sim_projy2.SetMarkerSize(2)

h_sf_projy2.SetLineStyle(1)
h_sf_projy2.SetLineColor(ROOT.kBlue)
h_sf_projy2.SetLineWidth(2)
h_sf_projy2.SetMarkerStyle(8)
h_sf_projy2.SetMarkerColor(ROOT.kBlue)
h_sf_projy2.SetMarkerSize(2)


h_data_projy3.SetLineStyle(1)
h_data_projy3.SetLineColor(ROOT.kGreen)
h_data_projy3.SetLineWidth(2)
h_data_projy3.SetMarkerStyle(8)
h_data_projy3.SetMarkerColor(ROOT.kGreen)
h_data_projy3.SetMarkerSize(2)

h_sim_projy3.SetLineStyle(2)
h_sim_projy3.SetLineColor(ROOT.kGreen)
h_sim_projy3.SetLineWidth(2)
h_sim_projy3.SetMarkerStyle(8)
h_sim_projy3.SetMarkerColor(ROOT.kGreen)
h_sim_projy3.SetMarkerSize(2)

h_sf_projy3.SetLineStyle(1)
h_sf_projy3.SetLineColor(ROOT.kGreen)
h_sf_projy3.SetLineWidth(2)
h_sf_projy3.SetMarkerStyle(8)
h_sf_projy3.SetMarkerColor(ROOT.kGreen)
h_sf_projy3.SetMarkerSize(2)


h_data_projy4.SetLineStyle(1)
h_data_projy4.SetLineColor(ROOT.kRed)
h_data_projy4.SetLineWidth(2)
h_data_projy4.SetMarkerStyle(8)
h_data_projy4.SetMarkerColor(ROOT.kRed)
h_data_projy4.SetMarkerSize(2)

h_sim_projy4.SetLineStyle(2)
h_sim_projy4.SetLineColor(ROOT.kRed)
h_sim_projy4.SetLineWidth(2)
h_sim_projy4.SetMarkerStyle(8)
h_sim_projy4.SetMarkerColor(ROOT.kRed)
h_sim_projy4.SetMarkerSize(2)

h_sf_projy4.SetLineStyle(1)
h_sf_projy4.SetLineColor(ROOT.kRed)
h_sf_projy4.SetLineWidth(2)
h_sf_projy4.SetMarkerStyle(8)
h_sf_projy4.SetMarkerColor(ROOT.kRed)
h_sf_projy4.SetMarkerSize(2)

h_line = h_data_projy1.Clone("line")
for i in range(h_line.GetNbinsX()+1):
    h_line.SetBinContent(i, 1.)
    h_line.SetBinError(i, 0.)
h_line.SetMarkerStyle(1)
h_line.SetLineStyle(3)
h_line.SetLineWidth(2)

# axis configuration
# h_data_projy1 is the first plot to be drawn in the pad_up
h_data_projy1.SetStats(0)
h_data_projy1.GetXaxis().SetLabelSize(0)
h_data_projy1.GetXaxis().SetRangeUser(*x_range)
h_data_projy2.GetXaxis().SetRangeUser(*x_range)
h_data_projy3.GetXaxis().SetRangeUser(*x_range)
h_data_projy4.GetXaxis().SetRangeUser(*x_range)
h_data_projy1.GetYaxis().SetTitle("Efficiency")
h_data_projy1.GetYaxis().SetTitleSize(0.04)
h_data_projy1.GetYaxis().SetTitleOffset(1.3)
h_data_projy1.GetYaxis().SetLabelSize(0.03)
h_data_projy1.GetYaxis().SetRangeUser(*y_range)

h_sim_projy1.GetXaxis().SetRangeUser(*x_range)
h_sim_projy2.GetXaxis().SetRangeUser(*x_range)
h_sim_projy3.GetXaxis().SetRangeUser(*x_range)
h_sim_projy4.GetXaxis().SetRangeUser(*x_range)

# h_sf_projy1 is the first plot to be drawn in the pad_down
h_sf_projy1.SetStats(0)
h_sf_projy1.GetXaxis().SetTitle("p_{T} [GeV]")
h_sf_projy1.GetXaxis().SetMoreLogLabels()
h_sf_projy1.GetXaxis().SetTitleSize(0.1)
h_sf_projy1.GetXaxis().SetTitleOffset(1.2)
h_sf_projy1.GetXaxis().SetLabelSize(0.1)
h_sf_projy1.GetXaxis().SetRangeUser(*x_range)
h_sf_projy2.GetXaxis().SetRangeUser(*x_range)
h_sf_projy3.GetXaxis().SetRangeUser(*x_range)
h_sf_projy4.GetXaxis().SetRangeUser(*x_range)
h_sf_projy1.GetYaxis().SetTitle("S.F.")
h_sf_projy1.GetYaxis().CenterTitle()
h_sf_projy1.GetYaxis().SetTitleSize(0.1)
h_sf_projy1.GetYaxis().SetTitleOffset(0.6)
h_sf_projy1.GetYaxis().SetLabelSize(0.08)
h_sf_projy1.GetYaxis().SetRangeUser(*sf_range)

# combine elements
legend_args = (0.6, 0.1, 0.9, 0.4, '', 'NDC')
legend = ROOT.TLegend(*legend_args)
legend.SetFillStyle(0)
legend.AddEntry(h_data_projy1, "data (|#eta| < 0.9)", "lep")
legend.AddEntry(h_sim_projy1, "MC (|#eta| < 0.9)", "lep")
legend.AddEntry(h_data_projy2, "data (0.9 < |#eta| < 1.2)", "lep")
legend.AddEntry(h_sim_projy2, "MC (0.9 < |#eta| < 1.2)", "lep")
legend.AddEntry(h_data_projy3, "data (1.2 < |#eta| < 2.1)", "lep")
legend.AddEntry(h_sim_projy3, "MC (1.2 < |#eta| < 2.1)", "lep")
legend.AddEntry(h_data_projy4, "data (2.1 < |#eta| < 2.4)", "lep")
legend.AddEntry(h_sim_projy4, "MC (2.1 < |#eta| < 2.4)", "lep")

canvas = ROOT.TCanvas("canvas", "", 1440, 1800)
pad_up = ROOT.TPad("up", "", 0., 0.25, 1, 1)
pad_down = ROOT.TPad("down", "", 0, 0, 1, 0.25)

text = ROOT.TLatex()
def setCMSText():
    text.SetTextSize(0.035)
    text.SetTextFont(61)

def setPrelimText():
    text.SetTextSize(0.035)
    text.SetTextFont(52)

pad_up.SetLogx()
#pad_up.SetGridx()
pad_up.SetTopMargin(0.055)
pad_up.SetBottomMargin(0.02)
pad_up.SetLeftMargin(0.13)
#pad_up.SetRightMargin(0.08)

pad_down.SetLogx()
#pad_down.SetGridx()
#pad_down.SetGridy()
pad_down.SetTopMargin(0.021)
pad_down.SetBottomMargin(0.25)
pad_down.SetLeftMargin(0.13)
#pad_down.SetRightMargin(0.08)

pad_up.cd()
h_data_projy1.Draw()
h_data_projy2.Draw("same")
h_data_projy3.Draw("same")
h_data_projy4.Draw("same")
h_sim_projy1.Draw("same")
h_sim_projy2.Draw("same")
h_sim_projy3.Draw("same")
h_sim_projy4.Draw("same")
h_line.Draw("same")
legend.Draw("same")
pad_up.RedrawAxis()

pad_down.cd()
h_sf_projy1.Draw()
h_sf_projy2.Draw("same")
h_sf_projy3.Draw("same")
h_sf_projy4.Draw("same")
h_line.Draw("same")
pad_down.RedrawAxis()

canvas.cd()
pad_up.Draw()
pad_down.Draw()
setCMSText(); text.DrawLatexNDC(0.13, 0.965, "CMS")
setPrelimText(); text.DrawLatexNDC(0.23, 0.965, "Preliminary")
tdrstyle.cmsPrel(lumi, 13.)
canvas.Update()

savepath= f"plots/{args.key}/efficiency.{args.era}.png"
os.makedirs(os.path.dirname(savepath), exist_ok=True)
canvas.SaveAs(savepath)

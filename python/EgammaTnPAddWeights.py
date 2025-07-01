#!/usr/bin/env python3
import os,sys,math
from array import array
import ROOT

infilename=sys.argv[1]
outfilename=sys.argv[2]
if not infilename.endswith(".root"):
    print("input file is not ROOT format: "+infilename)
    exit(1)
if not outfilename.endswith(".root"):
    print("output file is not ROOT format: "+outfilename)
    exit(1)

infile=ROOT.TFile(sys.argv[1])
if os.path.dirname(outfilename)!="" and not os.path.exists(os.path.dirname(outfilename)):
    try:
        os.makedirs(os.path.dirname(outfilename))
    except OSError:
        if os.path.exists(os.path.dirname(outfilename)):
            pass
        else:
            print("Cannot make output directory")
            exit(1)
outfile=ROOT.TFile(sys.argv[2],"recreate")

tree=infile.Get("tnpEleReco/fitter_tree")
tree.SetBranchStatus("PUweight",0)
tree.SetBranchStatus("totWeight",0)

outfile.cd()
newtree=tree.CloneTree(0)

if "2016a" in infilename or "2016preVFP" in infilename:
    era="2016preVFP"
    erashort="2016a"
elif "2016b" in infilename or "2016postVFP" in infilename:
    era="2016postVFP"
    erashort="2016b"
elif "2017" in infilename:
    era="2017"
    erashort="2017"
elif "2018" in infilename:
    era="2018"
    erashort="2018"
else:
    print("Unknown era")
    exit(1)
    
ROOT.TH1.AddDirectory(0)

## PUweight
PUweight=array("f",[float()])
newtree.Branch("PUweight",PUweight,"PUweight/F")
PUweight_up=array("f",[float()])
newtree.Branch("PUweight_up",PUweight_up,"PUweight_up/F")
PUweight_down=array("f",[float()])
newtree.Branch("PUweight_down",PUweight_down,"PUweight_down/F")
fPUweight=ROOT.TFile("/data6/Users/hsseo/SKFlatAnalyzer_UL/data/Run2UltraLegacy_v3/{}/PileUp/PileupWeight{}.root".format(era,era)).Get("MC_{}_central".format(era))
fPUweight_up=ROOT.TFile("/data6/Users/hsseo/SKFlatAnalyzer_UL/data/Run2UltraLegacy_v3/{}/PileUp/PileupWeight{}.root".format(era,era)).Get("MC_{}_sig_up".format(era))
fPUweight_down=ROOT.TFile("/data6/Users/hsseo/SKFlatAnalyzer_UL/data/Run2UltraLegacy_v3/{}/PileUp/PileupWeight{}.root".format(era,era)).Get("MC_{}_sig_down".format(era))

## prefireweight
prefireweight=array("f",[float()])
newtree.Branch("prefireweight",prefireweight,"prefireweight/F")
prefireweight_up=array("f",[float()])
newtree.Branch("prefireweight_up",prefireweight_up,"prefireweight_up/F")
prefireweight_down=array("f",[float()])
newtree.Branch("prefireweight_down",prefireweight_down,"prefireweight_down/F")
fPrefiringMap=None
if era=="2016preVFP":
    fPrefiringMap=ROOT.TFile("/data6/Users/hsseo/SKFlatAnalyzer_UL/data/Run2UltraLegacy_v3/2016preVFP/SMP/L1PrefiringMaps.root").Get("L1prefiring_photonptvseta_UL2016preVFP")
elif era=="2016postVFP":
    fPrefiringMap=ROOT.TFile("/data6/Users/hsseo/SKFlatAnalyzer_UL/data/Run2UltraLegacy_v3/2016preVFP/SMP/L1PrefiringMaps.root").Get("L1prefiring_photonptvseta_UL2016postVFP")
elif era=="2017":
    fPrefiringMap=ROOT.TFile("/data6/Users/hsseo/SKFlatAnalyzer_UL/data/Run2UltraLegacy_v3/2016preVFP/SMP/L1PrefiringMaps.root").Get("L1prefiring_photonptvseta_UL2017BtoF")
def GetPrefiringRate(eta,pt,sys):
    if not fPrefiringMap: 
        return 0.
    prefiringRateSystUncEcal_=0.2;
    #Check pt is not above map overflow
    nbinsy = fPrefiringMap.GetNbinsY();
    maxy = fPrefiringMap.GetYaxis().GetBinLowEdge(nbinsy + 1);
    if pt >= maxy:
        pt = maxy - 0.01;
    if pt<20.:
        return 0.
    abseta=abs(eta);
    if abseta<2. or abseta>3.:
        return 0.
    thebin = fPrefiringMap.FindBin(eta, pt);

    prefrate = fPrefiringMap.GetBinContent(thebin);

    statuncty = fPrefiringMap.GetBinError(thebin);
    systuncty = prefiringRateSystUncEcal_ * prefrate;

    if sys > 0:
        prefrate = min(1., prefrate + math.sqrt(statuncty**2 + systuncty**2));
    elif sys < 0:
        prefrate = max(0., prefrate - math.sqrt(statuncty**2 + systuncty**2));
    if prefrate > 1.:
        prefrate=1.
    return prefrate;

## zptweight
zptweight=array("f",[float()])
newtree.Branch("zptweight",zptweight,"zptweight/F")
if "DYJetsTo" in infilename and "MiNNLO" in infilename:
    sample="MiNNLO"
elif "DYJetsToLL" in infilename and "madgraph" in infilename:
    sample="DYJets_MG"
elif "DYJetsToLL" in infilename and "amcatnlo" in infilename:
    sample="DYJets"
else:
    print("Unknown sample")
    exit(1)
fZptWeight=ROOT.TFile("/data6/Users/hsseo/SKFlatAnalyzer_UL/data/Run2UltraLegacy_v3/{}/SMP/ZptWeight_{}.root".format(era,sample)).Get("zptweight_g")

## z0weight
z0weight=array("f",[float()])
newtree.Branch("z0weight",z0weight,"z0weight/F")
def GetZ0Weight(era,z0):
    rt=1.
    if era=="2016preVFP":
        data_val=ROOT.TMath.Gaus(z0,2.46312e-01,3.50458e+00,True)
        mc_val=ROOT.TMath.Gaus(z0,9.28612e-01,3.65203e+00,True)
        rt=data_val/mc_val
    elif era=="2016postVFP":
        data_val=ROOT.TMath.Gaus(z0,2.41640e-01,3.63717e+00,True)
        mc_val=ROOT.TMath.Gaus(z0,9.30108e-01,3.65454e+00,True)
        rt=data_val/mc_val
    elif era=="2017":
        data_val=ROOT.TMath.Gaus(z0,3.81830e-01,3.67614e+00,True)
        mc_val=ROOT.TMath.Gaus(z0,8.19642e-01,3.50992e+00,True)
        rt=data_val/mc_val
    elif era=="2018":
        data_val=ROOT.TMath.Gaus(z0,-1.36030e-01,3.41464e+00,True)
        mc_val=ROOT.TMath.Gaus(z0,3.58575e-02,3.50953e+00,True)
        rt=data_val/mc_val
    if rt>2:
        rt=2
    return rt

## Loop
for i in range(tree.GetEntries()):
    tree.GetEntry(i)
    PUweight[0]=fPUweight.GetBinContent(fPUweight.FindBin(tree.truePU))
    PUweight_up[0]=fPUweight_up.GetBinContent(fPUweight_up.FindBin(tree.truePU))
    PUweight_down[0]=fPUweight_down.GetBinContent(fPUweight_down.FindBin(tree.truePU))
    prefireweight[0]=(1-GetPrefiringRate(tree.tag_Ele_eta,tree.tag_Ele_pt,0))*(1-GetPrefiringRate(tree.sc_eta,tree.sc_pt,0))
    prefireweight_up[0]=(1-GetPrefiringRate(tree.tag_Ele_eta,tree.tag_Ele_pt,1))*(1-GetPrefiringRate(tree.sc_eta,tree.sc_pt,1))
    prefireweight_down[0]=(1-GetPrefiringRate(tree.tag_Ele_eta,tree.tag_Ele_pt,-1))*(1-GetPrefiringRate(tree.sc_eta,tree.sc_pt,-1))
    zptweight[0]=fZptWeight.Eval(tree.pair_pt)
    z0weight[0]=GetZ0Weight(era,tree.mPVz)

    newtree.Fill()

outfile.mkdir("tnpEleReco")
outfile.cd("tnpEleReco")
newtree.Write()
outfile.Close()

    



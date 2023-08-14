from tnpConfig import tnpConfig

#### samples
samples = {
    "data2016a": "/gv0/Users/jbhyun/TagAndProbe/muon/Z/v220707/Run2016_UL_HIPM/SingleMuon",
    "mi2016a": "/gv0/Users/jbhyun/TagAndProbe/muon/Z/v220707/Run2016_UL_HIPM/DYJetsToMuMu_M-50_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos",
    "mg2016a": "/gv0/Users/jbhyun/TagAndProbe/muon/Z/v220707/Run2016_UL_HIPM/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8",
    "data2016b": "/gv0/Users/jbhyun/TagAndProbe/muon/Z/v220707/Run2016_UL/SingleMuon",
    "mi2016b": "/gv0/Users/jbhyun/TagAndProbe/muon/Z/v220707/Run2016_UL/DYJetsToMuMu_M-50_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos",
    "mg2016b": "/gv0/Users/jbhyun/TagAndProbe/muon/Z/v220707/Run2016_UL/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8",
    "data2017": "/gv0/Users/jbhyun/TagAndProbe/muon/Z/v220707/Run2017_UL/SingleMuon",
    "mi2017": "/gv0/Users/jbhyun/TagAndProbe/muon/Z/v220707/Run2017_UL/DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos",
    "mg2017": "/gv0/Users/jbhyun/TagAndProbe/muon/Z/v220707/Run2017_UL/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8",
    "data2018": "/gv0/Users/jbhyun/TagAndProbe/muon/Z/v220707/Run2018_UL/SingleMuon",
    "mi2018": "/gv0/Users/jbhyun/TagAndProbe/muon/Z/v220707/Run2018_UL/DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos",
    "mg2018": "/gv0/Users/jbhyun/TagAndProbe/muon/Z/v220707/Run2018_UL/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8"
}

#### binning
binnings = {
    "ID": [
        {"var": "abs(probe_eta)",
         "type": "float",
         "bins": [0., 0.9, 1.2, 2.1, 2.4],
         "title": "|#eta|"},
        {"var": "probe_pt",
         "type": "float",
         "bins": [15, 20, 25, 30, 40, 50, 60, 120],
         "title": "p_{T} [GeV]"
        }
    ]
}

#### fit parameters
fit_nominal = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    #"Fit sigPass histPass_genmatching",
    #"Fit sigFail histFail_genmatching",
    #"SetConstant meanGaussP sigmaP meanGaussF sigmaF",
    "RooCMSShape::bkgPass(x, aCMSP[50.,40.,80.],bCMSP[0.1, 0.01,0.25],cCMSP[0.05, 0.0001,0.2],peakCMSP[90.0])",
    "RooCMSShape::bkgFail(x, aCMSF[50.,40.,80.],bCMSF[0.1, 0.01,0.25],cCMSF[0.05, 0.0001,0.2],peakCMSF[90.0])",
    #"Fit bkgPass histPass_notgenmatching",
    #"Fit bkgFail histPass_notgenmatching",
    #"SetConstant aCMSP bCMSP cCMSP aCMSF bCMSF cCMSF"
]
fit_altsig = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_genmass,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_genmass,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.8,0.5,3.5])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[1.4,0.8,2.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x, aCMSP[60., 50.,80.],bCMSP[0.03, 0.01,0.05],cCMSP[0.1, -0.1,1.0],peakCMSP[90.0])",
    "RooCMSShape::bkgFail(x, aCMSF[61.5, 50.,80.],bCMSF[0.03, 0.01,0.05],cCMSF[0.03, -0.1,1.0],peakCMSF[90.0])",
]

#### definition
expr_16UL = "probe_isTracker && abs(probe_dxy) < 0.2 && abs(probe_dz) < 0.5 && tag_isTight && tag_pt > 26. && tag_relIso04 < 0.2 && tag_HLT_IsoMu24_v == 1 && pair_probeMultiplicity == 1"
expr_17UL = "probe_isTracker && abs(probe_dxy) < 0.2 && abs(probe_dz) < 0.5 && tag_isTight && tag_pt > 29. && tag_relIso04 < 0.2 && tag_HLT_IsoMu27_v == 1 && pair_probeMultiplicity == 1" 
expr_18UL = expr_16UL

#### configs
Configs = {}
config = tnpConfig(
    data = samples["data2016a"],
    sim = samples["mg2016a"],
    sim_weight = "genWeight",
    sim_maxweight = 1e5,
    sim_genmatching = "tag_isMatchedGen && probe_isMatchedGen",
    sim_genmass = "genMass",
    tree = "muon/Events",
    mass = "pair_mass",
    bins = binnings['ID'],
    expr = expr_16UL,
    test = "probe_CutBasedIdMedium",
    hist_nbins = 140,
    hist_range = (65, 135),
    method = "fit",
    fit_parameter = fit_nominal,
    fit_range = (70, 130),
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
    ],
)
Configs["NUM_POGMedium_DEN_TrackerMuons_2016a"] = config.clone()
Configs["NUM_POGMedium_DEN_TrackerMuons_2016b"] = config.clone(
    data = samples["data2016b"],
    sim = samples["mg2016b"],
)
Configs["NUM_POGMedium_DEN_TrackerMuons_2017"] = config.clone(
    data = samples["data2017"],
    sim = samples["mg2017"],
    expr = expr_17UL
)
Configs["NUM_POGMedium_DEN_TrackerMuons_2018"] = config.clone(
    data = samples["data2018"],
    sim = samples["mg2018"],
    expr = expr_18UL
)

if __name__ == "__main__":
    for key in sorted(Configs.keys()):
        print key

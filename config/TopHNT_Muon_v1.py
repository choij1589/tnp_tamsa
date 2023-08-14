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
        {"var": "abs(probe_eta)", "type": "float", "bins": [0., 0.9, 1.2, 2.1, 2.4], "title": "|#eta|"},
        {"var": "probe_pt", "type": "float", "bins": [10, 15, 20, 25, 30, 40, 50, 60, 120, 200], "title": "p_{T} [GeV]"}
    ],
    "Mu8": [
        {"var": "abs(probe_eta)", "type": "float", "bins": [0., 0.9, 1.2, 2.1, 2.4], "title": "|#eta|"},
        {"var": "probe_pt", "type": "float", "bins": [10., 15., 20., 25., 30., 40., 50., 100., 200.], "title": "p_{T} [GeV]"}
    ],
    "Mu17": [
        {"var": "abs(probe_eta)", "type": "float", "bins": [0., 0.9, 1.2, 2.1, 2.4], "title": "|#eta|"},
        {"var": "probe_pt", "type": "float", "bins": [10., 14., 16., 18., 20., 25., 30., 40., 50., 100., 200.], "title": "p_{T} [GeV]"}
    ],
    # to aviod zero contents
    "Mu17_1718": [
        {"var": "abs(probe_eta)", "type": "float", "bins": [0., 0.9, 1.2, 2.1, 2.4], "title": "|#eta|"},
        {"var": "probe_pt", "type": "float", "bins": [10., 16., 18., 20., 25., 30., 40., 50., 100., 200.], "title": "p_{T} [GeV]"}
    ]
}

#### fit parameters
fit_nominal = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[1.5,0.02,4.0])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[1.5,0.04,4.0])",
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
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[1.5,1.2,4.0])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[1.5,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x, aCMSP[50.,40.,80.],bCMSP[0.1, 0.01,0.25],cCMSP[0.05,0.0001,0.2],peakCMSP[90.0])",
    "RooCMSShape::bkgFail(x, aCMSF[50.,40.,80.],bCMSF[0.1, 0.01,0.25],cCMSF[0.05,0.0001,0.2],peakCMSF[90.0])",
]

#### definition
expr_16UL = "(probe_isTracker && abs(probe_dxy) < 0.2 && abs(probe_dz) < 0.5 && tag_isTight && tag_pt > 26. && tag_HLT_IsoMu24_v == 1 && pair_probeMultiplicity == 1 && (tag_pfIso04_charged+max(0,tag_pfIso04_neutral+tag_pfIso04_photon-0.5*tag_pfIso04_sumPU) < 0.2*tag_pt))"
expr_17UL = "(probe_isTracker && abs(probe_dxy) < 0.2 && abs(probe_dz) < 0.5 && tag_isTight && tag_pt > 29. && tag_HLT_IsoMu27_v == 1 && pair_probeMultiplicity == 1 && (tag_pfIso04_charged+max(0,tag_pfIso04_neutral+tag_pfIso04_photon-0.5*tag_pfIso04_sumPU) < 0.2*tag_pt))" 
expr_18UL = expr_16UL

## ID
TopHNT = "(probe_CutBasedIdMedium && abs(probe_dz) < 0.1 && (probe_3DIPerrVTX != 0 && abs(probe_3DIPVTX) < 3.*probe_3DIPerrVTX) && probe_iso03_sumPt < 0.4*probe_pt && (probe_miniIso_rhoAll < 0.1))"

## triggers
Mu17Mu8_17leg_16ab     = 'probe_hltL3fL1sDoubleMu114L1f0L2f10OneMuL3Filtered17_dr<0.3 && probe_hltDiMuonGlb17Glb8RelTrkIsoFiltered0p4_dr<0.3'
Mu17TkMu8_17leg_16ab   = 'probe_hltL3fL1sDoubleMu114L1f0L2f10L3Filtered17_dr<0.3 && probe_hltDiMuonGlb17Trk8RelTrkIsoFiltered0p4_dr<0.3'
TkMu17TkMu8_17leg_16ab = 'probe_hltL3fL1sDoubleMu114TkFiltered17Q_dr<0.3 && probe_hltDiMuonTrk17Trk8RelTrkIsoFiltered0p4_dr<0.3'
Mu17Mu8_8leg_16ab      = 'probe_hltDiMuonGlb17Glb8RelTrkIsoFiltered0p4_dr<0.3'
Mu17TkMu8_8leg_16ab    = 'probe_hltDiMuonGlb17Trk8RelTrkIsoFiltered0p4_dr<0.3'
TkMu17TkMu8_8leg_16ab  = 'probe_hltDiMuonTrk17Trk8RelTrkIsoFiltered0p4_dr<0.3'
Mu17Mu8_17leg_1718     = 'probe_hltL3fL1DoubleMu155fFiltered17_dr<0.3 && probe_hltDiMuon178RelTrkIsoFiltered0p4_dr<0.3'
Mu17Mu8_8leg_1718      = 'probe_hltDiMuon178RelTrkIsoFiltered0p4_dr<0.3'
Mu17Leg1_16   = '( ('+Mu17Mu8_17leg_16ab+') || ('+Mu17TkMu8_17leg_16ab+') || ('+TkMu17TkMu8_17leg_16ab+') )'
Mu8Leg2_16    = '('+Mu17Mu8_8leg_16ab+' || '+Mu17TkMu8_8leg_16ab+' || '+TkMu17TkMu8_8leg_16ab+')'
Mu17Leg1_1718 = Mu17Mu8_17leg_1718
Mu8Leg2_1718  = Mu17Mu8_8leg_1718



#### configs
## ID
Configs = {}
config = tnpConfig(
    data = samples["data2016a"],
    sim = samples["mi2016a"],
    sim_weight = "genWeight",
    sim_maxweight = 1e5,
    sim_genmatching = "tag_isMatchedGen && probe_isMatchedGen",
    sim_genmass = "genMass",
    tree = "muon/Events",
    mass = "pair_mass",
    bins = binnings['ID'],
    expr = expr_16UL,
    test = TopHNT,
    hist_nbins = 148,
    hist_range = (53, 127),
    method = "fit",
    fit_parameter = fit_nominal,
    fit_range = (60, 120),
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "tagIso0p3", "expr": expr_16UL.replace("0.2*tag_pt", "0.3*tag_pt")},
         {"title": "tagIso0p1", "expr": expr_16UL.replace("0.2*tag_pt", "0.1*tag_pt")}],
        [{"title": "massbinmore", "hist_nbins": 296},
         {"title": "massbinless", "hist_nbins": 74}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}]
    ],
)
Configs["NUM_TopHNT_DEN_TrackerMuons_2016a"] = config.clone()
Configs["NUM_TopHNT_DEN_TrackerMuons_2016b"] = config.clone(
    data = samples["data2016b"],
    sim = samples["mi2016b"],
)
Configs["NUM_TopHNT_DEN_TrackerMuons_2017"] = config.clone(
    data = samples["data2017"],
    sim = samples["mi2017"],
    expr = expr_17UL,
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "tagIso0p3", "expr": expr_17UL.replace("0.2*tag_pt", "0.3*tag_pt")},
         {"title": "tagIso0p1", "expr": expr_17UL.replace("0.2*tag_pt", "0.1*tag_pt")}],
        [{"title": "massbinmore", "hist_nbins": 296},
         {"title": "massbinless", "hist_nbins": 74}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}]
    ],
)
Configs["NUM_TopHNT_DEN_TrackerMuons_2018"] = config.clone(
    data = samples["data2018"],
    sim = samples["mi2018"],
    expr = expr_18UL,
    systemtaics = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "tagIso0p3", "expr": expr_18UL.replace("0.2*tag_pt", "0.3*tag_pt")},
         {"title": "tagIso0p1", "expr": expr_18UL.replace("0.2*tag_pt", "0.1*tag_pt")}],
        [{"title": "massbinmore", "hist_nbins": 296},
         {"title": "massbinless", "hist_nbins": 74}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}]
    ],
)

## Mu17
configLeg1 = tnpConfig(
    data = samples["data2016a"],
    sim = samples["mi2016a"],
    sim_weight = "genWeight",
    sim_maxweight = 1e5,
    sim_genmatching = "tag_isMatchedGen && probe_isMatchedGen",
    sim_genmass = "genMass",
    tree = "muon/Events",
    mass = "pair_mass",
    bins = binnings['Mu17'],
    expr = expr_16UL+" && "+TopHNT,
    test = Mu17Leg1_16,
    hist_nbins = 148,
    hist_range = (53, 127),
    method = "fit",
    fit_parameter = fit_nominal,
    fit_range = (60, 120),
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "tagIso0p3", "expr": expr_16UL.replace("0.2*tag_pt", "0.3*tag_pt")+" && "+TopHNT},
         {"title": "tagIso0p1", "expr": expr_16UL.replace("0.2*tag_pt", "0.1*tag_pt")+" && "+TopHNT}],
        [{"title": "massbinmore", "hist_nbins": 296},
         {"title": "massbinless", "hist_nbins": 74}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}]
    ],
)

Configs["NUM_Mu17Leg1_DEN_TopHNT_2016a"] = configLeg1.clone()
Configs["NUM_Mu17Leg1_DEN_TopHNT_2016b"] = configLeg1.clone(
    data = samples["data2016b"],
    sim = samples["mi2016b"]
)
Configs["NUM_Mu17Leg1_DEN_TopHNT_2017"] = configLeg1.clone(
    data = samples["data2017"],
    sim = samples["mi2017"],
    expr = expr_17UL+" && "+TopHNT,
    test = Mu17Leg1_1718,
    bins = binnings["Mu17_1718"],
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "tagIso0p3", "expr": expr_17UL.replace("0.2*tag_pt", "0.3*tag_pt")+" && "+TopHNT},
         {"title": "tagIso0p1", "expr": expr_17UL.replace("0.2*tag_pt", "0.1*tag_pt")+" && "+TopHNT}],
        [{"title": "massbinmore", "hist_nbins": 296},
         {"title": "massbinless", "hist_nbins": 74}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}]
    ]      
)
Configs["NUM_Mu17Leg1_DEN_TopHNT_2018"] = configLeg1.clone(
    data = samples["data2018"],
    sim = samples["mi2018"],
    expr = expr_18UL+" && "+TopHNT,
    test = Mu17Leg1_1718,
    bins = binnings["Mu17_1718"],
    systemtaics = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "tagIso0p3", "expr": expr_18UL.replace("0.2*tag_pt", "0.3*tag_pt")+" && "+TopHNT},
         {"title": "tagIso0p1", "expr": expr_18UL.replace("0.2*tag_pt", "0.1*tag_pt")+" && "+TopHNT}],
        [{"title": "massbinmore", "hist_nbins": 296},
         {"title": "massbinless", "hist_nbins": 74}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}]
    ],
)

## Mu8
configLeg2 = tnpConfig(
    data = samples["data2016a"],
    sim = samples["mi2016a"],
    sim_weight = "genWeight",
    sim_maxweight = 1e5,
    sim_genmatching = "tag_isMatchedGen && probe_isMatchedGen",
    sim_genmass = "genMass",
    tree = "muon/Events",
    mass = "pair_mass",
    bins = binnings['Mu8'],
    expr = expr_16UL+" && "+TopHNT,
    test = Mu8Leg2_16,
    hist_nbins = 148,
    hist_range = (53, 127),
    method = "fit",
    fit_parameter = fit_nominal,
    fit_range = (60, 120),
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "tagIso0p3", "expr": expr_16UL.replace("0.2*tag_pt", "0.3*tag_pt")},
         {"title": "tagIso0p1", "expr": expr_16UL.replace("0.2*tag_pt", "0.1*tag_pt")}],
        [{"title": "massbinmore", "hist_nbins": 296},
         {"title": "massbinless", "hist_nbins": 74}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}]
    ],
)

Configs["NUM_Mu8Leg2_DEN_TopHNT_2016a"] = configLeg2.clone()
Configs["NUM_Mu8Leg2_DEN_TopHNT_2016b"] = configLeg2.clone(
    data = samples["data2016b"],
    sim = samples["mi2016b"]
)
Configs["NUM_Mu8Leg2_DEN_TopHNT_2017"] = configLeg2.clone(
    data = samples["data2017"],
    sim = samples["mg2017"],
    expr = expr_17UL+" && "+TopHNT,
    test = Mu8Leg2_1718,
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "tagIso0p3", "expr": expr_17UL.replace("0.2*tag_pt", "0.3*tag_pt")+" && "+TopHNT},
         {"title": "tagIso0p1", "expr": expr_17UL.replace("0.2*tag_pt", "0.1*tag_pt")+" && "+TopHNT}],
        [{"title": "massbinmore", "hist_nbins": 296},
         {"title": "massbinless", "hist_nbins": 74}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}]
    ]
)
Configs["NUM_Mu8Leg2_DEN_TopHNT_2018"] = configLeg2.clone(
    data = samples["data2018"],
    sim = samples["mi2018"],
    expr = expr_18UL+" && "+TopHNT,
    test = Mu8Leg2_1718,
    systemtaics = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "tagIso0p3", "expr": expr_18UL.replace("0.2*tag_pt", "0.3*tag_pt")+" && "+TopHNT},
         {"title": "tagIso0p1", "expr": expr_18UL.replace("0.2*tag_pt", "0.1*tag_pt")+" && "+TopHNT}],
        [{"title": "massbinmore", "hist_nbins": 296},
         {"title": "massbinless", "hist_nbins": 74}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}]
    ],
)


if __name__ == "__main__":
    for key in sorted(Configs.keys()):
        print key

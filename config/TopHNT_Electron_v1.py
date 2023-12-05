from tnpConfig import tnpConfig

#### samples
samples={
    'data2016a': '/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2016preVFP/data/SingleElectron',
    'mg2016a': '/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2016preVFP/mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'amc2016a': '/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2016preVFP/mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
    'mi2016a': '/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2016preVFP/mc/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'data2016b': '/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2016postVFP/data/SingleElectron',
    'mg2016b': '/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2016postVFP/mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'amc2016b': '/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2016postVFP/mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
    'mi2016b': '/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2016postVFP/mc/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'data2017': '/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2017/data/SingleElectron',
    'mg2017': '/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2017/mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'amc2017': '/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2017/mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
    'mi2017': '/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2017/mc/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'data2018': '/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2018/data/EGamma',
    'mg2018': '/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2018/mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'amc2018': '/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2018/mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
    'mi2018': '/gv0/Users/jbhyun/TagAndProbe/Electron/2022-10-28/UL2018/mc/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos'
}

#### binning
binnings = {
    "ID": [
        {"var": "el_sc_eta",
         "type": "float",
         "bins": [-2.5, -2., -1.566, -1.4442, -0.8, 0., 0.8, 1.4442, 1.566, 2., 2.5],
         "title": "#eta_{SC}"},
        {"var": "el_pt",
         "type": "float",
         "bins": [10., 15., 20., 25., 30., 35., 50., 70., 100., 200., 500.],
         "title": "p_{T} [GeV]"}
    ],
    "Ele23": [
        {"var": "el_sc_eta",
         "type": "float",
         "bins": [-2.5, -2., -1.566, -1.4442, -0.8, 0., 0.8, 1.4442, 1.566, 2., 2.5],
         "title": "#eta_{SC}"},
        {"var": "el_pt",
         "type": "float",
         "bins": [10., 19., 21., 23., 25., 30., 35., 50., 70., 100., 200.],
         "title": "p_{T} [GeV]"}
    ],
    "Ele12": [
        {"var": "el_sc_eta",
         "type": "float",
         "bins": [-2.5, -2., -1.566, -1.4442, -0.8, 0., 0.8, 1.4442, 1.566, 2., 2.5],
         "title": "#eta_{SC}"},
        {"var": "el_pt",
         "type": "float",
         "bins": [10., 12., 15., 20., 25., 30., 35., 50., 70., 100., 200.],
         "title": "p_{T} [GeV]"}
    ]
}

#### fit parameters
fit_nominal = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.4,0.4,4.0])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.05,0.05,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x, aCMSP[50.,40.,80.],bCMSP[0.1, 0.01,0.25],cCMSP[0.05, 0.0001,0.2],peakCMSP[90.0])",
    "RooCMSShape::bkgFail(x, aCMSF[50.,30.,100.],bCMSF[0.1, 0.01,0.5],cCMSF[0.05, 0.0001,0.4],peakCMSF[90.0])",
]

fit_altsig = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "RooCBShape::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[1,0.4,10.0],alphaP[2.0,1.2,3.5],nP[3,-5,5])",
    "RooCBShape::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[1,0.3,10.0],alphaF[2.0,1.2,3.5],nF[3,-5,5])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    #"sigFracF[0.5, 0., 1.]",
    #"Gaussian::sigGaussFail(x,meanGF[80.,70.,100.],sigmaGF[15,5.,125.])",
    "RooCMSShape::bkgPass(x, aCMSP[60., 50.,100.],bCMSP[0.03, 0.01,0.5],cCMSP[0.03, -0.1,1.0],peakCMSP[90.0])",
    "RooCMSShape::bkgFail(x, aCMSF[60., 50.,100.],bCMSF[0.03, 0.01,0.5],cCMSF[0.03, -0.1,1.0],peakCMSF[90.0])",
]

fit_altbkg = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
    "Exponential::bkgFail(x, alphaF[0.,-5.,5.])",
]


#### definition
VetoGapTag = "(abs(tag_sc_eta)<1.444 || abs(tag_sc_eta)>1.566)"
MTCutTag = 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
TagCut30 = "(tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0 && (el_pt > 20 || (tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45)) && " + VetoGapTag + ")"
TagCut35 = "(tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0 && (el_pt > 20 || (tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45)) && " + VetoGapTag + ")"
TagCut40 = "(tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0 && (el_pt > 20 || (tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45)) && " + VetoGapTag + ")"
HLTSafeEl = '( (abs(el_sc_eta) < 1.479 && el_5x5_sieie < 0.013 && abs(el_dEtaSeed) < 0.01 && abs(el_dPhiIn) < 0.07 && el_hoe < 0.13 && (el_ecalIso-event_rho*0.16544 < 0.5*el_pt) && (el_hcalIso-event_rho*0.05956 < 0.3*el_pt) && el_dr03TkSumPt < 0.2*el_pt) || (abs(el_sc_eta) > 1.479 && el_5x5_sieie < 0.035 && abs(el_dEtaSeed) < 0.015 && abs(el_dPhiIn) < 0.1 && el_hoe < 0.13 && (el_ecalIso-event_rho*0.13212 < 0.5*el_pt) && (el_hcalIso-event_rho*0.13052 < 0.3*el_pt) && el_dr03TkSumPt < 0.2*el_pt) )'
TopHNT = '(passingMVA94Xwp90noisoV2 && el_miniIsoAll_fall17 < 0.1*el_pt && el_sip<4 && abs(el_dz)<0.1 && el_mHits<2 && el_hasMatchedConversion == 0 && '+HLTSafeEl+' )'
HLTEl23 = 'passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match && el_l1et > L1ThesholdHLTEle23Ele12CaloIdLTrackIdLIsoVL'
HLTEl23v2 = 'passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match'
HLTEl12 = 'passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2'

#### configs
Configs = {}
config = tnpConfig(
    data = samples["data2016a"],
    sim = samples["mi2016a"],
    sim_weight = "totWeight",
    sim_maxweight = 1e5,
    sim_genmatching = "mcTrue",
    sim_genmass = "mcMass",
    tree = "tnpEleIDs/fitter_tree",
    mass = "pair_mass",
    bins = binnings['ID'],
    expr = TagCut30,
    test = TopHNT,
    hist_nbins = 70,
    hist_range = (55, 125),
    method = "fit",
    fit_parameter = fit_nominal,
    fit_range = (60, 120),
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        #[{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["mg2016a"]}],
        [{"title": "altTag", "expr": TagCut35}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}],
    ],
)
Configs["TopHNT_2016a"] = config.clone()
Configs["TopHNT_2016b"] = config.clone(
    data = samples["data2016b"],
    sim = samples["mi2016b"],
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        #[{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["mg2016b"]}],
        [{"title": "altTag", "expr": TagCut35}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}],
    ],
)
Configs["TopHNT_2017"] = config.clone(
    data = samples["data2017"],
    sim = samples["mi2017"],
    expr = TagCut35,
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        #[{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["mg2017"]}],
        [{"title": "altTag", "expr": TagCut40}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}],
    ],
)
Configs["TopHNT_2018"] = config.clone(
    data = samples["data2018"],
    sim = samples["mi2018"],
    expr = TagCut35,
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        #[{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["mg2018"]}],
        [{"title": "altTag", "expr": TagCut40}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}],
    ],
)

#### Trigger
config_HLT = tnpConfig(
    data = samples["data2016a"],
    sim = samples["mi2016a"],
    sim_weight = "totWeight",
    sim_maxweight = 1e5,
    sim_genmatching = "mcTrue",
    sim_genmass = "mcMass",
    tree = "tnpEleTrig/fitter_tree",
    mass = "pair_mass",
    bins = binnings['Ele23'],
    expr = TagCut30+" && "+TopHNT,
    test = HLTEl23,
    hist_nbins = 70,
    hist_range = (55, 125),
    method = "fit",
    fit_parameter = fit_nominal,
    fit_range = (60, 120),
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        #[{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["mg2016a"]}],
        [{"title": "altTag", "expr": TagCut35+" && "+TopHNT}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}],
    ],
)
Configs["HLTEl23_2016a"] = config_HLT.clone()
Configs["HLTEl23_2016b"] = config_HLT.clone(
    data = samples["data2016b"],
    sim = samples["mi2016b"],
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        #[{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["mg2016b"]}],
        [{"title": "altTag", "expr": TagCut35+" && "+TopHNT}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}],
    ],
)
Configs["HLTEl23_2017"] = config_HLT.clone(
    data = samples["data2017"],
    sim = samples["mi2017"],
    expr = TagCut35+" && "+TopHNT,
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        #[{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["mg2017"]}],
        [{"title": "altTag", "expr": TagCut40+" && "+TopHNT}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}],
    ],
)
Configs["HLTEl23_2018"] = config_HLT.clone(
    data = samples["data2018"],
    sim = samples["mi2018"],
    expr = TagCut35+" && "+TopHNT,
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        #[{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["mg2017"]}],
        [{"title": "altTag", "expr": TagCut40+" &&"+TopHNT}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}],
    ],
)
Configs["HLTEl12_2016a"] = config_HLT.clone(
    bins = binnings["Ele12"],
    test = HLTEl12
)
Configs["HLTEl12_2016b"] = config_HLT.clone(
    data = samples["data2016b"],
    sim = samples["mi2016b"],
    bins = binnings["Ele12"],
    test = HLTEl12,
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        #[{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["mg2016b"]}],
        [{"title": "altTag", "expr": TagCut35+" && "+TopHNT}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}],
    ],
)   
Configs["HLTEl12_2017"] = config_HLT.clone(
    data = samples["data2017"],
    sim = samples["mi2017"],
    bins = binnings["Ele12"],
    test = HLTEl12,
    expr = TagCut35+" && "+TopHNT,
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        #[{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["mg2017"]}],
        [{"title": "altTag", "expr": TagCut40+" && "+TopHNT}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}],
    ],
)
Configs["HLTEl12_2018"] = config_HLT.clone(
    data = samples["data2018"],
    sim = samples["mi2018"],
    bins = binnings["Ele12"],
    test = HLTEl12,
    expr = TagCut35+" && "+TopHNT,
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        #[{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["mg2017"]}],
        [{"title": "altTag", "expr": TagCut40+" &&"+TopHNT}],
        [{"title": "fitwindowup", "fit_range": (63, 123)},
         {"title": "fitwindowdown", "fit_range": (57, 117)}],
    ],
)


if __name__ == "__main__":
    for key in sorted(Configs.keys()):
        print key

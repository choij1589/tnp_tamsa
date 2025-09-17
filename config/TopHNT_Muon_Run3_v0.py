from tnpConfig import tnpConfig

#### samples
#samples = {
#    "data2023": "/gv0/Users/choij/MuonTnP/merged_files/TnP_Z_Run2023C.root",
#    "amc2023": "/gv0/Users/choij/MuonTnP/merged_files/TnP_Z_Run2023_DYto2L_amcatnlo.root",
#    "mg2023": "/gv0/Users/choij/MuonTnP/merged_files/TnP_Z_Run2023_DYto2L_4Jets.root",
#    "data2023BPix": "/gv0/Users/choij/MuonTnP/merged_files/TnP_Z_Run2023D.root",
#    "amc2023BPix": "/gv0/Users/choij/MuonTnP/merged_files/TnP_Z_Run2023_DYto2L_amcatnlo_BPix.root",
#    "mg2023BPix": "/gv0/Users/choij/MuonTnP/merged_files/TnP_Z_Run2023_DYto2L_4Jets_BPix.root",
#}
samples = {
    "data2022": "/gv0/Users/choij/MuonTnP/MuonTnPProducer/2022/Muon.root",
    "mg2022": "/gv0/Users/choij/MuonTnP/MuonTnPProducer/2022/DYJets_MG.root",
    "amc2022": "/gv0/Users/choij/MuonTnP/MuonTnPProducer/2022/DYJets.root",
    "data2022EE": "/gv0/Users/choij/MuonTnP/MuonTnPProducer/2022EE/Muon.root",
    "mg2022EE": "/gv0/Users/choij/MuonTnP/MuonTnPProducer/2022EE/DYJets_MG.root",
    "amc2022EE": "/gv0/Users/choij/MuonTnP/MuonTnPProducer/2022EE/DYJets.root",
    "data2023": "/gv0/Users/choij/MuonTnP/MuonTnPProducer/2023/Muon.root",
    "mg2023": "/gv0/Users/choij/MuonTnP/MuonTnPProducer/2023/DYJets_MG.root",
    "amc2023": "/gv0/Users/choij/MuonTnP/MuonTnPProducer/2023/DYJets.root",
    "data2023BPix": "/gv0/Users/choij/MuonTnP/MuonTnPProducer/2023BPix/Muon.root",
    "mg2023BPix": "/gv0/Users/choij/MuonTnP/MuonTnPProducer/2023BPix/DYJets_MG.root",
    "amc2023BPix": "/gv0/Users/choij/MuonTnP/MuonTnPProducer/2023BPix/DYJets.root",
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
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[1.0,0.1,4.0])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[1.4,0.1,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x, aCMSP[60.,40.,80.],bCMSP[0.1,0.01,0.25],cCMSP[0.05, -0.1,0.2],peakCMSP[90.0])",
    "RooCMSShape::bkgFail(x, aCMSF[60.,50.,90.],bCMSF[0.1,0.01,0.25],cCMSF[0.05, -0.1,0.2],peakCMSF[90.0])",
]

fit_altsig = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "RooCBShape::sigResPass(x,meanP[0.0,-5.0,5.0],sigmaP[1.0,0.1,4.0],alphaP[2.0,0.0,3.5],nP[3,-5,5])",
    "RooCBShape::sigResFail(x,meanF[0.0,-5.0,5.0],sigmaF[1.4,0.1,4.0],alphaF[2.0,0.0,3.5],nF[3,-5,5])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x, aCMSP[60.,40.,80.],bCMSP[0.1, 0.01,0.25],cCMSP[0.05, -0.1,0.2],peakCMSP[90.0])",
    "RooCMSShape::bkgFail(x, aCMSF[60.,50.,90.],bCMSF[0.1, 0.01,0.25],cCMSF[0.05, -0.1,0.2],peakCMSF[90.0])",
]

fit_altbkg = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[1.0,0.1,4.0])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[1.4,0.1,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Exponential::bkgPass(x, alphaP[0.,-3.,3.])",
    "Exponential::bkgFail(x, alphaF[0.,-3.,3.])"
]

#### definition
expr = ("(probe_isTracker"
        "&& abs(probe_dxy) < 0.2 && abs(probe_dz) < 0.5"
        "&& abs(tag_dxy) < 0.2 && abs(tag_dz) < 0.5"
        "&& tag_isTight"
        "&& tag_pt > 26."
        "&& tag_IsoMu24 == 1"
        "&& pair_probeMultiplicity == 1"
        "&& tag_pfRelIso04 < 0.2)")

expr_trig = ("(tag_IsoMu24 == 1"
             "&& tag_isTight"
             "&& tag_pt > 26."
             "&& abs(tag_eta) < 2.4"
             "&& pair_probeMultiplicity == 1)")

## ID
TopHNT = ("(probe_isMedium && abs(probe_dz) < 0.1"
          "&& abs(probe_sip3d) < 3."
          "&& probe_tkRelIso < 0.4"
          "&& probe_miniPFRelIso < 0.1)")

## triggers
## DiMuon Filter name changed during Run2022E (22EE)
## It's only the naming change, no overlapping between the two
DLT_Mu17Leg = "(probe_Mu17Leg1)"
DLT_Mu8Leg = "(probe_Mu8Leg2)"

#### configs
## ID
Configs = {}
config = tnpConfig(
    data = samples["data2023"],
    sim = samples["mg2023"],
    sim_weight = "genWeight",
    sim_maxweight = 1e5,
    sim_genmatching = "tag_gen_matched && probe_gen_matched",
    sim_genmass = "pair_gen_mass",
    tree = "muon/Events",
    mass = "pair_mass",
    bins = binnings['ID'],
    expr = expr,
    test = TopHNT,
    hist_nbins = 100,
    hist_range = (65, 115),
    method = "fit",
    fit_parameter = fit_nominal,
    fit_range = (70, 110),
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["amc2023"]}],
        [{"title": "tagIso0p3", "expr": expr.replace("tag_pfRelIso04 < 0.2", "tag_pfRelIso04 < 0.3")},
         {"title": "tagIso0p1", "expr": expr.replace("tag_pfRelIso04 < 0.2", "tag_pfRelIso04 < 0.1")}],
        [{"title": "massbinmore", "hist_nbins": 200},
         {"title": "massbinless", "hist_nbins": 50}],
        [{"title": "fitwindowup", "fit_range": (63, 113)},
         {"title": "fitwindowdown", "fit_range": (67, 117)}]
    ]
)

Configs["NUM_TopHNT_DEN_TrackerMuons_2023"] = config.clone()
Configs["NUM_TopHNT_DEN_TrackerMuons_2023BPix"] = config.clone(
    data = samples["data2023BPix"],
    sim = samples["mg2023BPix"],
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["amc2023BPix"]}],
        [{"title": "tagIso0p3", "expr": expr.replace("tag_pfRelIso04 < 0.2", "tag_pfRelIso04 < 0.3")},
         {"title": "tagIso0p1", "expr": expr.replace("tag_pfRelIso04 < 0.2", "tag_pfRelIso04 < 0.1")}],
        [{"title": "massbinmore", "hist_nbins": 200},
         {"title": "massbinless", "hist_nbins": 50}],
        [{"title": "fitwindowup", "fit_range": (63, 113)},
         {"title": "fitwindowdown", "fit_range": (67, 117)}]
    ]
)

Configs["NUM_TopHNT_DEN_TrackerMuons_2022"] = config.clone(
    data = samples["data2022"],
    sim = samples["mg2022"],
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["amc2022"]}],
        [{"title": "tagIso0p3", "expr": expr.replace("tag_pfRelIso04 < 0.2", "tag_pfRelIso04 < 0.3")},
         {"title": "tagIso0p1", "expr": expr.replace("tag_pfRelIso04 < 0.2", "tag_pfRelIso04 < 0.1")}],
        [{"title": "massbinmore", "hist_nbins": 200},
         {"title": "massbinless", "hist_nbins": 50}],
        [{"title": "fitwindowup", "fit_range": (63, 113)},
         {"title": "fitwindowdown", "fit_range": (67, 117)}]
    ]
)

Configs["NUM_TopHNT_DEN_TrackerMuons_2022EE"] = config.clone(
    data = samples["data2022EE"],
    sim = samples["mg2022EE"],
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["amc2022EE"]}],
        [{"title": "tagIso0p3", "expr": expr.replace("tag_pfRelIso04 < 0.2", "tag_pfRelIso04 < 0.3")},
         {"title": "tagIso0p1", "expr": expr.replace("tag_pfRelIso04 < 0.2", "tag_pfRelIso04 < 0.1")}],
        [{"title": "massbinmore", "hist_nbins": 200},
         {"title": "massbinless", "hist_nbins": 50}],
        [{"title": "fitwindowup", "fit_range": (63, 113)},
         {"title": "fitwindowdown", "fit_range": (67, 117)}]
    ]
)

config_DLT_17Leg = tnpConfig(
    data = samples["data2023"],
    sim = samples["mg2023"],
    sim_weight = "genWeight",
    sim_maxweight = 1e5,
    sim_genmatching = "tag_gen_matched && probe_gen_matched",
    sim_genmass = "pair_gen_mass",
    tree = "muon/Events",
    mass = "pair_mass",
    bins = binnings['Mu17'],
    expr = expr+" && "+TopHNT,
    test = DLT_Mu17Leg,
    hist_nbins = 100,
    hist_range = (65, 115),
    method = "fit",
    fit_parameter = fit_nominal,
    fit_range = (70, 110),
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["amc2023"]}],
        [{"title": "tagIso0p3", "expr": expr.replace("0.2*tag_pt", "0.3*tag_pt")+" && "+TopHNT},
         {"title": "tagIso0p1", "expr": expr.replace("0.2*tag_pt", "0.1*tag_pt")+" && "+TopHNT}],
        [{"title": "massbinmore", "hist_nbins": 200},
         {"title": "massbinless", "hist_nbins": 50}],
        [{"title": "fitwindowup", "fit_range": (63, 113)},
         {"title": "fitwindowdown", "fit_range": (67, 117)}]
    ]
)

Configs["NUM_DLT_Mu17Leg_DEN_TopHNT_2023"] = config_DLT_17Leg.clone()
Configs["NUM_DLT_Mu17Leg_DEN_TopHNT_2023BPix"] = config_DLT_17Leg.clone(
    data = samples["data2023BPix"],
    sim = samples["mg2023BPix"],
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["amc2023BPix"]}],
        [{"title": "tagIso0p3", "expr": expr.replace("0.2*tag_pt", "0.3*tag_pt")+" && "+TopHNT},
         {"title": "tagIso0p1", "expr": expr.replace("0.2*tag_pt", "0.1*tag_pt")+" && "+TopHNT}],
        [{"title": "massbinmore", "hist_nbins": 200},
         {"title": "massbinless", "hist_nbins": 50}],
        [{"title": "fitwindowup", "fit_range": (63, 113)},
         {"title": "fitwindowdown", "fit_range": (67, 117)}]
    ]
)
Configs["NUM_DLT_Mu17Leg_DEN_TopHNT_2022"] = config_DLT_17Leg.clone(
    data = samples["data2022"],
    sim = samples["mg2022"],
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["amc2022"]}],
        [{"title": "tagIso0p3", "expr": expr.replace("0.2*tag_pt", "0.3*tag_pt")+" && "+TopHNT},
         {"title": "tagIso0p1", "expr": expr.replace("0.2*tag_pt", "0.1*tag_pt")+" && "+TopHNT}],
        [{"title": "massbinmore", "hist_nbins": 200},
         {"title": "massbinless", "hist_nbins": 50}],
        [{"title": "fitwindowup", "fit_range": (63, 113)},
         {"title": "fitwindowdown", "fit_range": (67, 117)}]
    ]
)
Configs["NUM_DLT_Mu17Leg_DEN_TopHNT_2022EE"] = config_DLT_17Leg.clone(
    data = samples["data2022EE"],
    sim = samples["mg2022EE"],
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["amc2022EE"]}],
        [{"title": "tagIso0p3", "expr": expr.replace("0.2*tag_pt", "0.3*tag_pt")+" && "+TopHNT},
         {"title": "tagIso0p1", "expr": expr.replace("0.2*tag_pt", "0.1*tag_pt")+" && "+TopHNT}],
        [{"title": "massbinmore", "hist_nbins": 200},
         {"title": "massbinless", "hist_nbins": 50}],
        [{"title": "fitwindowup", "fit_range": (63, 113)},
         {"title": "fitwindowdown", "fit_range": (67, 117)}]
    ]
)

config_DLT_8Leg = tnpConfig(
    data = samples["data2023"],
    sim = samples["mg2023"],
    sim_weight = "genWeight",
    sim_maxweight = 1e5,
    sim_genmatching = "tag_gen_matched && probe_gen_matched",
    sim_genmass = "pair_gen_mass",
    tree = "muon/Events",
    mass = "pair_mass",
    bins = binnings['Mu8'],
    expr = expr+" && "+ TopHNT,
    test = DLT_Mu8Leg,
    hist_nbins = 100,
    hist_range = (65, 115),
    method = "fit",
    fit_parameter = fit_nominal,
    fit_range = (70, 110),
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["amc2023"]}],
        [{"title": "tagIso0p3", "expr": expr.replace("0.2*tag_pt", "0.3*tag_pt")+" && "+TopHNT},
         {"title": "tagIso0p1", "expr": expr.replace("0.2*tag_pt", "0.1*tag_pt")+" && "+TopHNT}],
        [{"title": "massbinmore", "hist_nbins": 200},
         {"title": "massbinless", "hist_nbins": 50}],
        [{"title": "fitwindowup", "fit_range": (63, 113)},
         {"title": "fitwindowdown", "fit_range": (67, 117)}]
    ]
)

Configs["NUM_DLT_Mu8Leg_DEN_TopHNT_2023"] = config_DLT_8Leg.clone()
Configs["NUM_DLT_Mu8Leg_DEN_TopHNT_2023BPix"] = config_DLT_8Leg.clone(
    data = samples["data2023BPix"],
    sim = samples["mg2023BPix"],
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["amc2023BPix"]}],
        [{"title": "tagIso0p3", "expr": expr.replace("0.2*tag_pt", "0.3*tag_pt")+" && "+TopHNT},
         {"title": "tagIso0p1", "expr": expr.replace("0.2*tag_pt", "0.1*tag_pt")+" && "+TopHNT}],
        [{"title": "massbinmore", "hist_nbins": 200},
         {"title": "massbinless", "hist_nbins": 50}],
        [{"title": "fitwindowup", "fit_range": (63, 113)},
         {"title": "fitwindowdown", "fit_range": (67, 117)}]
    ]
)
Configs["NUM_DLT_Mu8Leg_DEN_TopHNT_2022"] = config_DLT_8Leg.clone(
    data = samples["data2022"],
    sim = samples["mg2022"],
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["amc2022"]}],
        [{"title": "tagIso0p3", "expr": expr.replace("0.2*tag_pt", "0.3*tag_pt")+" && "+TopHNT},
         {"title": "tagIso0p1", "expr": expr.replace("0.2*tag_pt", "0.1*tag_pt")+" && "+TopHNT}],
        [{"title": "massbinmore", "hist_nbins": 200},
         {"title": "massbinless", "hist_nbins": 50}],
        [{"title": "fitwindowup", "fit_range": (63, 113)},
         {"title": "fitwindowdown", "fit_range": (67, 117)}]
    ]
)
Configs["NUM_DLT_Mu8Leg_DEN_TopHNT_2022EE"] = config_DLT_8Leg.clone(
    data = samples["data2022EE"],
    sim = samples["mg2022EE"],
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["amc2022EE"]}],
        [{"title": "tagIso0p3", "expr": expr.replace("0.2*tag_pt", "0.3*tag_pt")+" && "+TopHNT},
         {"title": "tagIso0p1", "expr": expr.replace("0.2*tag_pt", "0.1*tag_pt")+" && "+TopHNT}],
        [{"title": "massbinmore", "hist_nbins": 200},
         {"title": "massbinless", "hist_nbins": 50}],
        [{"title": "fitwindowup", "fit_range": (63, 113)},
         {"title": "fitwindowdown", "fit_range": (67, 117)}]
    ]
)

if __name__ == "__main__":
    for key in sorted(Configs.keys()):
        print(key)

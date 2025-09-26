from tnpConfig import tnpConfig

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
        {"var": "probe_pt", "type": "float", "bins": [15, 20, 25, 30, 40, 50, 60, 120, 200], "title": "p_{T} [GeV]"}
    ],
    "ID_23": [
        {"var": "probe_eta", "type": "float", "bins": [-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4], "title": "#eta"},
        {"var": "probe_pt", "type": "float", "bins": [15, 20, 25, 30, 40, 50, 60, 120, 200], "title": "p_{T} [GeV]"}
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
    "RooCMSShape::bkgFail(x, aCMSF[60.,40.,100.],bCMSF[0.1,0.01,0.25],cCMSF[0.05, -0.1,0.2],peakCMSF[90.0])",
]

fit_altsig = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "RooCBShape::sigResPass(x,meanP[0.0,-5.0,5.0],sigmaP[1.0,0.1,4.0],alphaP[2.0,0.0,3.5],nP[3,-5,5])",
    "RooCBShape::sigResFail(x,meanF[0.0,-5.0,5.0],sigmaF[1.4,0.1,4.0],alphaF[2.0,0.0,3.5],nF[3,-5,5])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x, aCMSP[60.,40.,80.],bCMSP[0.1, 0.01,0.25],cCMSP[0.05, -0.1,0.2],peakCMSP[90.0])",
    "RooCMSShape::bkgFail(x, aCMSF[60.,50.,80.],bCMSF[0.1, 0.01,0.25],cCMSF[0.05, -0.1,0.2],peakCMSF[90.0])",
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

## ID
POGMedium = "probe_isMedium"

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
    bins = binnings['ID_23'],
    expr = expr,
    test = POGMedium,
    hist_nbins = 100,
    hist_range = (65, 115),
    method = "fit",
    fit_parameter = fit_nominal,
    fit_range = (70, 110),
    systematic = []
)

Configs["NUM_POGMedium_DEN_TrackerMuons_2023"] = config.clone()
Configs["NUM_POGMedium_DEN_TrackerMuons_2023BPix"] = config.clone(
    data = samples["data2023BPix"],
    sim = samples["mg2023BPix"],
)

Configs["NUM_POGMedium_DEN_TrackerMuons_2022"] = config.clone(
    data = samples["data2022"],
    sim = samples["mg2022"],
    bins = binnings['ID']
)

Configs["NUM_POGMedium_DEN_TrackerMuons_2022EE"] = config.clone(
    data = samples["data2022EE"],
    sim = samples["mg2022EE"],
    bins = binnings['ID']
)

if __name__ == "__main__":
    for key in sorted(Configs.keys()):
        print(key)

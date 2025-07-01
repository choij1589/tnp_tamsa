from tnpConfig import tnpConfig

#### samples
samples={
    "data2022": "/gv0/Users/choij/EgammaTnP/POG/2022/merged_Run2022_BCD_ReReco_updated.root",
    "mg2022": "/gv0/Users/choij/EgammaTnP/POG/2022/mc/merged_DYJetsToLL_M_50_Run3Summer22MiniAODv4-forPOG_130X_mcRun3_2022_realistic_v5-v2.root",
    "amc2022": "/gv0/Users/choij/EgammaTnP/POG/2022/mc/merged_Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2.root",
    "data2022EE": "/gv0/Users/choij/EgammaTnP/POG/2022EE/merged_Run2022_EReReco_FG_PromptReco_updated.root",
    "mg2022EE": "/gv0/Users/choij/EgammaTnP/POG/2022EE/mc/merged_DYJetsToLLL_M_50_Ru_M_50_Run3Summer22EEMiniAODv4-forPOG_130X_mcRun3_2022_realistic_postEE_v6-v2.root",
    "amc2022EE": "/gv0/Users/choij/EgammaTnP/POG/2022EE/mc/merged_Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2.root",
    "data2023": "/gv0/Users/choij/EgammaTnP/POG/2023/data_2023C.root",
    "mg2023": "/gv0/Users/choij/EgammaTnP/POG/2023/mc/DY_LO_2023preBPIX.root",
    "amc2023": "/gv0/Users/choij/EgammaTnP/POG/2023/mc/DY_NLO_2023preBPIX.root",
    "data2023BPix": "/gv0/Users/choij/EgammaTnP/POG/2023BPix/data_2023D.root",
    "mg2023BPix": "/gv0/Users/choij/EgammaTnP/POG/2023BPix/mc/DY_LO_2023postBPIX.root",
    "amc2023BPix": "/gv0/Users/choij/EgammaTnP/POG/2023BPix/mc/DY_NLO_2023postBPIX.root"
}

#### binning
binnings = {
    # Low pT bins [10, 20 GeV]: coarser eta binning for better statistics
    "ID_lowPt": [
        {"var": "el_sc_abseta",
         "type": "float", 
         "bins": [0., 1.0, 1.444, 1.566, 2., 2.5],
         "title": "|#eta_{SC}|"},
        {"var": "el_pt",
         "type": float,
         "bins": [10., 20.]}
    ],
    
    # Mid pT [20-75 GeV] bins: finer eta binning
    "ID_midPt": [
        {"var": "el_sc_abseta",
         "type": "float", 
         "bins": [0., 0.5, 1.0, 1.444, 1.566, 2., 2.5],
         "title": "|#eta_{SC}|"},
        {"var": "el_pt",
         "type": float,
         "bins": [20., 45., 75.]}
    ],
    
    # High pT [pT > 75 GeV] bins: finer eta binning  
    "ID_highPt": [
        {"var": "el_sc_abseta",
         "type": "float", 
         "bins": [0., 0.5, 1.0, 1.444, 1.566, 2., 2.5],
         "title": "|#eta_{SC}|"},
        {"var": "el_pt",
         "type": float,
         "bins": [75., 100., 500.]}
    ],
}

#### fit parameters
fit_nominal_lowpt = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.5,0.02,4.0])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",

    "RooBernstein::bkgPass(x,RooArgList(a0P[0.5,0.,1.],a1P[0.5,0.,1.],a2P[0.5,0.,1.]))",
    "RooBernstein::bkgFail(x,RooArgList(a0F[0.5,0.,1.],a1F[0.5,0.,1.],a2F[0.5,0.,1.]))",
]


fit_nominal_midpt = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.5,0.02,4.0])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",

    "RooCMSShape::bkgPass(x, aCMSP[70.,20.,120.],bCMSP[0.03, 0.0001,0.8],cCMSP[0.15, 0.0001,1.0],peakCMSP[90.0])",
    "RooCMSShape::bkgFail(x, aCMSF[70.,20.,120.],bCMSF[0.03, 0.0001,0.8],cCMSF[0.15, 0.0001,1.0],peakCMSF[90.0])",
]

fit_nominal_highpt = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.5,0.02,4.0])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",

    "Chebychev::bkgPass(x, {p0P[-0.2,-1.,1.],p1P[-0.2,-1.,1.],p2P[0.1,-1.,1.]})",
    "Chebychev::bkgFail(x, {p0F[-0.2,-1.,1.],p1F[-0.2,-1.,1.],p2F[0.1,-1.,1.]})",
]

#### definition
# Based on the requirements from the image and patterns from other configs:
# Tag electrons are already pre-selected in TnP trees with tight ID and trigger matching
# Tag Selection: Basic kinematics - pT > 35 GeV, |η| < 2.5, opposite charge requirement
# Probe Selection: PassingReco [scEt > 5 GeV && |η| < 2.5], pT > 10GeV, |η| < 2.5  
# Additional cuts can be added later: mT < 45 GeV, isolation MVA > 0.90

# Note: Tag electrons in TnP trees are typically pre-selected with tight ID and trigger matching
# Similar to patterns seen in electron.py and other configs

expr = ("tag_Ele_pt > 35.0 && abs(tag_sc_eta) < 2.5"
        "&& sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45.0"
        "&& (el_pt > 20. || (el_pt > 10. && tag_Ele_Iso122X > 0.9 && el_trkIso/el_tk_pt < 0.1))"
        )

mg_expr = expr.replace("tag_Ele_Iso122X", "tag_Ele_IsoMVA_RunIIIWinter22")

MVANoIsoWP90 = "passingMVA122Xwp90noisoV1" 

#### config
Configs = {}
config = tnpConfig(
    data = samples["data2022"],
    sim = samples["amc2022"],
    sim_weight = "totWeight",
    sig_maxweight = 1e5,
    sim_genmatching = "mcTrue",
    sim_genmass = "mcMass",
    tree = "tnpEleIDs/fitter_tree",
    mass = "pair_mass",
    bins = binnings["ID_midPt"],
    expr = expr,
    test = MVANoIsoWP90,
    hist_nbins = 64,
    hist_range = (58, 122),
    method = "fit",
    fit_parameter = fit_nominal_midpt,
    fit_range = (60, 120),
    systematic = [
        #[{"title": "altsig", "fit_parameter": fit_altsig}],
    ],
)

Configs["POGMVANoIsoWP90_MidPT_2022"] = config.clone()
Configs["POGMVANoIsoWP90_LowPT_2022"] = Configs["POGMVANoIsoWP90_MidPT_2022"].clone(
    bins = binnings["ID_lowPt"],
    fit_parameter = fit_nominal_lowpt
)
Configs["POGMVANoIsoWP90_HighPT_2022"] = Configs["POGMVANoIsoWP90_MidPT_2022"].clone(
    bins = binnings["ID_highPt"],
    fit_parameter = fit_nominal_highpt
)

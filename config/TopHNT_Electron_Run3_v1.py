from tnpConfig import tnpConfig

#### samples
samples={
    "data2022": "/gv0/Users/choij/EgammaTnP/POG/2022/merged_Run2022CD.root",
    "mg2022": "/gv0/Users/choij/EgammaTnP/POG/2022/mc/merged_DYto2L_madgraph_preEE.root",
    "amc2022": "/gv0/Users/choij/EgammaTnP/POG/2022/mc/merged_DYto2L_amcatnlo_preEE.root",
    "data2022EE": "/gv0/Users/choij/EgammaTnP/POG/2022EE/merged_Run2022EFG.root",
    "mg2022EE": "/gv0/Users/choij/EgammaTnP/POG/2022EE/mc/merged_DYto2L_madgraph_postEE.root",
    "amc2022EE": "/gv0/Users/choij/EgammaTnP/POG/2022EE/mc/merged_DYto2L_amcatnlo_postEE.root",
    "data2023": "/gv0/Users/choij/EgammaTnP/POG/2023/data_2023C.root",
    "mg2023": "/gv0/Users/choij/EgammaTnP/POG/2023/mc/DY_LO_2023preBPIX.root",
    "amc2023": "/gv0/Users/choij/EgammaTnP/POG/2023/mc/DY_NLO_2023preBPIX.root",
    "data2023BPix": "/gv0/Users/choij/EgammaTnP/POG/2023BPix/data_2023D.root",
    "mg2023BPix": "/gv0/Users/choij/EgammaTnP/POG/2023BPix/mc/DY_LO_2023postBPIX.root",
    "amc2023BPix": "/gv0/Users/choij/EgammaTnP/POG/2023BPix/mc/DY_NLO_2023postBPIX.root"
}

#### binning
binnings = {
    "ID": [
        {"var": "el_sc_eta",
         "type": "float", 
         "bins": [-2.5, -2., -1.566, -1.444, -0.8, 0., 0.8, 1.444, 1.566, 2., 2.5],
         "title": "#eta_{SC}"},
        {"var": "el_pt",
         "type": float,
         "bins": [10., 15., 20., 35., 50., 100., 200., 500.]}
    ],
    "ID_lowPT": [
        {"var": "el_sc_abseta",
         "type": "float", 
         "bins": [0., 0.8, 1.444, 1.566, 2., 2.5],
         "title": "|#eta_{SC}|"},
        {"var": "el_pt",
         "type": float,
         "bins": [10., 20.]}
    ],
    "ID_highPT": [
        {"var": "el_sc_abseta",
         "type": "float",
         "bins": [0., 0.8, 1.444, 1.566, 2., 2.5],
         "title": "|#eta_{SC}|"},
        {"var": "el_pt",
         "type": float,
         "bins": [100., 200., 500.]}
    ]
}

#### fit parameters
fit_nominal = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[1.0,0.4,4.0])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[1.4,0.4,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x, aCMSP[50.,50.,80.],bCMSP[0.1,0.01,0.25],cCMSP[0.05,-0.1,0.2],peakCMSP[90.0])",
    "RooCMSShape::bkgFail(x, aCMSF[60.,40.,90.],bCMSF[0.1,0.1,0.5],cCMSF[0.05,-0.1,0.2],peakCMSF[90.0])"
]

fit_altsig = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "RooCBShape::sigResPass(x,meanP[0.0,-5.0,5.0],sigmaP[1.0,0.4,4.0],alphaP[2.0,0.0,3.5],nP[3,-5,5])",
    "RooCBShape::sigResFail(x,meanF[0.0,-5.0,5.0],sigmaF[1.4,0.4,4.0],alphaF[2.0,0.0,3.5],nF[3,-5,5])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x, aCMSP[50.,50.,80.],bCMSP[0.1, 0.01,0.25],cCMSP[0.05, -0.1,0.2],peakCMSP[90.0])",
    "RooCMSShape::bkgFail(x, aCMSF[50.,40.,90.],bCMSF[0.1, 0.1,0.5],cCMSF[0.05, -0.1,0.2],peakCMSF[90.0])"
]

fit_altbkg = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[1.0,0.4,4.0])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[1.4,0.4,5.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Exponential::bkgPass(x, alphaP[0.,-3.,3.])",
    "Exponential::bkgFail(x, alphaF[0.,-3.,3.])"
]

### definition
VetoGapTag = "(tag_sc_abseta<1.444 || tag_sc_abseta>1.566)"
expr = ("(tag_Ele_pt > 32.0 && tag_sc_abseta < 2.5 && el_q*tag_Ele_q < 0"
        "&& sqrt(2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45.0"
        "&& (el_pt > 20. || (el_pt > 10. && tag_Ele_Iso122X > 0.9)))"
        ) 
expr += " && "+VetoGapTag

#expr_mg = expr.replace("tag_Ele_Iso122X", "tag_Ele_IsoMVA_RunIIIWinter22")
expr_alttag = expr.replace("tag_Ele_pt > 32.0", "tag_Ele_pt > 37.0")

HLTSafeEl = ("( (el_sc_abseta < 1.479"
             "&& el_5x5_sieie < 0.013"
             "&& abs(el_dEtaSeed) < 0.01"
             "&& abs(el_dPhiIn) < 0.07"
             "&& el_hoe < 0.13"
             "&& (el_ecalIso-event_rho*0.16544 < 0.5*el_pt)"
             "&& (el_hcalIso-event_rho*0.05956 < 0.3*el_pt)"
             "&& el_dr03TkSumPt < 0.2*el_pt)"
             "|| (el_sc_abseta > 1.479"
             "&& el_5x5_sieie < 0.035"
             "&& abs(el_dEtaSeed) < 0.015"
             "&& abs(el_dPhiIn) < 0.1"
             "&& el_hoe < 0.13"
             "&& (el_ecalIso-event_rho*0.13212 < 0.5*el_pt)"
             "&& (el_hcalIso-event_rho*0.13052 < 0.3*el_pt)"
             "&& el_dr03TkSumPt < 0.2*el_pt) )")

TopHNT = ("(passingMVA122Xwp90noisoV1"
          "&& el_miniIsoAll_fall17 < 0.1*el_pt"
          "&& el_sip<4 && abs(el_dz)<0.1 && el_mHits<2" 
          "&& el_hasMatchedConversion == 0)")
TopHNT += " && "+HLTSafeEl

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
    bins = binnings["ID"],
    expr = expr,
    test = TopHNT,
    hist_nbins = 72,
    hist_range = (54, 126),
    method = "fit",
    fit_parameter = fit_nominal,
    fit_range = (60, 120),
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["mg2022"]}],
        [{"title": "altTag", "expr": expr_alttag}],
        [{"title": "fitwindowup", "fit_range": (57, 117)}, {"title": "fitwindowdown", "fit_range": (63, 113)}]
    ]
)

Configs["TopHNT_2022"] = config.clone(
    data = samples["data2022"],
    sim = samples["amc2022"],
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["mg2022"], "hist_nbins": 36}],
        [{"title": "altTag", "expr": expr_alttag}],
        [{"title": "fitwindowup", "fit_range": (57, 117)}, {"title": "fitwindowdown", "fit_range": (63, 113)}]
    ]
)

Configs["TopHNT_2022EE"] = config.clone(
    data = samples["data2022EE"],
    sim = samples["amc2022EE"],
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["mg2022EE"]}],
        [{"title": "altTag", "expr": expr_alttag}],
        [{"title": "fitwindowup", "fit_range": (57, 117)}, {"title": "fitwindowdown", "fit_range": (63, 113)}]
    ]
)
Configs["TopHNT_2023"] = config.clone(
    data = samples["data2023"],
    sim = samples["amc2023"],
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["mg2023"]}],
        [{"title": "altTag", "expr": expr_alttag}],
        [{"title": "fitwindowup", "fit_range": (57, 117)}, {"title": "fitwindowdown", "fit_range": (63, 113)}]
    ]
)
Configs["TopHNT_2023BPix"] = config.clone(
    data = samples["data2023BPix"],
    sim = samples["amc2023BPix"],
    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        [{"title": "altbkg", "fit_parameter": fit_altbkg}],
        [{"title": "altmc", "sim": samples["mg2023BPix"]}],
        [{"title": "altTag", "expr": expr_alttag}],
        [{"title": "fitwindowup", "fit_range": (57, 117)}, {"title": "fitwindowdown", "fit_range": (63, 113)}]
    ]
)

from tnpConfig import tnpConfig

#### samples
samples={
    'data2016a': '/gv0/Users/choij/EgammaTnP/POG/2016a/SingleElectron',
    'mg2016a': '/gv0/Users/choij/EgammaTnP/POG/2016a/mc',
    'data2016b': '/gv0/Users/choij/EgammaTnP/POG/2016b/SingleElectron',
    'mg2016b': '/gv0/Users/choij/EgammaTnP/POG/2016b/mc',
    'data2017': '/gv0/Users/choij/EgammaTnP/POG/2017/SingleElectron',
    'mg2017': '/gv0/Users/choij/EgammaTnP/POG/2017/mc',
    'data2018': '/gv0/Users/choij/EgammaTnP/POG/2018/ntuple_EGamma_UL2018_MINIAOD_Nm1_v1',
    'mg2018': '/gv0/Users/choij/EgammaTnP/POG/2018/ntuple_DYJetsToLL_madgraphMLM_UL2018_106X_upgrade2018_realistic_v11_L1v1-v1_Nm1_v1/mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
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
         "bins": [10., 20., 35., 50., 100., 200., 500.],
         "title": "p_{T} [GeV]"}
    ],
    "ID16b": [
        {"var": "el_sc_eta",
         "type": "float",
         "bins": [-2.5, -2., -1.566, -1.4442, -0.8, 0., 0.8, 1.4442, 1.566, 2., 2.5],
         "title": "#eta_{SC}"},
        {"var": "el_pt",
         "type": "float",
         "bins": [10., 20., 35., 50., 100., 500.],
         "title": "p_{T} [GeV]"}
    ]
}

#### fit parameters
fit_nominal = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.5,0.02,4.0])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x, aCMSP[50.,40.,80.],bCMSP[0.1, 0.01,0.25],cCMSP[0.05, 0.0001,0.2],peakCMSP[90.0])",
    "RooCMSShape::bkgFail(x, aCMSF[50.,40.,80.],bCMSF[0.1, 0.01,0.25],cCMSF[0.05, 0.0001,0.2],peakCMSF[90.0])",
    #"Fit sigPass histPass_genmatching",
    #"Fit sigFail histFail_genmatching",
    #"SetConstant meanGaussP sigmaP meanGaussF sigmaF",
    #"Gaussian::sigGaussFail(x,meanGF[80.,70.,100.],sigmaGF[15,5.,125.])",
    #"sigFracF[0.5, 0., 1.]",
    #"Fit bkgPass histPass_notgenmatching",
    #"Fit bkgFail histPass_notgenmatching",
    #"SetConstant aCMSP bCMSP cCMSP aCMSF bCMSF cCMSF"
]

fit_altsig = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanGaussP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanGaussF[0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x, aCMSP[60., 50.,80.],bCMSP[0.03, 0.01,0.05],cCMSP[0.1, -0.1,1.0],peakCMSP[90.0])",
    "RooCMSShape::bkgFail(x, aCMSF[61.5, 50.,80.],bCMSF[0.03, 0.01,0.05],cCMSF[0.03, -0.1,1.0],peakCMSF[90.0])",
]

#### definition
expr = "tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0 && (el_pt > 20 || tag_Ele_trigMVA > 0.92)"
MVANoIsoWP90 = "passingMVA94Xwp90noisoV2"
#POGCBM = "passingCutBasedMedium94XV2"
POGCBM = "passingMedium94XV2"

#### configs
Configs = {}
config = tnpConfig(
    data = samples["data2016a"],
    sim = samples["mg2016a"],
    sim_weight = "totWeight",
    sim_maxweight = 1e5,
    sim_genmatching = "mcTrue",
    sim_genmass = "mcMass",
    tree = "tnpEleIDs/fitter_tree",
    mass = "pair_mass",
    bins = binnings['ID'],
    expr = expr,
    test = MVANoIsoWP90,
    hist_nbins = 64,
    hist_range = (58, 122),
    method = "fit",
    fit_parameter = fit_nominal,
    fit_range = (60, 120),
    systematic = [
        #[{"title": "altsig", "fit_parameter": fit_altsig}],
    ],
)
Configs["POGMVANoIsoWP90_2016a"] = config.clone()
Configs["POGMVANoIsoWP90_2016b"] = config.clone(
    data = samples["data2016b"],
    sim = samples["mg2016b"],
    bins = binnings['ID16b']
)
Configs["POGMVANoIsoWP90_2017"] = config.clone(
    data = samples["data2017"],
    sim = samples["mg2017"],
)
Configs["POGMVANoIsoWP90_2018"] = config.clone(
    data = samples["data2018"],
    sim = samples["mg2018"],
)

if __name__ == "__main__":
    for key in sorted(Configs.keys()):
        print key
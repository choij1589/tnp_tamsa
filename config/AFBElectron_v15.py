from tnpConfig import tnpConfig
### RECO efficiency; better initial norm guess
############## samples ################
samples={
    'data2012':'/gv0/Users/hsseo/TnP_Run12/data',
    'powheg2012':'/gv0/Users/hsseo/TnP_Run12/S12pwgZee',

    'data2016a':'/gv0/Users/hsseo/EgammaTnP/SKFlat/Run2UltraLegacy_v3/2016preVFP/DATA_SkimTree_EgammaTnP/SingleElectron',
    'mi2016a':'/gv0/Users/hsseo/EgammaTnP/SKFlat/Run2UltraLegacy_v3/2016preVFP/MC_SkimTree_EgammaTnP/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'mg2016a':'/gv0/Users/hsseo/EgammaTnP/SKFlat/Run2UltraLegacy_v3/2016preVFP/MC_SkimTree_EgammaTnP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'data2016a_reco':'/gv0/Users/hsseo/EgammaTnP/2023-04-13/UL2016preVFP/data/SingleElectron',
    'mi2016a_reco':'/gv0/Users/hsseo/EgammaTnP/2023-04-13/UL2016preVFP/mc_weight/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'mg2016a_reco':'/gv0/Users/hsseo/EgammaTnP/2023-04-13/UL2016preVFP/mc_weight/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',

    'data2016b':'/gv0/Users/hsseo/EgammaTnP/SKFlat/Run2UltraLegacy_v3/2016postVFP/DATA_SkimTree_EgammaTnP/SingleElectron',
    'mi2016b':'/gv0/Users/hsseo/EgammaTnP/SKFlat/Run2UltraLegacy_v3/2016postVFP/MC_SkimTree_EgammaTnP/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'mg2016b':'/gv0/Users/hsseo/EgammaTnP/SKFlat/Run2UltraLegacy_v3/2016postVFP/MC_SkimTree_EgammaTnP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'data2016b_reco':'/gv0/Users/hsseo/EgammaTnP/2023-04-13/UL2016postVFP/data/SingleElectron',
    'mi2016b_reco':'/gv0/Users/hsseo/EgammaTnP/2023-04-13/UL2016postVFP/mc_weight/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'mg2016b_reco':'/gv0/Users/hsseo/EgammaTnP/2023-04-13/UL2016postVFP/mc_weight/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',

    'data2017':'/gv0/Users/hsseo/EgammaTnP/SKFlat/Run2UltraLegacy_v3/2017/DATA_SkimTree_EgammaTnP/SingleElectron',
    'mi2017':'/gv0/Users/hsseo/EgammaTnP/SKFlat/Run2UltraLegacy_v3/2017/MC_SkimTree_EgammaTnP/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'mg2017':'/gv0/Users/hsseo/EgammaTnP/SKFlat/Run2UltraLegacy_v3/2017/MC_SkimTree_EgammaTnP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'data2017_reco':'/gv0/Users/hsseo/EgammaTnP/2023-04-13/UL2017/data/SingleElectron',
    'mi2017_reco':'/gv0/Users/hsseo/EgammaTnP/2023-04-13/UL2017/mc_weight/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'mg2017_reco':'/gv0/Users/hsseo/EgammaTnP/2023-04-13/UL2017/mc_weight/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',

    'data2018':'/gv0/Users/hsseo/EgammaTnP/SKFlat/Run2UltraLegacy_v3/2018/DATA_SkimTree_EgammaTnP/EGamma',
    'mi2018':'/gv0/Users/hsseo/EgammaTnP/SKFlat/Run2UltraLegacy_v3/2018/MC_SkimTree_EgammaTnP/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'mg2018':'/gv0/Users/hsseo/EgammaTnP/SKFlat/Run2UltraLegacy_v3/2018/MC_SkimTree_EgammaTnP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
    'data2018_reco':'/gv0/Users/hsseo/EgammaTnP/2023-04-13/UL2018/data/EGamma',
    'mi2018_reco':'/gv0/Users/hsseo/EgammaTnP/2023-04-13/UL2018/mc_weight/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'mg2018_reco':'/gv0/Users/hsseo/EgammaTnP/2023-04-13/UL2018/mc_weight/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
}
############## binning ################
bin_RECO = [
    { 'var' : 'sc_eta' , 'type': 'float', 'bins': [-2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.566, -1.4442, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4442, 1.566, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5], 'title':'#eta' },
    { 'var' : 'sc_pt' , 'type': 'float', 'bins': [20, 500], 'title':'p_{T} [GeV]' },
]
bin_ID = [
    { 'var' : 'el_eta' , 'type': 'float', 'bins': [-2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.566, -1.4442, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4442, 1.566, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5], 'title':'#eta' },
    { 'var' : 'el_pt_cor' , 'type': 'float', 'bins': [10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 100, 500], 'title':'p_{T} [GeV]' },
]
bin_Ele35 = [
    { 'var' : 'el_eta' , 'type': 'float', 'bins': [-2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.566, -1.4442, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4442, 1.566, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5], 'title':'#eta' },
    { 'var' : 'el_pt_cor' , 'type': 'float', 'bins': [10, 20, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 40, 45, 50, 60, 70, 100, 500], 'title':'p_{T} [GeV]' },
]
bin_Ele32 = [
    { 'var' : 'el_eta' , 'type': 'float', 'bins': [-2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.566, -1.4442, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4442, 1.566, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5], 'title':'#eta' },
    { 'var' : 'el_pt_cor' , 'type': 'float', 'bins': [10, 20, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 40, 45, 50, 60, 70, 100, 500], 'title':'p_{T} [GeV]' },
]
bin_Ele28 = [
    { 'var' : 'el_eta' , 'type': 'float', 'bins': [-2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.566, -1.4442, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4442, 1.566, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5], 'title':'#eta' },
    { 'var' : 'el_pt_cor' , 'type': 'float', 'bins': [10, 20, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 40, 45, 50, 60, 70, 100, 500], 'title':'p_{T} [GeV]' },
]
bin_Ele27 = [
    { 'var' : 'el_eta' , 'type': 'float', 'bins': [-2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.566, -1.4442, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4442, 1.566, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5], 'title':'#eta' },
    { 'var' : 'el_pt_cor' , 'type': 'float', 'bins': [10, 20, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 40, 45, 50, 60, 70, 100, 500], 'title':'p_{T} [GeV]' },
]
bin_Ele23 = [
    { 'var' : 'el_eta' , 'type': 'float', 'bins': [-2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.566, -1.4442, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4442, 1.566, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5], 'title':'#eta' },
    { 'var' : 'el_pt_cor' , 'type': 'float', 'bins': [10, 19, 23, 25, 27, 30, 35, 40, 45, 50, 60, 70, 100, 500], 'title':'p_{T} [GeV]' },
]
bin_Ele12 = [
    { 'var' : 'el_eta' , 'type': 'float', 'bins': [-2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.566, -1.4442, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4442, 1.566, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5], 'title':'#eta' },
    { 'var' : 'el_pt_cor' , 'type': 'float', 'bins': [10, 12, 15, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 100, 500], 'title':'p_{T} [GeV]' },
]

bin2012_ID = [
    { 'var' : 'probe_eta' , 'type': 'float', 'bins': [-2.5, -2.1, -1.80, -1.566, -1.4442, -1.1, -0.8, -0.4, 0.0, 0.4, 0.8, 1.1, 1.4442, 1.566, 1.80, 2.1, 2.5], 'title':'#eta' },
    { 'var' : 'probe_pt' , 'type': 'float', 'bins': [10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 100, 500], 'title':'p_{T} [GeV]' },
]
bin2012_Ele35 = [
    { 'var' : 'probe_eta' , 'type': 'float', 'bins': [-2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.566, -1.4442, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4442, 1.566, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5], 'title':'#eta' },
    { 'var' : 'probe_pt' , 'type': 'float', 'bins': [10, 20, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 40, 45, 50, 60, 70, 100, 500], 'title':'p_{T} [GeV]' },
]
bin2012_Ele32 = [
    { 'var' : 'probe_eta' , 'type': 'float', 'bins': [-2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.566, -1.4442, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4442, 1.566, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5], 'title':'#eta' },
    { 'var' : 'probe_pt' , 'type': 'float', 'bins': [10, 20, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 40, 45, 50, 60, 70, 100, 500], 'title':'p_{T} [GeV]' },
]
bin2012_Ele28 = [
    { 'var' : 'probe_eta' , 'type': 'float', 'bins': [-2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.566, -1.4442, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4442, 1.566, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5], 'title':'#eta' },
    { 'var' : 'probe_pt' , 'type': 'float', 'bins': [10, 20, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 40, 45, 50, 60, 70, 100, 500], 'title':'p_{T} [GeV]' },
]
bin2012_Ele27 = [
    { 'var' : 'probe_eta' , 'type': 'float', 'bins': [-2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.566, -1.4442, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4442, 1.566, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5], 'title':'#eta' },
    { 'var' : 'probe_pt' , 'type': 'float', 'bins': [10, 20, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 40, 45, 50, 60, 70, 100, 500], 'title':'p_{T} [GeV]' },
]
bin2012_Ele23 = [
    { 'var' : 'probe_eta' , 'type': 'float', 'bins': [-2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.566, -1.4442, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4442, 1.566, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5], 'title':'#eta' },
    { 'var' : 'probe_pt' , 'type': 'float', 'bins': [10, 19, 23, 25, 27, 30, 35, 40, 45, 50, 60, 70, 100, 500], 'title':'p_{T} [GeV]' },
]
bin2012_Ele12 = [
    { 'var' : 'probe_eta' , 'type': 'float', 'bins': [-2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.566, -1.4442, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4442, 1.566, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5], 'title':'#eta' },
    { 'var' : 'probe_pt' , 'type': 'float', 'bins': [10, 12, 15, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 100, 500], 'title':'p_{T} [GeV]' },
]


############### Expr ################
## selection
tight_mcTrue='mcTrue && el_et/mc_probe_et>0.9 && el_et/mc_probe_et < 1.1 && (el_eta-mc_probe_eta)*(el_eta-mc_probe_eta)+(el_phi-mc_probe_phi)*(el_phi-mc_probe_phi)<0.01'
tight_mcTrue_reco='mcTrue && sc_et/mc_probe_et>0.9 && sc_et/mc_probe_et < 1.1 && (sc_eta-mc_probe_eta)*(sc_eta-mc_probe_eta)+(sc_phi-mc_probe_phi)*(sc_phi-mc_probe_phi)<0.01'
medium_mcTrue='mcTrue && el_et/mc_probe_et>0.8 && el_et/mc_probe_et < 1.2 && (el_eta-mc_probe_eta)*(el_eta-mc_probe_eta)+(el_phi-mc_probe_phi)*(el_phi-mc_probe_phi)<0.01'
loose_mcTrue='mcTrue && el_et/mc_probe_et>0.5 && el_et/mc_probe_et < 1.5 && (el_eta-mc_probe_eta)*(el_eta-mc_probe_eta)+(el_phi-mc_probe_phi)*(el_phi-mc_probe_phi)<0.01'
loose_mcTrue_reco='mcTrue && sc_et/mc_probe_et>0.5 && sc_et/mc_probe_et < 1.5 && (sc_eta-mc_probe_eta)*(sc_eta-mc_probe_eta)+(sc_phi-mc_probe_phi)*(sc_phi-mc_probe_phi)<0.09'

## fits
fit_nominal = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x,acmsP[60.,50.,80.],betaP[0.05,0.01,0.08],gammaP[0.1, -1, 1],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[60.,50.,80.],betaF[0.05,0.01,0.08],gammaF[0.1, -1, 1],peakF[90.0])",
]

fit_altsig = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_genmass,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_genmass,2)",
    "RooCBShape::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[1,0.3,10.0],alphaP[2.0,1.2,3.5],nP[3,-5,5])",
    "RooCBShape::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[1,0.3,10.0],alphaF[2.0,1.2,3.5],nF[3,-5,5])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Fit sigPass histPass_genmatching",
    "Fit sigFail histFail_genmatching",
    "SetConstant alphaP nP alphaF nF",
    "RooCMSShape::bkgPass(x,acmsP[60.,50.,80.],betaP[0.05,0.01,0.08],gammaP[0.1, -1, 1],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[60.,50.,80.],betaF[0.05,0.01,0.08],gammaF[0.1, -1, 1],peakF[90.0])",
]

fit_altbkg = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
    "Exponential::bkgFail(x, alphaF[0.,-5.,5.])",
]

fit_altbkg_chebychev = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Chebychev::bkgPass(x, {p0P[-0.2.,-1.,1.],p1P[-0.2.,-1.,1.],p2P[0.1,-1.,1.]})",
    "Chebychev::bkgFail(x, {p0F[-0.2.,-1.,1.],p1F[-0.2.,-1.,1.],p2F[0.1,-1.,1.]})",
]

fit_nominal_random = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_random,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_random,2)",
    "Gaussian::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x,acmsP[60.,50.,80.],betaP[0.05,0.01,0.08],gammaP[0.1, -1, 1],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[60.,50.,80.],betaF[0.05,0.01,0.08],gammaF[0.1, -1, 1],peakF[90.0])",
]

fit_altsig_random = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_genmass_random,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_genmass_random,2)",
    "RooCBShape::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[1,0.3,10.0],alphaP[2.0,1.2,3.5],nP[3,-5,5])",
    "RooCBShape::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[1,0.3,10.0],alphaF[2.0,1.2,3.5],nF[3,-5,5])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Fit sigPass histPass_genmatching",
    "Fit sigFail histFail_genmatching",
    "SetConstant alphaP nP alphaF nF",
    "RooCMSShape::bkgPass(x,acmsP[60.,50.,80.],betaP[0.05,0.01,0.08],gammaP[0.1, -1, 1],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[60.,50.,80.],betaF[0.05,0.01,0.08],gammaF[0.1, -1, 1],peakF[90.0])",
]

fit_altbkg_random = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_random,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_random,2)",
    "Gaussian::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
    "Exponential::bkgFail(x, alphaF[0.,-5.,5.])",
]



########### Configs ##############
Configs={}

#### 2012
## ID
config=tnpConfig(
    data=samples['data2012'],
    sim=samples['powheg2012'],
    sim_weight='weight',
    sim_maxweight=10000.,
    sim_genmatching="gen_matching",
    sim_genmass="gen_mass",
    tree='e',
    mass="pair_mass",
    bins=bin2012_ID,
    expr='( tag_Tight && tag_Ele27 && tag_pt>30 && probe_q>0 )*(probe_q*tag_q<0?1.:-1.)',
    test='probe_Medium',
    hist_nbins=98,
    hist_range=(52,150),
    method="fit",
    fit_parameter=fit_nominal,
    fit_range=(60,140),
    count_range=None,
    systematic=[
        [{'title':'altbkg','fit_parameter':fit_altbkg}],
        [{'title':'altsig','fit_parameter':fit_altsig}],
        [{'title':'alttag','expr.replace':('tag_pt>30','tag_pt>35')}],
        [{'title':'altmc'}],
        [{'title':'altsub','expr.replace':('(probe_q*tag_q<0?1.:-1.)','(probe_q*tag_q<0?1.:-0.6)')}],
        [{'title':'nogenmatching','sim_genmatching':"(1)"}],
    ],
)
Configs['2012_MediumID_Plus']=config.clone(test='probe_Medium')
Configs['2012_SelQ_MediumID_Plus']=config.clone(
    expr='( probe_Medium && tag_Tight && tag_Ele27 && tag_pt>30 && probe_q>0 )',
    test='probe_3charge',
    method="count",
    count_range=(76,106),
)

## trigger
config=config.clone(
    expr='( probe_Medium && tag_Tight && tag_Ele27 && tag_pt>30 && probe_q>0 )',
    method="count",
    count_range=(76,106),
)
Configs['2012_Ele27_MediumID_Plus']=config.clone(
    bins=bin2012_Ele27,
    test='probe_Ele27',
    method="count",
    count_range=(76,106),
)
Configs['2012_Ele27_SelQ_MediumID_Plus']=config.clone(
    bins=bin2012_Ele27,
    expr='( probe_Medium&&probe_3charge && tag_Tight && tag_Ele27 && tag_pt>30 && probe_q>0 )',
    test='probe_Ele27',
    method="count",
    count_range=(76,106),
)

#### 2016a
## ID
config=tnpConfig(
    data=samples['data2016a'],
    sim=samples['mi2016a'],
    sim_weight='weight*PUweight*prefireweight',
    sim_maxweight=10000.,
    sim_genmatching=loose_mcTrue,
    sim_genmass="mcMass",
    tree='tnpEleIDs/fitter_tree',
    mass="pair_mass_cor",
    bins=bin_ID,
    expr='( tag_passHltEle27WPTightGsf&&tag_passingCutBasedTight94XV2 && tag_Ele_pt_cor>30 && el_q>0 )*(el_q*tag_Ele_q<0?1.:-1.)',
    test='passingCutBasedMedium94XV2',
    hist_nbins=98,
    hist_range=(52,150),
    method="fit",
    fit_parameter=fit_nominal,
    fit_range=(60,140),
    count_range=None,
    systematic=[
        [{'title':'altbkg','fit_parameter':fit_altbkg}],
        [{'title':'altsig','fit_parameter':fit_altsig}],
        [{'title':'alttag','expr.replace':('tag_Ele_pt_cor>30','tag_Ele_pt_cor>35')}],
        [{'title':'altmc','sim.replace':('DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos','DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8')}],
        [{'title':'altsub','expr.replace':('(el_q*tag_Ele_q<0?1.:-1.)','(el_q*tag_Ele_q<0?1.:-0.6)')}],
        [{'title':'nogenmatching','sim_genmatching':"(1)"}],
        [{'title':'PUweight_up','sim_weight.replace':('PUweight','PUweight_up')},{'title':'PUweight_down','sim_weight.replace':('PUweight','PUweight_down')}],
        [{'title':'prefireweight_up','sim_weight.replace':('prefireweight','prefireweight_up')},{'title':'prefireweight_down','sim_weight.replace':('prefireweight','prefireweight_down')}],
        [{'title':'zptweight','sim_weight.add':'*zptweight'}],
        [{'title':'z0weight','sim_weight.add':'*z0weight'}],
Configs['2016a_MediumID_Plus']=config.clone(test='passingCutBasedMedium94XV2',option="fix_ptbelow20")
Configs['2016a_SelQ_MediumID_Plus']=config.clone(
    expr='( passingCutBasedMedium94XV2 && tag_passHltEle27WPTightGsf&&tag_passingCutBasedTight94XV2 && tag_Ele_pt_cor>30 && el_q>0 )',
    test='el_3charge',
    method="count",
    count_range=(76,106),
)

## trigger
config=config.clone(
    tree='tnpEleTrig/fitter_tree',
    expr='( passingCutBasedMedium94XV2 && tag_passHltEle27WPTightGsf&&tag_passingCutBasedTight94XV2 && tag_Ele_pt_cor>30 && el_q>0 )',
    method="count",
    count_range=(76,106),
)
Configs['2016a_Ele23Leg1_MediumID_Plus']=config.clone(
    bins=bin_Ele23,
    test='passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1&&el_l1et>L1ThresholdHLTEle23Ele12CaloIdLTrackIdLIsoVL',
)
Configs['2016a_Ele12Leg2_MediumID_Plus']=config.clone(
    bins=bin_Ele12,
    test='passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2',
)
Configs['2016a_Ele27_MediumID_Plus']=config.clone(
    bins=bin_Ele27,
    test='passHltEle27WPTightGsf',
)
Configs['2016a_Ele27_SelQ_MediumID_Plus']=config.clone(
    bins=bin_Ele27,
    expr='( passingCutBasedMedium94XV2&&el_3charge && tag_passHltEle27WPTightGsf&&tag_passingCutBasedTight94XV2 && tag_Ele_pt_cor>30 && el_q>0 )',
    test='passHltEle27WPTightGsf',
)

#### 2016b
Configs_2016b={}
for key in Configs:
    if "2016a_" in key:
        Configs_2016b[key.replace("2016a_","2016b_")]=Configs[key].clone(data=samples["data2016b"],sim=samples["mi2016b"])
Configs.update(Configs_2016b)

#### 2017
## ID
config=config.clone(
    data=samples['data2017'],
    sim=samples['mi2017'],
    tree='tnpEleIDs/fitter_tree',
    expr='( tag_passHltEle32DoubleEGWPTightGsf&&tag_passEGL1SingleEGOr&&tag_passingCutBasedTight94XV2 && tag_Ele_pt_cor>35 && el_q>0 )*(el_q*tag_Ele_q<0?1.:-1.)',
    method="fit",
    count_range=None,
    systematic=[
        [{'title':'altbkg','fit_parameter':fit_altbkg}],
        [{'title':'altsig','fit_parameter':fit_altsig}],
        [{'title':'alttag','expr.replace':('tag_Ele_pt_cor>35','tag_Ele_pt_cor>38')}],
        [{'title':'altmc','sim.replace':('DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos','DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8')}],
        [{'title':'altsub','expr.replace':('(el_q*tag_Ele_q<0?1.:-1.)','(el_q*tag_Ele_q<0?1.:-0.6)')}],
        [{'title':'nogenmatching','sim_genmatching':"(1)"}], 
        [{'title':'PUweight_up','sim_weight.replace':('PUweight','PUweight_up')},{'title':'PUweight_down','sim_weight.replace':('PUweight','PUweight_down')}],
        [{'title':'prefireweight_up','sim_weight.replace':('prefireweight','prefireweight_up')},{'title':'prefireweight_down','sim_weight.replace':('prefireweight','prefireweight_down')}],
        [{'title':'zptweight','sim_weight.add':'*zptweight'}],
        [{'title':'z0weight','sim_weight.add':'*z0weight'}],
    ],
)
Configs['2017_MediumID_Plus']=config.clone(test='passingCutBasedMedium94XV2',option="fix_ptbelow20")
Configs['2017_SelQ_MediumID_Plus']=config.clone(
    expr='( passingCutBasedMedium94XV2 && tag_passHltEle32DoubleEGWPTightGsf&&tag_passEGL1SingleEGOr&&tag_passingCutBasedTight94XV2 && tag_Ele_pt_cor>35 && el_q>0 )',
    test='el_3charge',
    method="count",
    count_range=(76,106),
)

## trigger
config=config.clone(
    tree='tnpEleTrig/fitter_tree',
    expr='( passingCutBasedMedium94XV2 && tag_passHltEle32DoubleEGWPTightGsf&&tag_passEGL1SingleEGOr&&tag_passingCutBasedTight94XV2 && tag_Ele_pt_cor>35 && el_q>0 )',
    method="count",
    count_range=(76,106),
)
Configs['2017_Ele23Leg1_MediumID_Plus']=config.clone(
    bins=bin_Ele23,
    test='passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1&&el_l1et>L1ThresholdHLTEle23Ele12CaloIdLTrackIdLIsoVL',
)
Configs['2017_Ele12Leg2_MediumID_Plus']=config.clone(
    bins=bin_Ele12,
    test='passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2',
)
Configs['2017_Ele32DoubleEG_MediumID_Plus']=config.clone(
    bins=bin_Ele32,
    test='passHltEle32DoubleEGWPTightGsf&&passEGL1SingleEGOr',
)
Configs['2017_Ele27_MediumID_Plus']=config.clone(
    bins=bin_Ele27,
    expr='( passingCutBasedMedium94XV2 && tag_passHltEle27WPTightGsf&&tag_passingCutBasedTight94XV2 && tag_Ele_pt_cor>35 && el_q>0 )',
    test='passHltEle27WPTightGsf',
)
Configs['2017_Ele32_MediumID_Plus']=config.clone(
    bins=bin_Ele32,
    expr='( passingCutBasedMedium94XV2 && tag_passHltEle32WPTightGsf&&tag_passingCutBasedTight94XV2 && tag_Ele_pt_cor>35 && el_q>0 )',
    test='passHltEle32WPTightGsf',
)
Configs['2017_Ele32DoubleEG_SelQ_MediumID_Plus']=config.clone(
    bins=bin_Ele32,
    expr='( passingCutBasedMedium94XV2&&el_3charge && tag_passHltEle32DoubleEGWPTightGsf&&tag_passEGL1SingleEGOr&&tag_passingCutBasedTight94XV2 && tag_Ele_pt_cor>35 && el_q>0 )',
    test='passHltEle32DoubleEGWPTightGsf&&passEGL1SingleEGOr',
)
Configs['2017_Ele27_SelQ_MediumID_Plus']=config.clone(
    bins=bin_Ele27,
    expr='( passingCutBasedMedium94XV2&&el_3charge && tag_passHltEle27WPTightGsf&&tag_passingCutBasedTight94XV2 && tag_Ele_pt_cor>35 && el_q>0 )',
    test='passHltEle27WPTightGsf',
)
Configs['2017_Ele32_SelQ_MediumID_Plus']=config.clone(
    bins=bin_Ele32,
    expr='( passingCutBasedMedium94XV2&&el_3charge && tag_passHltEle32WPTightGsf&&tag_passingCutBasedTight94XV2 && tag_Ele_pt_cor>35 && el_q>0 )',
    test='passHltEle32WPTightGsf',
)

#### 2018
## ID
config=config.clone(
    data=samples['data2018'],
    sim=samples['mi2018'],
    tree='tnpEleIDs/fitter_tree',
    expr='( tag_passHltEle32WPTightGsf&&tag_passingCutBasedTight94XV2 && tag_Ele_pt_cor>35 && el_q>0 )*(el_q*tag_Ele_q<0?1.:-1.)',
    method="fit",
    count_range=None,
)
Configs['2018_MediumID_Plus']=config.clone(test='passingCutBasedMedium94XV2',option="fix_ptbelow20")
Configs['2018_SelQ_MediumID_Plus']=config.clone(
    expr='( passingCutBasedMedium94XV2 && tag_passHltEle32WPTightGsf&&tag_passingCutBasedTight94XV2 && tag_Ele_pt_cor>35 && el_q>0 )',
    test='el_3charge',
    method="count",
    count_range=(76,106),
)

## trigger
config=config.clone(
    tree='tnpEleTrig/fitter_tree',
    expr='( passingCutBasedMedium94XV2 && tag_passHltEle32WPTightGsf&&tag_passingCutBasedTight94XV2 && tag_Ele_pt_cor>35 && el_q>0 )',
    method="count",
    count_range=(76,106),
)
Configs['2018_Ele23Leg1_MediumID_Plus']=config.clone(
    bins=bin_Ele23,
    test='passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1&&el_l1et>L1ThresholdHLTEle23Ele12CaloIdLTrackIdLIsoVL',
)
Configs['2018_Ele12Leg2_MediumID_Plus']=config.clone(
    bins=bin_Ele12,
    test='passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2',
)
Configs['2018_Ele32_MediumID_Plus']=config.clone(
    bins=bin_Ele32,
    test='passHltEle32WPTightGsf',
)
Configs['2018_Ele28_MediumID_Plus']=config.clone(
    bins=bin_Ele28,
    expr='( passingCutBasedMedium94XV2 && tag_passHltEle28WPTightGsf&&tag_passingCutBasedTight94XV2 && tag_Ele_pt_cor>35 && el_q>0 )',
    test='passHltEle28WPTightGsf',
)
Configs['2018_Ele32_SelQ_MediumID_Plus']=config.clone(
    bins=bin_Ele32,
    expr='( passingCutBasedMedium94XV2&&el_3charge && tag_passHltEle32WPTightGsf&&tag_passingCutBasedTight94XV2 && tag_Ele_pt_cor>35 && el_q>0 )',
    test='passHltEle32WPTightGsf',
)
Configs['2018_Ele28_SelQ_MediumID_Plus']=config.clone(
    bins=bin_Ele28,
    expr='( passingCutBasedMedium94XV2&&el_3charge && tag_passHltEle28WPTightGsf&&tag_passingCutBasedTight94XV2 && tag_Ele_pt_cor>35 && el_q>0 )',
    test='passHltEle28WPTightGsf',
)

## RECO
Configs['2016a_RECO']=tnpConfig(
    data=samples['data2016a_reco'],
    sim=samples['mi2016a_reco'],
    sim_weight='PUweight*prefireweight',
    sim_maxweight=10000.,
    sim_genmatching=tight_mcTrue_reco,
    sim_genmass="mcMass",
    tree='tnpEleReco/fitter_tree',
    mass="pair_mass",
    bins=bin_RECO,
    expr='( tag_Ele_pt>30 )',
    test='passingRECO',
    hist_nbins=98,
    hist_range=(52,150),
    method="fit",
    fit_parameter=fit_nominal,
    fit_range=(60,140),
    count_range=None,
    systematic=[
        [{'title':'altbkg','fit_parameter':fit_altbkg_chebychev}],
        [{'title':'altsig','fit_parameter':fit_altsig}],
        [{'title':'alttag','expr.replace':('tag_Ele_pt>30','tag_Ele_pt>35')}],
        [{'title':'altmc','sim.replace':('DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos','DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8')}],
        [{'title':'altsub'}],
        [{'title':'genmatching','sim_genmatching':loose_mcTrue_reco}],
        [{'title':'PUweight_up','sim_weight.replace':('PUweight','PUweight_up')},{'title':'PUweight_down','sim_weight.replace':('PUweight','PUweight_down')}],
        [{'title':'prefireweight_up','sim_weight.replace':('prefireweight','prefireweight_up')},{'title':'prefireweight_down','sim_weight.replace':('prefireweight','prefireweight_down')}],
        [{'title':'zptweight','sim_weight.add':'*zptweight'}],
        [{'title':'z0weight','sim_weight.add':'*z0weight'}],
    ],
)
Configs['2016b_RECO']=Configs['2016a_RECO'].clone(
    data=samples['data2016b_reco'],
    sim=samples['mi2016b_reco'],
)
Configs['2017_RECO']=Configs['2016a_RECO'].clone(
    data=samples['data2017_reco'],
    sim=samples['mi2017_reco'],
    expr='( tag_Ele_pt>35 )',
    systematic=[
        [{'title':'altbkg','fit_parameter':fit_altbkg_chebychev}],
        [{'title':'altsig','fit_parameter':fit_altsig}],
        [{'title':'alttag','expr.replace':('tag_Ele_pt>35','tag_Ele_pt>38')}],
        [{'title':'altmc','sim.replace':('DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos','DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8')}],
        [{'title':'altsub'}],
        [{'title':'genmatching','sim_genmatching':loose_mcTrue_reco}],
        [{'title':'PUweight_up','sim_weight.replace':('PUweight','PUweight_up')},{'title':'PUweight_down','sim_weight.replace':('PUweight','PUweight_down')}],
        [{'title':'prefireweight_up','sim_weight.replace':('prefireweight','prefireweight_up')},{'title':'prefireweight_down','sim_weight.replace':('prefireweight','prefireweight_down')}],
        [{'title':'zptweight','sim_weight.add':'*zptweight'}],
        [{'title':'z0weight','sim_weight.add':'*z0weight'}],
    ],
)
Configs['2018_RECO']=Configs['2017_RECO'].clone(
    data=samples['data2018_reco'],
    sim=samples['mg2018_reco'],
)


#### minus
Configs_minus={}
for key in Configs:
    if "_Plus" in key:
        if "2012" in key:
            Configs_minus[key.replace("_Plus","_Minus")]=Configs[key].clone({"expr.replace":("probe_q>0","probe_q<0")})
        else:
            Configs_minus[key.replace("_Plus","_Minus")]=Configs[key].clone({"expr.replace":("el_q>0","el_q<0")})
Configs.update(Configs_minus)

#### inclusive
Configs_inclusive={}
for key in Configs:
    if "_Plus" in key:
        if "2012" in key:
            Configs_inclusive[key.replace("_Plus","")]=Configs[key].clone({"expr.replace":("&& probe_q>0","")})
        else:
            Configs_inclusive[key.replace("_Plus","")]=Configs[key].clone({"expr.replace":("&& el_q>0","")})
Configs.update(Configs_inclusive)

if __name__=="__main__":
    for key in sorted(Configs.keys()):
        print key
from tnpConfig import tnpConfig

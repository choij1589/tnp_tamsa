## quick start

```
source setup.sh
python3 tnp_tamsa.py config/AFBMuon_v15.py 2018_MediumID_LooseTrkIso
```

## Workflow
3 steps for ```tnp_tamsa.py```.
1. ```--step hist```: make pass / fail histograms for each bins.
2. ```--step fit```: Do fitting.
3. ```--step sum```: Sum up the efficiencies in all bins and make final efficiency root file.

In step 2, the fitting results might not good enough with the initial fitting configurations.
You can check the unsatisfactory fitting status by following:
```
checkFitStatus.py results/TopHNT_Electron_Run3_v0/TopHNT_2022EE
```

After updating the config file, submit the re-fit script:
```
submitRefitJobs.py config/TopHNT_Electron_Run3_v0.py TopHNT_2022EE
```

It will reduce the unnecessary fitting jobs significantly. Still you should do the fittings manually:
```
python3 tnp_tamsa.py config/TopHNT_Electron_Run3_v0.py TopHNT_2022EE --step fit --no-condor --bin 4 -s 3 -m 0
```
#!/bin/bash
ERA=$1

mkdir -p ~/Sync/workspace/ChargedHiggsAnalysisV3/MeasTrigEff/results/${ERA}/ROOT

cp results/TopHNT_Electron_Run3_v0/TopHNT_${ERA}/efficiency.root ~/Sync/workspace/ChargedHiggsAnalysisV3/MeasTrigEff/results/${ERA}/ROOT/efficiency_EleID.root

cp results/TopHNT_Muon_Run3_v0/NUM_TopHNT_DEN_TrackerMuons_${ERA}/efficiency.root ~/Sync/workspace/ChargedHiggsAnalysisV3/MeasTrigEff/results/${ERA}/ROOT/efficiency_MuID.root

cp results/TopHNT_Muon_Run3_v0/NUM_DLT_Mu17Leg_DEN_TopHNT_${ERA}/efficiency.root ~/Sync/workspace/ChargedHiggsAnalysisV3/MeasTrigEff/results/${ERA}/ROOT/efficiency_DLT_Mu17Leg.root

cp results/TopHNT_Muon_Run3_v0/NUM_DLT_Mu8Leg_DEN_TopHNT_${ERA}/efficiency.root ~/Sync/workspace/ChargedHiggsAnalysisV3/MeasTrigEff/results/${ERA}/ROOT/efficiency_DLT_Mu8Leg.root
#!/bin/bash
ERA=$1

CONFIG_El=""
CONFIG_Mu=""
if [[ $ERA == "201"* ]]; then
    CONFIG_El="TopHNT_Electron_v2"
    CONFIG_Mu="TopHNT_Muon_v1"
elif [[ $ERA == "202"* ]]; then
    CONFIG_El="TopHNT_Electron_Run3_v1"
    CONFIG_Mu="TopHNT_Muon_Run3_v0"
else
    echo "Invalid ERA"
    exit 1
fi

mkdir -p ~/Sync/workspace/ChargedHiggsAnalysisV3/MeasTrigEff/results/${ERA}/ROOT

cp results/${CONFIG_El}/TopHNT_${ERA}/efficiency.root ~/Sync/workspace/ChargedHiggsAnalysisV3/MeasTrigEff/results/${ERA}/ROOT/efficiency_EleID.root
cp results/${CONFIG_Mu}/NUM_TopHNT_DEN_TrackerMuons_${ERA}/efficiency.root ~/Sync/workspace/ChargedHiggsAnalysisV3/MeasTrigEff/results/${ERA}/ROOT/efficiency_MuID.root
cp results/${CONFIG_Mu}/NUM_DLT_Mu17Leg_DEN_TopHNT_${ERA}/efficiency.root ~/Sync/workspace/ChargedHiggsAnalysisV3/MeasTrigEff/results/${ERA}/ROOT/efficiency_DLT_Mu17Leg.root
cp results/${CONFIG_Mu}/NUM_DLT_Mu8Leg_DEN_TopHNT_${ERA}/efficiency.root ~/Sync/workspace/ChargedHiggsAnalysisV3/MeasTrigEff/results/${ERA}/ROOT/efficiency_DLT_Mu8Leg.root
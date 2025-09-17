#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_13_3_1/src
eval `scramv1 runtime -sh`
cd -

export TNP_BASE="/data9/Users/choij/Sync/workspace/tnp_tamsa"
export PATH=$TNP_BASE/python:$PATH
export PYTHONPATH=$TNP_BASE/python${PYTHONPATH:+:$PYTHONPATH}
#export PYTHONPATH=${PYTHONPATH}:$TNP_BASE/tdr-style

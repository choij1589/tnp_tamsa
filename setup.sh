#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /cvmfs/cms.cern.ch/slc7_amd64_gcc900/cms/cmssw/CMSSW_11_2_5/src/
eval `scramv1 runtime -sh`
cd -
export TNP_BASE="/data6/Users/choij/tnp_tamsa"
export PYTHONPATH=$TNP_BASE/python${PYTHONPATH:+:$PYTHONPATH}

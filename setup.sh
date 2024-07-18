#!/bin/bash
if [[ $HOSTNAME == "localhost" ]]; then
    echo @@@@ Working in $HOSTNAME
    source ~/.conda-activate
    conda activate pyg
    export TNP_BASE=`pwd`
else
    source /cvmfs/cms.cern.ch/cmsset_default.sh
    cd /cvmfs/cms.cern.ch/slc7_amd64_gcc900/cms/cmssw/CMSSW_11_2_5/src/
    eval `scramv1 runtime -sh`
    cd -
    export TNP_BASE="/data6/Users/choij/tnp_tamsa"
fi
export PYTHONPATH=$TNP_BASE/python${PYTHONPATH:+:$PYTHONPATH}
export PYTHONPATH=${PYTHON_PATH}:$TNP_BASE/tdr-style

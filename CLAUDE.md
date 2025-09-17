# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is **tnp_tamsa**, a Tag-and-Probe (TnP) analysis framework for measuring lepton identification and trigger efficiencies in CMS physics data. The framework processes ROOT files containing physics data and Monte Carlo simulations to extract efficiency measurements using statistical fitting methods.

## Architecture

The codebase follows a modular design with distinct components:

### Core Components
- **tnp_tamsa.py**: Main orchestrator script that coordinates the analysis workflow (histogram creation, fitting, summarization)
- **python/tnpConfig.py**: Central configuration class (`tnpConfig`) that manages analysis parameters, binning, systematic variations, and data/MC samples
- **python/fitUtils.py**: Statistical fitting utilities using RooFit for efficiency extraction
- **python/histUtils.py**: Histogram creation and manipulation utilities
- **python/plotUtils.py**: Plotting and visualization tools
- **python/efficiencyUtils.py**: Efficiency calculation and combination utilities

### Configuration System
- **config/**: Contains analysis configuration files (Python modules) defining:
  - Sample paths and weights
  - Binning schemes for different measurements
  - Fitting parameters and systematic variations
  - Selection criteria for tag/probe pairs
- Key configurations include AFB (Asymmetry Forward-Backward), POG (Physics Object Group), and TopHNT (Top Heavy Neutral Leptons) analyses

### Analysis Workflow
The framework implements a three-step process:
1. **hist**: Create pass/fail histograms from input ROOT trees
2. **fit**: Perform statistical fits to extract efficiencies
3. **sum**: Combine results and generate final plots

## Common Commands

### Environment Setup
```bash
source setup.sh
```
This script sets up the environment by:
- Activating conda environment (local) or CVMFS environment (CERN)
- Setting `TNP_BASE` environment variable
- Configuring Python paths

### Basic Analysis Execution
```bash
# Basic usage pattern
python tnp_tamsa.py <config_file> <config_name>

# Example: Run TopHNT electron analysis for 2016a
python tnp_tamsa.py config/TopHNT_Electron_v1.py TopHNT_2016a

# Run specific steps
python tnp_tamsa.py config/AFBMuon_v15.py 2018_MediumID_LooseTrkIso --step hist,fit,sum
```

### Batch Processing Scripts
Several convenience scripts automate common analysis workflows:
- `doThisTopHNT.sh`: Runs TopHNT muon analysis for all years
- `doThisPOGEle.sh`: Runs POG electron analysis
- `doThisMu17.sh` / `doThisMu8.sh`: Runs specific muon trigger analyses

### Configuration Management
```bash
# Check available configurations in a config file
python tnp_tamsa.py config/TopHNT_Electron_v1.py --checkConfig

# Check binning definitions
python tnp_tamsa.py config/TopHNT_Electron_v1.py TopHNT_2016a --checkBins
```

### Condor Job Submission
The framework supports HTCondor for large-scale processing:
```bash
# Submit with default job splitting
python tnp_tamsa.py config/file.py config_name --njob 100,10

# Control concurrency
python tnp_tamsa.py config/file.py config_name --nmax 50
```

## Configuration File Structure

Configuration files define:
- **samples**: Dictionary mapping logical names to ROOT file paths
- **binnings**: Multi-dimensional binning schemes for different analyses
- **fit_parameters**: RooFit model definitions for signal and background
- **Configs**: Dictionary of `tnpConfig` objects defining complete analysis setups

### Key Configuration Elements
- **Systematic variations**: Alternative fitting models, MC samples, selection criteria
- **Binning schemes**: Eta-pt binning for ID efficiencies, optimized bins for trigger measurements
- **Selection criteria**: Tag selection, probe definitions, physics object requirements

## Development Notes

### Dependencies
- ROOT/PyROOT for data processing and fitting
- NumPy for numerical operations
- RooFit for statistical modeling
- Environment managed via conda (local) or CVMFS (CERN computing)

### File Organization
- Results are organized by configuration name under `results/` or custom output directories
- Intermediate files (.d directories) contain condor job outputs
- Final results include efficiency.root files and plots/

### Testing and Validation
- Use `--checkConfig` and `--checkBins` flags for configuration validation
- Individual bin processing available via `--bin` parameter
- Systematic variations help assess uncertainties

### Plotting and Visualization
- Automatic plot generation in summary step
- TDR-style formatting applied via tdr-style/ directory
- Plots saved as PNG files organized by configuration

## Special Features

### Systematic Uncertainty Handling
The framework systematically varies:
- Fitting models (alternative signal/background shapes)
- MC generators (different physics simulations)
- Selection criteria (tag pT thresholds)
- Fit windows (mass range variations)

### Multi-dimensional Binning
Supports up to 3D efficiency measurements with automatic histogram creation and bin management.

### Data/MC Scale Factors
Automatically computes scale factors by dividing data efficiencies by MC efficiencies, with proper error propagation.

## Best Practices and Workflow Tips

### Python and Environment Setup
- Always do `source setup.sh` first to set up the correct environment
- Use `python3` for executing Python scripts in this repository
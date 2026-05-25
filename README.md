# Norovirus VP1 Phytochemical Docking Study

## Project Title
Discovery of Phytochemicals as Potential Inhibitors or Virucidal Agents Against Norovirus

## Objective
Computational screening of four phytochemicals (cyclocommunol, curcumin, quercetin, EGCG)
against the Norovirus VP1 capsid protein (PDB: 6GVZ) using molecular docking.

## Target
- Protein: Norovirus VP1 P-domain
- PDB ID: 6GVZ

## Candidate Ligands
| Ligand | Source Plant | PubChem CID |
|--------|-------------|-------------|
| Cyclocommunol | Artocarpus communis (breadfruit) | 10315987 |
| Curcumin | Curcuma longa (turmeric) | 969516 |
| Quercetin | Multiple plants | 5280343 |
| EGCG | Camellia sinensis (green tea) | 65064 |

## Tools Used
- AutoDock Vina 1.2.x — Molecular docking engine
- PyMOL 4.6.0 — 3D visualization
- MGLTools 1.5.7 / AutoDockTools — Protein preparation (PDBQT)
- Open Babel 3.1.0 — Ligand format conversion and PDBQT preparation
- SwissADME — Drug-likeness and ADME analysis
- Python 3.9 — Automation scripts

## Project Status
- [x] Phase 1 — Project understanding
- [x] Phase 2 — Environment setup
- [x] Phase 3 — Protein preparation
- [x] Phase 4 — Ligand preparation
- [x] Phase 5 — Binding site identification
- [ ] Phase 6 — Docking execution
- [ ] Phase 7 — Visualization
- [ ] Phase 8 — Drug-likeness analysis
- [ ] Phase 9 — Results interpretation
- [ ] Phase 10 — Documentation

## Repository Structure
\```
├── data/
│   ├── protein/          # Raw and prepared protein files
│   └── ligands/
│       ├── raw/          # Downloaded SDF/MOL2 files
│       └── prepared/     # PDBQT-ready ligand files
├── results/
│   ├── docking_outputs/  # Vina output files per ligand
│   └── binding_scores/   # Score summaries
├── scripts/              # Python/shell scripts used
├── figures/              # PyMOL screenshots and plots
└── docs/                 # Notes, methodology drafts
\```

# Environment Setup Log

## System
- OS: Windows 11 64-bit
- Username: Aashi-tripathi
- Date: 20-05-2026

## Tools Installed
| Tool | Version | Location |
|------|---------|----------|
| Git | 2.54.0 | System PATH |
| AutoDock Vina | 1.2.x | C:\AutoDock\vina.exe |
| MGLTools | 1.5.7 | C:\Program Files (x86)\MGLTools-1.5.7 |
| PyMOL open-source | 4.6.0 | conda docking environment |
| Open Babel | 3.1.0 | conda docking environment |
| SwissADME | web-based | swissadme.ch |

## Conda Environment
- Environment name: docking
- Python version: 3.9
- Activated via: Anaconda Prompt

## Key Notes
- MGLTools is at Program Files (x86), NOT C:\MGLTools-1.5.7
- PyMOL and Open Babel only accessible from Anaconda Prompt
- Git and Vina accessible from regular Command Prompt

## Preparation Notes
- Protein: Water molecules (HOH) and co-crystallized ligand (CHO) 
  removed using custom Python script. Hydrogens and Kollman charges 
  added via AutoDockTools.
- Ligands: Downloaded as 3D conformer SDF from PubChem. Converted 
  to PDBQT using Open Babel with Gasteiger partial charges.
- Binding site: Defined using coordinates of co-crystallized ligand 
  CHO (X=-9.586, Y=-53.924, Z=16.226) as grid box center.
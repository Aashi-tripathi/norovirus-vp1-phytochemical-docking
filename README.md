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
| Cyclocommunol | Artocarpus communis (breadfruit) | TBD |
| Curcumin | Curcuma longa (turmeric) | TBD |
| Quercetin | Multiple plants | TBD |
| EGCG | Camellia sinensis (green tea) | TBD |

## Tools Used
- AutoDock Vina 1.2.x — Molecular docking
- PyMOL — Visualization
- MGLTools 1.5.7 — File preparation (PDBQT)
- Open Babel — Format conversion
- SwissADME — Drug-likeness analysis

## Project Status
- [x] Phase 1 — Project understanding
- [x] Phase 2 — Environment setup
- [ ] Phase 3 — Protein preparation
- [ ] Phase 4 — Ligand preparation
- [ ] Phase 5 — Binding site identification
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
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
- [ ] Phase 2 — Environment setup
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
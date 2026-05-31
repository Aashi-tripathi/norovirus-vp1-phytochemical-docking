# Methodology

## 1. Software and Tools
| Tool | Version | Purpose |
|------|---------|---------|
| AutoDock Vina | 1.2.7 | Molecular docking |
| PyMOL open-source | 4.6.0 | Visualization |
| MGLTools/AutoDockTools | 1.5.7 | Protein preparation |
| Open Babel | 3.1.0 | Ligand preparation |
| SwissADME | web server | Drug-likeness |
| Python | 3.9 | Automation scripts |

## 2. Protein Preparation
- Source: RCSB PDB, ID 6GVZ
- Resolution: 1.54 Å, X-ray diffraction
- Cleaning: HOH and HETATM removed (clean_protein.py)
- Preparation: Hydrogens added, Kollman charges computed
- Output: 6GVZ_prepared.pdbqt

## 3. Ligand Preparation
- Source: PubChem 3D conformers
- Format conversion: SDF → PDB → PDBQT (Open Babel)
- Charges: Gasteiger partial charges
- Output: prepared/*.pdbqt

## 4. Grid Box Parameters
- Center: X=-9.586, Y=-53.924, Z=16.226
- Dimensions: 25×25×25 Å
- Basis: Co-crystallized CHO ligand coordinates

## 5. Docking Parameters
- Scoring function: Vina
- Exhaustiveness: 8
- Binding modes: 9
- Energy range: 3 kcal/mol

## 6. Interaction Analysis
- Software: PyMOL 4.6.0
- Binding site: residues within 5.5 Å of ligand
- H-bond cutoff: 3.5 Å, geometric mode 2

## 7. Drug-likeness
- Tool: SwissADME
- Filter: Lipinski Rule of Five
- Input: Canonical SMILES from PubChem
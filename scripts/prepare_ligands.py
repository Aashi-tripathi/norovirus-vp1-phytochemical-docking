# prepare_ligands.py
# Purpose: Convert all ligand SDF files to PDB format using Open Babel
# Open Babel handles 3D coordinate generation if needed
# Input:  data/ligands/raw/*.sdf
# Output: data/ligands/raw/*.pdb (intermediate files)

import subprocess
import os

# Define project root — change this if your path is different
project_root = r"C:\Users\Aash2\OneDrive\Desktop\norovirus-vp1-phytochemical-docking"

# List of ligands to process
ligands = [
    "curcumin",
    "quercetin", 
    "egcg",
    "cyclocommunol"
]

raw_dir = os.path.join(project_root, "data", "ligands", "raw")

print("=" * 50)
print("LIGAND SDF TO PDB CONVERSION")
print("=" * 50)

for ligand in ligands:
    sdf_file = os.path.join(raw_dir, f"{ligand}.sdf")
    pdb_file = os.path.join(raw_dir, f"{ligand}.pdb")
    
    # Check SDF file exists
    if not os.path.exists(sdf_file):
        print(f"ERROR: {ligand}.sdf not found in {raw_dir}")
        print(f"       Please download it from PubChem first")
        continue
    
    # Run Open Babel conversion
    # --gen3d generates 3D coordinates if only 2D is available
    # -h adds hydrogens
    cmd = [
        "obabel",
        "-isdf", sdf_file,
        "-opdb",
        "-O", pdb_file,
        "--gen3d",
        "-h"
    ]
    
    print(f"\nProcessing: {ligand}")
    print(f"Input : {sdf_file}")
    print(f"Output: {pdb_file}")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if os.path.exists(pdb_file):
        size = os.path.getsize(pdb_file)
        print(f"Status: SUCCESS — {size} bytes written")
    else:
        print(f"Status: FAILED")
        print(f"Error : {result.stderr}")

print("\n" + "=" * 50)
print("Conversion complete. Check data/ligands/raw/ for .pdb files")
print("=" * 50)
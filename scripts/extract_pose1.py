# extract_pose1.py
# Extracts the best docking pose (Model 1) from each Vina output file
# Converts PDBQT to PDB format for PyMOL visualization

import os

project_root = r"C:\Users\Aash2\OneDrive\Desktop\norovirus-vp1-phytochemical-docking"

ligands = ["curcumin", "quercetin", "egcg", "cyclocommunol"]

docking_dir = os.path.join(project_root, "results", "docking_outputs")
figures_dir = os.path.join(project_root, "figures")

print("=" * 50)
print("EXTRACTING BEST POSE FROM EACH DOCKING OUTPUT")
print("=" * 50)

for ligand in ligands:
    input_file = os.path.join(docking_dir, f"{ligand}_out.pdbqt")
    output_file = os.path.join(docking_dir, f"{ligand}_pose1.pdb")
    
    if not os.path.exists(input_file):
        print(f"ERROR: {ligand}_out.pdbqt not found")
        continue
    
    pose1_lines = []
    inside_model1 = False
    
    with open(input_file, 'r') as f:
        for line in f:
            # Start capturing at MODEL 1
            if line.strip() == "MODEL 1":
                inside_model1 = True
                continue
            # Stop capturing at ENDMDL
            if line.strip() == "ENDMDL" and inside_model1:
                break
            # Keep ATOM and HETATM lines, convert to PDB format
            if inside_model1:
                if line.startswith("ATOM") or line.startswith("HETATM"):
                    # Remove the charge column at end (not standard PDB)
                    pose1_lines.append(line[:66] + "\n")
                elif line.startswith("REMARK"):
                    pose1_lines.append(line)
    
    with open(output_file, 'w') as f:
        f.writelines(pose1_lines)
        f.write("END\n")
    
    if os.path.exists(output_file):
        print(f"\n{ligand}: SUCCESS")
        print(f"  Score: check REMARK line in {ligand}_out.pdbqt")
        print(f"  Saved: {ligand}_pose1.pdb")
    else:
        print(f"\n{ligand}: FAILED")

print("\n" + "=" * 50)
print("Pose 1 extraction complete")
print("=" * 50)
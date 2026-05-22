# clean_protein.py
# Purpose: Remove HETATM records (water, ligands, additives) from PDB file
# Keeps only ATOM records which represent the actual protein
# Input:  data/protein/6GVZ.pdb
# Output: data/protein/6GVZ_clean.pdb

input_file  = r"C:\Users\Aash2\OneDrive\Desktop\norovirus-vp1-phytochemical-docking\data\protein\6GVZ.pdb"
output_file = r"C:\Users\Aash2\OneDrive\Desktop\norovirus-vp1-phytochemical-docking\data\protein\6GVZ_clean.pdb"

kept_lines    = 0
removed_water = 0
removed_heta  = 0

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:

        # Count and skip water molecules
        if line.startswith('HETATM') and 'HOH' in line:
            removed_water += 1
            continue

        # Count and skip all other HETATM records (CHO, SO4, GOL etc.)
        if line.startswith('HETATM'):
            removed_heta += 1
            continue

        # Skip ANISOU lines - not needed for docking
        if line.startswith('ANISOU'):
            continue

        # Keep everything else (ATOM, REMARK, HEADER, SEQRES, END)
        outfile.write(line)
        kept_lines += 1

print("Cleaning complete.")
print(f"Water molecules removed : {removed_water} lines")
print(f"Other HETATM removed    : {removed_heta} lines")
print(f"Lines kept              : {kept_lines}")
print(f"Output saved to         : {output_file}")
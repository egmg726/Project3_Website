from Bio.PDB.PDBParser import PDBParser


parser = PDBParser()
structure = parser.get_structure('test','4igk.pdb1')
residues = structure.get_residues()
for residue in residues:
	print(residue)

from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.PDBList import PDBList
import urllib
import xml.etree.ElementTree as ET


parser = PDBParser()
pdbl = PDBList()
structure = parser.get_structure('4igk','4IGK.pdb')
#structure = pdbl.retrieve_pdb_file('1JM7')
residues = structure.get_residues()
compound = structure.header['compound']
title = structure.header['name']
journal = structure.header['journal_reference']
dict_keys = ['synonym','chain','fragment','molecule']
start_pos,end_pos = compound['1']['fragment'].split('unp residues ')[1].split('-')
start_pos = int(start_pos)
end_pos = int(end_pos)
print compound['1']['synonym']
pdb_dict = {}

for comp in range(0,len(compound)):
    key = str(comp+1)
    for dkey in dict_keys:
        compound[key][dkey]
    

#if residue is within start and end positions



#print pdbl.retrieve_pdb_file('1FAT')

#print structure.header['name']


'''
for residue in residues:
	print(residue.get_full_id()[3][1])

url = 'http://files.rcsb.org/view/4Y18.pdb'

webpage = urllib.urlopen(url)
#print webpage.read()

text_file = open('pdb_test.txt','w')
text_file.write(webpage.read())
text_file.close()
'''

url = 'http://pfam.xfam.org/protein/BRCA1_HUMAN?output=xml'
webpage = urllib.urlopen(url)
xml_text = webpage.read()

'''
text_file = open('xml_test.xml','w')
text_file.write(xml_text)
text_file.close()
'''

root = ET.fromstring(xml_text)
#print xml_text

tree = ET.parse('xml_test.xml')
root = tree.getroot()

#print root.tag



count = 0
match_dict = {}

for child in root.iter('match'):
    type_attr = child.attrib['type']
    acc_attr = child.attrib['accession']
    id_attr = child.attrib['id']

    for grandchild in child.iter('location'):
        start = grandchild.attrib['start']
        end = grandchild.attrib['end']
        match_dict[count] = [type_attr,acc_attr,id_attr,int(start),int(end)]
        count += 1

print match_dict

for seq in root.iter('sequence'):
    sequence = seq.text

print sequence

    

    




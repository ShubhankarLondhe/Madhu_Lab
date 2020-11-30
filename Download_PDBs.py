
from Bio.PDB import *
import csv

'''
The only thing you need is a list of PDB IDs.
'''

pdb1 = PDBList()

with open('culled_list_nr30.txt', newline='') as csvfile:  		#This file contains the list of PDB Ids I want downloaded. One PDB Id in each line in my case since the output was like that. 							
    data = list(csv.reader(csvfile))

for line in data:												#line looks like: "3C5I       1482      XRAY        2.200    0.21    0.26".
	line = line[0].rsplit()
	pdb_id = line[0]
	pdb1.retrieve_pdb_file(pdb_id, file_format = "pdb", pdir = "path directory")			#This line downloads the PDB.


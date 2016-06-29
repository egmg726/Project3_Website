import requests, sys
import json
import pandas as pd
import math
 
server = "https://rest.ensembl.org"
server = "http://grch37.rest.ensembl.org"
#ext = "/vep/human/region/9:22125503-22125502:1/C?"
#ext = "/vep/human/hgvs/ENST00000357654:c.5A>G"
#ext = "/vep/human/hgvs/ENSP00000418960:p.M1V"
#ext = "/lookup/id/ENSG00000012048?expand=1"
ext = "/lookup/id/ENST00000357654?expand=1"
#ext = "/variation/human/rs80356994"
#ext = "/vep/human/region/17:43124078-43124078:1/C"
ext = "/vep/human/region/17:41276044-41276044:1/G"

r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
 
if not r.ok:
  r.raise_for_status()
  sys.exit()
 
decoded = r.json()
ensembl_dict = decoded[0]


brca1_csv = pd.read_csv('/project/homemsc/eg315/project3/p3_website/BRCA1.missense.20150128.csv')
chr_list = brca1_csv.hg19_chr.tolist()
pos_list = brca1_csv.hg19_pos.tolist()

for x in brca1_csv.rsID.tolist():
    if type(x) == float:
        continue
    elif type(x) == str:
        break

#print decoded

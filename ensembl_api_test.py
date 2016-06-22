import requests, sys
import json
 
server = "https://rest.ensembl.org"
#ext = "/vep/human/region/9:22125503-22125502:1/C?"
ext = "/vep/human/hgvs/ENST00000357654:c.1A>C"
ext = "/vep/human/hgvs/ENSP00000418960:p.M1L"
 
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
 
if not r.ok:
  r.raise_for_status()
  sys.exit()
 
decoded = r.json()
print decoded

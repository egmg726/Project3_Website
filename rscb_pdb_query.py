import requests
import pandas as pd
import urllib

url = "http://www.rcsb.org/pdb/rest/search"

queryText = """
<?xml version="1.0" encoding="UTF-8"?>
<orgPdbQuery>    
    <queryType>org.pdb.query.simple.UpAccessionIdQuery</queryType>
    <description>Simple query for a list of UniprotKB Accession IDs:  P69905</description>   
    <accessionIdList> P69905</accessionIdList>
</orgPdbQuery>
"""

response = requests.post(
  url,
  data=queryText.encode(),
  headers={'Content-Type': 'application/x-www-form-urlencoded'}
)

pdb_str = ''
for pdb_id in response.text.encode('ascii').split('\n'):
    pdb_str += pdb_id+','

webpage = urllib.urlopen('http://www.rcsb.org/pdb/rest/customReport.csv?pdbids=1stp,2jef,1cdg&customReportColumns=structureId,structureTitle,experimentalTechnique&format=csv')
print webpage.read()

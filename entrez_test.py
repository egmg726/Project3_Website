from Bio import Entrez
Entrez.email = 'emma.gail15@imperial.ac.uk'
#handle = Entrez.esearch(db='gene',retmax=10,term='BRCA1')
handle = Entrez.esummary(db='gene',id='672',retmode='xml')
record = Entrez.read(handle)
handle.close()

print record

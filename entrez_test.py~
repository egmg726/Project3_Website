from Bio import Entrez
#import pandas as pd


#for loop when have all gene ids
#store in file

def get_entrez_gene_dict(gene_id):
    gene_id = str(gene_id)
    Entrez.email = 'emma.gail15@imperial.ac.uk'
    handle = Entrez.esummary(db='gene',id=gene_id,retmode='text')
    record = Entrez.read(handle)
    handle.close()
    entrez_dict = dict(record['DocumentSummarySet'])
    gene_dict = dict(entrez_dict['DocumentSummary'][0])
    return gene_dict


Entrez.email = 'emma.gail15@imperial.ac.uk'
#handle = Entrez.esearch(db='nucleotide',retmax=10,term='BRCA1[gene] AND human[orgn]')
handle = Entrez.esummary(db='gene',id='672',retmode='text')
record = Entrez.read(handle)
handle.close()

entrez_dict = dict(record['DocumentSummarySet'])
gene_dict = dict(entrez_dict['DocumentSummary'][0])
print gene_dict
#print gene_dict['Description']
#print gene_dict['Summary']


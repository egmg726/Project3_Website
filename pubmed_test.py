import pandas as pd
from Bio import Entrez

brca1_csv = pd.read_csv('/project/homemsc/eg315/project3/p3_website/BRCA1.missense.20150128.csv')
pubmed_list = brca1_csv.hgmd_pubmed_list.dropna().tolist()
pubmed_list.append(brca1_csv.walker_pubmeds.dropna().tolist())
pmid_list = []
for pmid in pubmed_list:
    if ' ' in pmid:
        plist = pmid.split()
        for p in plist:
            if p not in pmid_list:
                try:
                    int(p)
                    pmid_list.append(p)
                except ValueError:
                    continue

    elif ',' in pmid:
        plist = pmid.split(',')
        for p in plist:
            if p not in pmid_list:
                try:
                    int(p)
                    pmid_list.append(p)
                except ValueError:
                    continue

    else:
        if pmid not in pmid_list:
            try:
                int(pmid)
                pmid_list.append(pmid)
            except ValueError:
                continue
            except TypeError:
                continue


Entrez.email = 'emma.gail15@imperial.ac.uk'

#with open('pmid_dict.py','w') as text_file:

pmid_dict = {}
for pmid in pmid_list:
    handle = Entrez.esummary(db='pubmed',id=pmid,retmode='text')
    record = Entrez.read(handle)
    handle.close()
    pmid_dict[pmid] = record[0]
    break

#print pmid_dict['22762150']
    
    
with open('pmid_dict.py','w') as text_file:
    text_file.write('pmid_dict = '+str(pmid_dict))



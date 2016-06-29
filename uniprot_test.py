from Bio import SeqIO

record = SeqIO.read(open('P38398_uniprot.xml'),'uniprot-xml')
#record.features
for ref in record.annotations['references']:
    print ref.pubmed_id
    break
#record.annotations['comment_domain']
#print record.annotations['comment_tissuespecificity']
#record.annotations['comment_enzymeregulation']
#record.annotations['comment_disease']
#record.annotations['comment_onlineinformation']
#record.annotations['comment_subunit']
#record.annotations['comment_function']
#record.annotations['comment_polymorphism']
#record.annotations['comment_PTM']
#print record.annotations['comment_function']

#print record.annotations.keys()

for feature in record.features:
    
    print feature.qualifiers
    break
    feature.type
    feature.location
    feature.id
    feature.qualifiers
    #print feature.qualifiers
#str(feature.location).split(':')
    

#handle = open('P38398_uniprot.xml','rU')
#for record in SeqIO.parse(handle,'uniprot-xml'):
#    print(record)
#handle.close()

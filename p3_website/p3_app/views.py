from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.PDBList import PDBList
import urllib
import xml.etree.ElementTree as ET
from django.conf import settings
import os

from .forms import RsForm
from .models import *
from pmid_dict import *
from gene_dict import *

def index(request):
    errors = []
    which_error = None

    if request.POST:

        try:
            rsid = request.POST['rs_id']
            
        except MultiValueDictKeyError:
            rsid = False
            

        try:
            chr_num = request.POST['chr_num']
            chr_loc = request.POST['chr_loc']
            
        except MultiValueDictKeyError:
            chr_num = False
            chr_loc = False
            

        snpsub = request.POST.get('snpsubstitution', '')

        try:
            protein_id = request.POST['protein_id']
            aa_change = request.POST['aa_change']
        except MultiValueDictKeyError:
            protein_id = False
            aa_change = False


        if rsid != False:      
            if rsid.startswith('rs') == False:
                errors.append('Please enter a valid rs number')
            elif not Brca1New.objects.filter(rsid=rsid).exists():
                errors.append('This ID is not currently in our database.')
        
            if not errors:
                brca1_objects = Brca1New.objects.filter(rsid=rsid)
                brca1_object = ''
                for obj in brca1_objects:
                    sub = obj.hgvs_cdna.split('>')[1]
                    if sub == snpsub:
                        brca1_object = obj
                        break

                if brca1_object == '':
                    errors.append('You have not entered a missense mutation for this position.')
    

        elif chr_loc != False:
            try:
                int(chr_loc)
            except ValueError:
                errors.append('You have not entered a valid integer for the chromosome location.')
            try:
                int(chr_num)
            except ValueError:
                errors.append('You have not entered a valid integer for the chromosome number.')    
            if not Brca1New.objects.filter(hg19_pos=chr_loc).exists():
                errors.append('This position does not currently exist in our database.')
            var_loc_objects = Brca1New.objects.filter(hg19_pos=chr_loc)
            brca1_object = ''
            for obj in var_loc_objects:
                if obj.hg19_chr != chr_num:
                    var_loc_objects.remove(obj)
                else:
                    sub = obj.hgvs_cdna.split('>')[1]
                    if sub == snpsub:
                        brca1_object = obj
                        break                   

            if brca1_object == '':
                errors.append('You have not entered a missense mutation for this position.')    

        elif protein_id != False:

            if not Brca1New.objects.filter(gene=protein_id).exists():
                errors.append('You have entered an ID that does not currently exist in our database.')
            else:
                brca1_object = None
                for obj in Brca1New.objects.filter(gene=protein_id):
                    if aa_change == obj.hgvs_prot.split('.')[1] or aa_change == obj.hgvs_prot_code1.split('.')[1]:
                        brca1_object = obj
                        break

                if brca1_object == None:
                    errors.append('That amino acid change was not found in the database.') 


    
        if errors:
            if rsid != False:
                which_error = 'rsid'
            elif chr_loc != False:
                which_error = 'chr'
            elif protein_id != False:
                which_error = 'protein_id'

            return render(request,'p3_app/index.html',{'errors':errors, 'which_error':which_error})

        resi_num = brca1_object.hgvs_prot_code1.split('.')[1][:-1][1:]
        resi_string = 'resi:'+str(resi_num)+';chain:A'

        if int(resi_num) >= 1 and int(resi_num) <= 103:
            pdb_entry = '1JM7'
        elif int(resi_num) >= 1646 and int(resi_num) <= 1859:
            pdb_entry = '4IGK'
        else:
            pdb_entry = None


        #list of pdb information for each gene for protein sequence diagram

        if pdb_entry is not None:
            parser = PDBParser()
            pdbl = PDBList()
            module_dir = os.path.dirname(__file__)  # get current directory
            file_path = os.path.join(module_dir, 'static/p3_app/pdb_files/'+pdb_entry+'.pdb')
            pdb_file = open(file_path)
            structure = parser.get_structure(pdb_entry,pdb_file)
            compound = structure.header['compound']
            title = structure.header['name']
            journal = structure.header['journal_reference']
            pdb_list = [compound,title,journal]
        else:
            pdb_list = []

        #create a list of synonyms and fragments so they're properly capitalized for site

        pfam_id = 'P38398'

        #create dictionary for uniprot/gene names when all gene names are present

        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, 'static/p3_app/pfam_files/'+pfam_id+'.xml')
        xml_file = open(file_path)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        count = 0
        match_dict = {}

        resi_in_domain = None

        for child in root.iter('match'):
            type_attr = child.attrib['type']
            acc_attr = child.attrib['accession']
            id_attr = child.attrib['id']

            for grandchild in child.iter('location'):
                start = grandchild.attrib['start']
                end = grandchild.attrib['end']
                start = int(start)
                end = int(end)
                if resi_num > end and resi_num < start:
                     resi_in_domain = id_attr
                match_dict[count] = [type_attr,acc_attr,id_attr,start,end]
                count += 1

        for seq in root.iter('sequence'):
            sequence = seq.text

        

        #additional pfam info for mouseover feature

        if brca1_object.hgmd_pubmed == 'Pubmed':
            hgmd_pubmed_list = brca1_object.hgmd_pubmed_list.split(' ')
        else:
            hgmd_pubmed_list = None

        pubmed_dict = {}
        if hgmd_pubmed_list is not None:
            for pmid in hgmd_pubmed_list:
                if pmid in pmid_dict.keys():
                    pubmed_dict[pmid] = pmid_dict[pmid]


                
        #add info for pubmed list - turn into dictionary of citation values

        #add checkpoint to make sure residues match of pdb file and residue of variation in database
        #Brca1New.objects.values('swissprot_type').distinct()
        
        count = 0
        swissprot_dict = {}
        for sp_ran in Brca1New.objects.values_list('swissprot_range').distinct():
            sp_ran = ''.join(sp_ran)
            obj = Brca1New.objects.filter(swissprot_range=sp_ran)[0]
            sp_type = obj.swissprot_type.encode('ascii')
            sp_desc = obj.swissprot_desc.encode('ascii')
            if sp_desc == '':
                continue
            
            sp_ran = sp_ran.split('[')[1].split(']')[0]
            
            if '-' in sp_ran:
                start,end = sp_ran.split('-')
                start = int(start)
                end = int(end)
            else:
                start = int(sp_ran)
                end = int(sp_ran)
            
            swissprot_dict[count] = [sp_type,start,end,sp_desc]
            count += 1
        
        count = 0
        alamut_pd1_dict = {}
        ala_list = []
        ala_indices = []
        cdna_pos_list = []
        end = 0

        for ala_dom in Brca1New.objects.values_list('alamut_proteindomain1'):
            ala_dom = ''.join(ala_dom)
            ala_list.append(ala_dom)

        for cdna_pos in Brca1New.objects.values_list('codon'):
            cdna_pos = ''.join(cdna_pos)
            cdna_pos_list.append(cdna_pos)
        
        for ala_ind in range(1,len(ala_list)):
            if ala_list[ala_ind-1] == ala_list[ala_ind]:
                continue
            else:
               # if ala_list[ala_ind-1] == '':
               #     continue

                if end == 0:
                    for ai in range(1,len(ala_list)):
                        if ala_list[ai] == ala_list[ala_ind-1]:
                            start = int(cdna_pos_list[ai])
                            break
                            
                else:
                    start = end+1

                end = int(cdna_pos_list[ala_ind])
                domain = ala_list[ala_ind-1]
                if domain != '':
                    alamut_pd1_dict[count] = [domain,start,end]
                    count += 1

        ala_list = []
        alamut_pd2_dict = {}
        end = 0
        count = 0
        for ala_dom in Brca1New.objects.values_list('alamut_proteindomain2'):
            ala_dom = ''.join(ala_dom)
            ala_list.append(ala_dom)
        
        for ala_ind in range(1,len(ala_list)):
            if ala_list[ala_ind-1] == ala_list[ala_ind]:
                continue
            else:
               # if ala_list[ala_ind-1] == '':
               #     continue

                if end == 0:
                    for ai in range(1,len(ala_list)):
                        if ala_list[ai] == ala_list[ala_ind-1]:
                            start = int(cdna_pos_list[ai])
                            break
                else:
                    start = end+1

                end = int(cdna_pos_list[ala_ind])
                domain = ala_list[ala_ind-1]
                if domain != '':
                    alamut_pd2_dict[count] = [domain,start,end]
                    count += 1                

        ala_list = []
        alamut_pd3_dict = {}
        end = 0
        count = 0
        for ala_dom in Brca1New.objects.values_list('alamut_proteindomain3'):
            ala_dom = ''.join(ala_dom)
            ala_list.append(ala_dom)
        
        for ala_ind in range(1,len(ala_list)):
            if ala_list[ala_ind-1] == ala_list[ala_ind]:
                continue
            else:
               # if ala_list[ala_ind-1] == '':
               #     continue

                if end == 0:
                    for ai in range(1,len(ala_list)):
                        if ala_list[ai] == ala_list[ala_ind-1]:
                            start = int(cdna_pos_list[ai])
                            break
                else:
                    start = end+1

                end = int(cdna_pos_list[ala_ind])
                domain = ala_list[ala_ind-1]
                if domain != '':
                    alamut_pd3_dict[count] = [domain,start,end]
                    count += 1                


                #make condition if last entry is part of a domain
        ala_list = []
        alamut_pd4_dict = {}
        end = 0
        count = 0
        for ala_dom in Brca1New.objects.values_list('alamut_proteindomain4'):
            ala_dom = ''.join(ala_dom)
            ala_list.append(ala_dom)
        
        for ala_ind in range(1,len(ala_list)):
            if ala_list[ala_ind-1] == ala_list[ala_ind]:
                continue
            else:
               # if ala_list[ala_ind-1] == '':
               #     continue

                if end == 0:
                    for ai in range(1,len(ala_list)):
                        if ala_list[ai] == ala_list[ala_ind-1]:
                            start = int(cdna_pos_list[ai])
                            break
                else:
                    start = end+1

                end = int(cdna_pos_list[ala_ind])
                domain = ala_list[ala_ind-1]
                if domain != '':
                    alamut_pd4_dict[count] = [domain,start,end]
                    count += 1                
                  


        if brca1_object.alamut_siftprediction == '':
            brca1_object.alamut_siftprediction = None

        if '_' in brca1_object.muttaster_prediction:
            brca1_object.muttaster_prediction = brca1_object.muttaster_prediction.replace('_',' ')

        if brca1_object.muttaster_features != '':
            brca1_object.muttaster_features = brca1_object.muttaster_features.split(',')

        ss_img_loc = int(brca1_object.suspect_score)*4
        agvgd_dict = {'C0': 40, 'C15': 92, 'C25':148, 'C35':205,'C45':261,'C55':317,'C65':375} 

        muttaster_model_dict = {'complex_aa':'mutation introducing a premature stop codon','simple_aae':'substitution/insertion/deletion of a single amino acid'}

        context = {'rsid':rsid, 'brca1_object':brca1_object,'resi_string':resi_string, 'resi_num':resi_num, 'pdb_entry':pdb_entry, 'chr_num':chr_num,'chr_loc':chr_loc, 'pdb_list':pdb_list, 'match_dict':match_dict, 'sequence':sequence, 'hgmd_pubmed_list':hgmd_pubmed_list, 'swissprot_dict':swissprot_dict, 'alamut_pd1_dict':alamut_pd1_dict,'alamut_pd2_dict':alamut_pd2_dict,'alamut_pd3_dict':alamut_pd3_dict,
'alamut_pd4_dict':alamut_pd4_dict,'agvgd_dict':agvgd_dict,
'ss_img_loc':ss_img_loc,'muttaster_model_dict':muttaster_model_dict, 
'pubmed_dict':pubmed_dict, 'gene_dict':gene_dict, 'protein_id':protein_id,'aa_change':aa_change}
        return render(request,'p3_app/results_page2.html',context)

    return render(request,'p3_app/index.html',{})

def thanks(request):
    return render(request,'p3_app/pviz_test.html')

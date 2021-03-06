from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.PDBList import PDBList
from Bio import SeqIO
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

        try:
            gene_id = request.POST['gene_id']
        except MultiValueDictKeyError:
            gene_id = False


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

        elif gene_id != False:
            if not Brca1New.objects.filter(gene=gene_id).exists():
                errors.append('You have entered an ID that does not currently exist in our database.')
                
    
        if errors:
            if rsid != False:
                which_error = 'rsid'
            elif chr_loc != False:
                which_error = 'chr'
            elif protein_id != False:
                which_error = 'protein_id'
            elif gene_id != False:
                which_error = 'gene_id'

            return render(request,'p3_app/index.html',{'errors':errors, 'which_error':which_error})

        context = {}

        context['rsid'] = rsid
        context['chr_loc'] = chr_loc
        context['chr_num'] = chr_num
        context['protein_id'] = protein_id
        context['gene_id'] = gene_id
        context['aa_change'] = aa_change

        #get right gene dict based on gene_id -- dictionary?
        context['gene_dict'] = gene_dict


        pdb_list_dict = {
            'BRCA1':['1JM7','4IGK'],

        }

    
        pdb_stop_start_dict = {
            '1JM7':[1,103],
            '4IGK':[1646,1859],
        }

        context['pdb_stop_start_dict'] = pdb_stop_start_dict




        if gene_id is False:
            resi_num = brca1_object.hgvs_prot_code1.split('.')[1][:-1][1:]
            context['resi_num'] = resi_num
            resi_string = 'resi:'+str(resi_num)+';chain:A'
            context['resi_string'] = resi_string

            pdb_entry_list = pdb_list_dict[brca1_object.gene]
            
            pdb_entry = None

            for pdbe in pdb_entry_list:
                pdb_stop_start_list = pdb_stop_start_dict[pdbe]
                if int(resi_num) >= pdb_stop_start_list[0] and int(resi_num) <= pdb_stop_start_list[1]:
                    pdb_entry = pdbe


        else:
            pdb_entry = pdb_list_dict[gene_id]
            resi_num = 0
            #create dictionary for this list
        


        context['pdb_entry'] = pdb_entry

        #list of pdb information for each gene for protein sequence diagram

        pdb_translate_list = ['ring','brca1','bard1','brct','unp','atrip','atm','rad3']
        do_not_translate_list = ['of','being','and','in','with','the']


        def correct_pdb_capitalization(title):
            title_split = title.split()
            title_list = []
            for t in title_split:
                if '/' in t:
                    t = t.split('/')
                    for ts in t:
                        for x in range(0,len(pdb_translate_list)):
                            if pdb_translate_list[x] == ts:
                                index = t.index(ts)
                                ts = ts.upper()
                                t[index] = ts
                        if ts not in do_not_translate_list and ts not in pdb_translate_list:
                            ts = ts.title()

    
                    t = "/".join(t)

                    title_list.append(t)

                elif '-' in t:
                    t = t.split('-')
                    for ts in t:
                        for x in range(0,len(pdb_translate_list)):
                            if pdb_translate_list[x] == ts:
                                index = t.index(ts)
                                ts = ts.upper()
                                t[index] = ts
                        if ts not in do_not_translate_list and ts not in pdb_translate_list:
                            ts = ts.title()

                    t = '-'.join(t)

                    title_list.append(t)

                else:
                   # for x in range(0,len(pdb_translate_list)):
                   #     if pdb_translate_list[x] == t:
                   #         t = t.upper()
                    if (t not in do_not_translate_list) and (t not in pdb_translate_list):
                        t = t.title()
                    if t in pdb_translate_list:
                        t = t.upper()
                       

                    title_list.append(t)              
            
            title = ' '.join(title_list)
            return title


        if pdb_entry is not None:
            parser = PDBParser()
            pdbl = PDBList()
            module_dir = os.path.dirname(__file__)  # get current directory
            if type(pdb_entry) == str:
                file_path = os.path.join(module_dir, 'static/p3_app/pdb_files/'+pdb_entry+'.pdb')
                pdb_file = open(file_path)
                structure = parser.get_structure(pdb_entry,pdb_file)
                compound = structure.header['compound']
                title = structure.header['name']
 
                title = correct_pdb_capitalization(title)

                for keys,values in compound.items():
                    for k,v in values.items():
                        if k != 'other_details':
                            values[k] = correct_pdb_capitalization(v)

                journal = structure.header['journal_reference']
                pdb_list = [compound,title,journal]
            elif type(pdb_entry) == list:
                pdb_dict = {}
                for pdbe in pdb_entry:        
                    file_path = os.path.join(module_dir, 'static/p3_app/pdb_files/'+pdbe+'.pdb')
                    pdb_file = open(file_path)
                    structure = parser.get_structure(pdb_entry,pdb_file)
                    compound = structure.header['compound']
                    title = structure.header['name']
                    title = correct_pdb_capitalization(title)
                    journal = structure.header['journal_reference']
                    pdb_list = [compound,title,journal]
                    pdb_dict[pdbe] = pdb_list

                pdb_list = []
                context['pdb_dict'] = pdb_dict

        else:
            pdb_list = []

        context['pdb_list'] = pdb_list

        #if gene_id is not False:
         #get gene list   

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

        context['sequence'] = sequence
        context['match_dict'] = match_dict
        context['resi_in_domain'] = resi_in_domain

        #additional pfam info for mouseover feature


        file_path = os.path.join(module_dir, 'static/p3_app/uniprot_files/'+pfam_id+'.xml')
        record = SeqIO.read(open(file_path),'uniprot-xml')
        uniprot_comment_dict = {}

        uniprot_comment_dict['domain'] = record.annotations['comment_domain']
        uniprot_comment_dict['tissue_specificity'] = record.annotations['comment_tissuespecificity']
        uniprot_comment_dict['enzyme_regulation'] = record.annotations['comment_enzymeregulation']
        uniprot_comment_dict['disease'] = record.annotations['comment_disease']

        oi_dict = {}
        for oi in record.annotations['comment_onlineinformation']:
            oi = oi.split('@')
            oi_dict[oi[0]] = oi[1]

        uniprot_comment_dict['subunit'] = record.annotations['comment_subunit']
        uniprot_comment_dict['function'] = record.annotations['comment_function']
        uniprot_comment_dict['polymorphism'] = record.annotations['comment_polymorphism']
        uniprot_comment_dict['ptm'] = record.annotations['comment_PTM']

        context['uniprot_comment_dict'] = uniprot_comment_dict
        context['oi_dict'] = oi_dict


        uniprot_references = record.annotations['references']
        context['uniprot_references'] = uniprot_references

        secondary_structure_features = []
        variant_features = []
        other_uniprot_features = []

        for feature in record.features:
            if feature.qualifiers['type'] == 'strand' or feature.qualifiers['type'] == 'helix' or feature.qualifiers['type'] == 'turn':
                if feature.qualifiers['type'] == 'strand':
                    feature.type = 'beta_strand'
                secondary_structure_features.append(feature)
            elif feature.type == 'cross-link' or feature.type == 'modified residue' or feature.type == 'mutagenesis site' or feature.type == 'sequence variant' or feature.type == 'sequence conflict':
                variant_features.append(feature)
            else:
                other_uniprot_features.append(feature)


        context['uniprot_features'] = record.features

        context['secondary_structure_features'] = secondary_structure_features
        context['variant_features'] = variant_features
        context['other_uniprot_features'] = other_uniprot_features

        variation_dict = {}

      
        
        for rsid in Brca1New.objects.values('rsid').distinct():
            rsid = rsid['rsid']
            if rsid.startswith('rs'):
                variation_dict[rsid] = True
            else:
                continue
            '''
            if not rsid.startswith('rs'):
                continue
            else:
                obj = Brca1New.objects.filter(rsid=rsid)[0]
                pos = obj.codon
                variation_dict[rsid] = pos
            '''


        
        context['variation_dict'] = variation_dict        
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

        context['swissprot_dict'] = swissprot_dict
        
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

        context['alamut_pd1_dict'] = alamut_pd1_dict

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

        context['alamut_pd2_dict'] = alamut_pd2_dict


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

        context['alamut_pd3_dict'] = alamut_pd3_dict

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

        context['alamut_pd4_dict'] = alamut_pd4_dict

        if gene_id is not False:
            return render(request,'p3_app/gene_results.html',context)
                  

        if brca1_object.hgmd_pubmed == 'Pubmed':
            hgmd_pubmed_list = brca1_object.hgmd_pubmed_list.split(' ')
        else:
            hgmd_pubmed_list = None

        context['hgmd_pubmed_list'] = hgmd_pubmed_list

        pubmed_dict = {}
        if hgmd_pubmed_list is not None:
            for pmid in hgmd_pubmed_list:
                if pmid in pmid_dict.keys():
                    pubmed_dict[pmid] = pmid_dict[pmid]

        context['pubmed_dict'] = pubmed_dict


        if brca1_object.alamut_siftprediction == '':
            brca1_object.alamut_siftprediction = None

        if '_' in brca1_object.muttaster_prediction:
            brca1_object.muttaster_prediction = brca1_object.muttaster_prediction.replace('_',' ')

        if brca1_object.muttaster_features != '':
            brca1_object.muttaster_features = brca1_object.muttaster_features.split(',')

        ss_img_loc = int(brca1_object.suspect_score)*4
        context['ss_img_loc'] = ss_img_loc

        agvgd_dict = {'C0': 40, 'C15': 92, 'C25':148, 'C35':205,'C45':261,'C55':317,'C65':375} 
        context['agvgd_dict'] = agvgd_dict

        muttaster_model_dict = {'complex_aa':'mutation introducing a premature stop codon','simple_aae':'substitution/insertion/deletion of a single amino acid'}
        context['muttaster_model_dict'] = muttaster_model_dict

        context['brca1_object'] = brca1_object

        '''
        context = {'rsid':rsid, 'brca1_object':brca1_object,'resi_string':resi_string, 'resi_num':resi_num, 'pdb_entry':pdb_entry, 'chr_num':chr_num,'chr_loc':chr_loc, 'pdb_list':pdb_list, 'match_dict':match_dict, 'sequence':sequence, 'hgmd_pubmed_list':hgmd_pubmed_list, 'swissprot_dict':swissprot_dict, 'alamut_pd1_dict':alamut_pd1_dict,'alamut_pd2_dict':alamut_pd2_dict,'alamut_pd3_dict':alamut_pd3_dict,
'alamut_pd4_dict':alamut_pd4_dict,'agvgd_dict':agvgd_dict,
'ss_img_loc':ss_img_loc,'muttaster_model_dict':muttaster_model_dict, 
'pubmed_dict':pubmed_dict, 'gene_dict':gene_dict, 'protein_id':protein_id,'aa_change':aa_change}
        '''

        return render(request,'p3_app/results_page2.html',context)

    return render(request,'p3_app/index.html',{})

def thanks(request):
    return render(request,'p3_app/pviz_test.html')

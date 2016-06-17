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
    

        else:
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

    
        if errors:
            if rsid != False:
                which_error = 'rsid'
            else:
                which_error = 'chr'

            return render(request,'p3_app/index.html',{'errors':errors, 'which_error':which_error})

        resi_num = brca1_object.hgvs_prot_code1.split('.')[1][:-1][1:]
        resi_string = 'resi:'+str(resi_num)

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

        pfam_id = 'P38398'

        #create dictionary for uniprot/gene names when all gene names are present

        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, 'static/p3_app/pfam_files/'+pfam_id+'.xml')
        xml_file = open(file_path)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        count = 0
        match_dict = {}

        for child in root.iter('match'):
            type_attr = child.attrib['type']
            acc_attr = child.attrib['accession']
            id_attr = child.attrib['id']

            for grandchild in child.iter('location'):
                start = grandchild.attrib['start']
                end = grandchild.attrib['end']
                match_dict[count] = [type_attr,acc_attr,id_attr,int(start),int(end)]
                count += 1

        for seq in root.iter('sequence'):
            sequence = seq.text

        #additional pfam info for mouseover feature

        if brca1_object.hgmd_pubmed == 'Pubmed':
            hgmd_pubmed_list = brca1_object.hgmd_pubmed_list.split(' ')
        else:
            hgmd_pubmed_list = None
                
        #add info for pubmed list - turn into dictionary of citation values

        if brca1_object.muttaster_features != '':
            brca1_object.muttaster_features = brca1_object.muttaster_features.split(',')

        context = {'rsid':rsid, 'brca1_object':brca1_object,'resi_string':resi_string, 'resi_num':resi_num, 'pdb_entry':pdb_entry, 'chr_num':chr_num,'chr_loc':chr_loc, 'pdb_list':pdb_list, 'match_dict':match_dict, 'sequence':sequence, 'hgmd_pubmed_list':hgmd_pubmed_list}
        return render(request,'p3_app/results_page2.html',context)

    return render(request,'p3_app/index.html',{})

def thanks(request):
    return render(request,'p3_app/pviz_test.html')

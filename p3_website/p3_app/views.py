from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect

from .forms import RsForm
from .models import *

def index(request):
    errors = []

    if request.POST:
        rsid = request.POST['rs_id']
        snpsub = request.POST.get('snpsubstitution', '')
        #return HttpResponse('null')
      
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
                errors.append('You have not entered a missense mutation.')

        
        if errors:
            return render(request,'p3_app/index.html',{'errors':errors})

        context = {'rsid':rsid, 'brca1_object':brca1_object}
        return render(request,'p3_app/about.html',context)

    return render(request,'p3_app/index.html',{})

def thanks(request):
    return render(request,'p3_app/index.html')

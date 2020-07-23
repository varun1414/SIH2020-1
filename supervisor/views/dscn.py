from django.shortcuts import render
from login import models as models
from django.http import HttpResponse,HttpResponseRedirect
# from . import main
from . import main
def daily(request):
    dscndaily=[entry for entry in models.Dscndaily.objects.all().values().order_by('-date')]
    for i in dscndaily:
       i['token']=main.encode(request,str(i['p_id']))
       if i['unit_incharge_approval']=="YES":
           i['flag']=1
       elif['unit_incharge_approval']=="NO":
           i['flag']=0
       else:
           i['flag']=9
    
    return render(request,'supervisor/list_details.html',{'context':dscndaily,'name':'Dscndaily'})

def monthly(request):
    dscnmonthly=[entry for entry in models.Dscnmonthly.objects.all().values().order_by('-date')]
    for i in dscnmonthly:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9
    
    return render(request,'supervisor/list_details.html',{'context':dscnmonthly,'name':'Dscnmonthly'})

def weekly(request):
    dscnweekly=[entry for entry in models.Dscnweekly.objects.all().values().order_by('-date')]
    for i in dscnweekly:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9
    
    return render(request,'supervisor/list_details.html',{'context':dscnweekly,'name':'Dscnweekly'})
from django.shortcuts import render
from login import models as models
from django.http import HttpResponse,HttpResponseRedirect
from . import main
def daily(request):
    cdvordaily=[entry for entry in models.Cdvordaily.objects.all().values().order_by('-date')]
    for i in cdvordaily:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9

    return render(request,'supervisor/list_details.html',{'context':cdvordaily,'name':'Cdvordaily'}) 

def weekly(request):
    cdvorweekly=[entry for entry in models.Cdvorweekly.objects.all().values().order_by('-date')]
    for i in cdvorweekly:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9

    return render(request,'supervisor/list_details.html',{'context':cdvorweekly,'name':'Cdvorweekly'})         

def monthly(request):
    cdvormonthly=[entry for entry in models.Cdvormonthly.objects.all().values().order_by('-date')]
    for i in cdvormonthly:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9
    
    return render(request,'supervisor/list_details.html',{'context':cdvormonthly,'name':'Cdvormonthly'})
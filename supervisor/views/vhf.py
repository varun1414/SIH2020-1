from django.shortcuts import render
from login import models as models
from django.http import HttpResponse,HttpResponseRedirect
from . import main
def daily(request):
    vhfdaily=[entry for entry in models.Vhfdaily.objects.all().values().order_by('-date')]
    for i in vhfdaily:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9
    return render(request,'supervisor/list_details.html',{'context':vhfdaily,'name':'Vhfdaily'})


# def monthly(request):
#     vhfmonthly=[entry for entry in models.vhfmonthly.objects.all().values().order_by('-date')]
#     return render(request,'supervisor/monthly_details.html',{'context':vhfmonthly,'name':'vhfmonthly'}) 
def weekly(request):
    vhfweekly=[entry for entry in models.Vhfweekly.objects.all().values().order_by('-date')]
    for i in vhfweekly:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9
    
    return render(request,'supervisor/list_details.html',{'context':vhfweekly,'name':'Vhfweekly'})
def monthly(request):
    vhfmonthly=[entry for entry in models.Vhfmonthly.objects.all().values().order_by('-date')]
    for i in vhfmonthly:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9
    
    return render(request,'supervisor/list_details.html',{'context':vhfmonthly,'name':'Vhfmonthly'})
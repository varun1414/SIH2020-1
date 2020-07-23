from django.shortcuts import render
from login import models as models
from django.http import HttpResponse,HttpResponseRedirect
from . import main
def daily(request):
    scctvdaily=[entry for entry in models.Scctvdaily.objects.all().values().order_by('-date')]
    for i in scctvdaily:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9
    return render(request,'supervisor/list_details.html',{'context':scctvdaily,'name':'Scctvdaily'})


def monthly(request):
    scctvmonthly=[entry for entry in models.Scctvmonthly.objects.all().values().order_by('-date')]
    for i in scctvmonthly:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9
    
    return render(request,'supervisor/list_details.html',{'context':scctvmonthly,'name':'Scctvmonthly'})

def weekly(request):
    scctvweekly=[entry for entry in models.Scctvweekly.objects.all().values().order_by('-date')]
    for i in scctvweekly:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9
    
    return render(request,'supervisor/list_details.html',{'context':scctvweekly,'name':'Scctvweekly'})
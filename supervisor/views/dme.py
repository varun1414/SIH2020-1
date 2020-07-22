from django.shortcuts import render
from login import models as models
from django.http import HttpResponse,HttpResponseRedirect
from . import main
def daily(request):
    dmedaily=[entry for entry in models.Dmedaily.objects.all().values().order_by('-date')]
    for i in dmedaily:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9
    return render(request,'supervisor/list_details.html',{'context':dmedaily,'name':'Dmedaily'})

def monthly(request):
    dmemonthly=[entry for entry in models.Dmemonthly.objects.all().values().order_by('-date')]
    for i in dmemonthly:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9
    
    return render(request,'supervisor/list_details.html',{'context':dmemonthly,'name':'Dmemonthly'})
    
    
def weekly(request):
    dmeweekly=[entry for entry in models.Dmeweekly.objects.all().values().order_by('-date')]
    for i in dmeweekly:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9
    return render(request,'supervisor/list_details.html',{'context':dmeweekly,'name':'Dmeweekly'})
    return 0
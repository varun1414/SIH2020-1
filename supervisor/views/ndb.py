from django.shortcuts import render
from login import models as models
from django.http import HttpResponse,HttpResponseRedirect
from . import main
def daily(request):
    ndbdaily=[entry for entry in models.Ndbdaily.objects.all().values().order_by('-date')]
    for i in ndbdaily:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9
    return render(request,'supervisor/list_details.html',{'context':ndbdaily,'name':'Ndbdaily'})
def monthly(request):
   ndbmonthly=[entry for entry in models.Ndbmonthly.objects.all().values().order_by('-date')]
   for i in ndbmonthly:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9
    
   return render(request,'supervisor/list_details.html',{'context':Ndbmonthly,'name':'Ndbmonthly'})

def weekly(request):
    ndbweekly=[entry for entry in models.Ndbweekly.objects.all().values().order_by('-date')]
    for i in ndbweekly:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9
    
    return render(request,'supervisor/list_details.html',{'context':ndbweekly,'name':'Ndbweekly'})
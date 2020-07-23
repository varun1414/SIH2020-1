from django.shortcuts import render
from login import models as models
from django.http import HttpResponse,HttpResponseRedirect
from . import main

def daily(request):
    datisdaily=[entry for entry in models.Datisdaily.objects.all().values().order_by('-date')]
   #  sorted(datisdaily,key=itemgetter('date'),reverse=True)
    for i in datisdaily:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9
    return render(request,'supervisor/list_details.html',{'context':datisdaily,'name':'Datisdaily'})


# def monthly(request):
#     Datismonthly=[entry for entry in models.Datismonthly.objects.all().values()order_by('-date')]
#     return render(request,'supervisor/monthly_details.html',{'context':Datismonthly,'name':'Datismonthly'}) 
def weekly(request):
    Datisweekly=[entry for entry in models.Datisweekly.objects.all().values().order_by('-date')]
    for i in Datisweekly:
        i['token']=main.encode(request,str(i['p_id']))
        if i['unit_incharge_approval']=="YES":
           i['flag']=1
        elif['unit_incharge_approval']=="NO":
           i['flag']=0
        else:
           i['flag']=9
    
    return render(request,'supervisor/list_details.html',{'context':Datisweekly,'name':'Datisweekly'})
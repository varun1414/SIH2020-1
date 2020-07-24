from django.shortcuts import render
import collections
import re
from datetime import date,datetime,timedelta
from django.db import connection
from cryptography.fernet import Fernet as frt
from django.db.models import Count
from supervisor.views import main
from operator import itemgetter
from django.db.models import Q
from itertools import groupby,chain
# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from login import models
from django.db import connection
from django.db.models import Q

def calendar(request):
    year= date.today().year
    month=date.today().month
    startdate=str(year)+"-01-01"
    if month == 1 or month == 2 or month == 3:
        startdate = datetime.strptime(startdate,'%Y-%m-%d').date()
        enddate=str(year)+"-04-01"
        enddate = datetime.strptime(enddate,'%Y-%m-%d').date()
        Datisdaily=[entry for entry in models.Datisdaily.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Datisdaily:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update({"type":"DatD"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
            Datisweekly=[entry for entry in models.Datisweekly.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Datisweekly:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"DatW"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
    elif month == 4 or month == 5 or month == 6:
        startdate=str(year)+"-03-31"
        startdate = datetime.strptime(startdate,'%Y-%m-%d').date()
        enddate=str(year)+"-07-01"
        enddate = datetime.strptime(enddate,'%Y-%m-%d').date()
        Datisdaily=[entry for entry in models.Datisdaily.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Datisdaily:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"DatD"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
            Datisweekly=[entry for entry in models.Datisweekly.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Datisweekly:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"DatW"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
    
    elif month == 7 or month == 8 or month == 9 :
        startdate=str(year)+"-06-30"
        startdate = datetime.strptime(startdate,'%Y-%m-%d').date()
        enddate=str(year)+"-10-01"
        enddate = datetime.strptime(enddate,'%Y-%m-%d').date()
        Datisdaily=[entry for entry in models.Datisdaily.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Datisdaily:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"DatD"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
            Datisweekly=[entry for entry in models.Datisweekly.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Datisweekly:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"DatW"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
    else :
        startdate=str(year)+"-09-31"
        startdate = datetime.strptime(startdate,'%Y-%m-%d').date()
        enddate=str(year)+"-12-31"
        enddate = datetime.strptime(enddate,'%Y-%m-%d').date()
        Datisdaily=[entry for entry in models.Datisdaily.objects.values().filter(date__gt=startdate,date__lte=enddate)]
        for item in Datisdaily:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"DatD"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
            Datisweekly=[entry for entry in models.Datisweekly.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Datisweekly:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"DatW"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
    
    com=Datisdaily+[i for i in Datisweekly]
    return render(request,'dgm/calendar.html',{'com':com})

def calendarn(request):
    year= date.today().year
    month=date.today().month
    startdate=str(year)+"-01-01"
    if month == 1 or month == 2 or month == 3:
        startdate = datetime.strptime(startdate,'%Y-%m-%d').date()
        enddate=str(year)+"-04-01"
        enddate = datetime.strptime(enddate,'%Y-%m-%d').date()
        Cdvordaily=[entry for entry in models.Cdvordaily.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Cdvordaily:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"CdvorD"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
        Cdvorweekly=[entry for entry in models.Cdvorweekly.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Cdvorweekly:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"CdvorW"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
    elif month == 4 or month == 5 or month == 6:
        startdate=str(year)+"-03-31"
        startdate = datetime.strptime(startdate,'%Y-%m-%d').date()
        enddate=str(year)+"-07-01"
        enddate = datetime.strptime(enddate,'%Y-%m-%d').date()
        Cdvordaily=[entry for entry in models.Cdvordaily.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Cdvordaily:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"CdvorD"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
        Cdvorweekly=[entry for entry in models.Cdvorweekly.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Cdvorweekly:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"CdvorW"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
    
    elif month == 7 or month == 8 or month == 9 :
        startdate=str(year)+"-06-30"
        startdate = datetime.strptime(startdate,'%Y-%m-%d').date()
        enddate=str(year)+"-10-01"
        enddate = datetime.strptime(enddate,'%Y-%m-%d').date()
        Cdvordaily=[entry for entry in models.Cdvordaily.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Cdvordaily:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"CdvorD"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
        Cdvorweekly=[entry for entry in models.Cdvorweekly.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Cdvorweekly:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"CdvorW"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
    else :
        startdate=str(year)+"-09-31"
        startdate = datetime.strptime(startdate,'%Y-%m-%d').date()
        enddate=str(year)+"-12-31"
        enddate = datetime.strptime(enddate,'%Y-%m-%d').date()
        Cdvordaily=[entry for entry in models.Cdvordaily.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Cdvordaily:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"CdvorD"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
        Cdvorweekly=[entry for entry in models.Cdvorweekly.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Cdvorweekly:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"CdvorW"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
    
    com=Cdvordaily+[i for i in Cdvorweekly]
    return render(request,'dgm/calendar.html',{'com':com})

def calendars(request):
    year= date.today().year
    month=date.today().month
    startdate=str(year)+"-01-01"
    if month == 1 or month == 2 or month == 3:
        startdate = datetime.strptime(startdate,'%Y-%m-%d').date()
        enddate=str(year)+"-04-01"
        enddate = datetime.strptime(enddate,'%Y-%m-%d').date()
        Scctvdaily=[entry for entry in models.Scctvdaily.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Scctvdaily:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"ScctvD"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
        Scctvweekly=[entry for entry in models.Scctvweekly.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Scctvweekly:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"ScctvW"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
    elif month == 4 or month == 5 or month == 6:
        startdate=str(year)+"-03-31"
        startdate = datetime.strptime(startdate,'%Y-%m-%d').date()
        enddate=str(year)+"-07-01"
        enddate = datetime.strptime(enddate,'%Y-%m-%d').date()
        Scctvdaily=[entry for entry in models.Scctvdaily.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Scctvdaily:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"ScctvD"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
        Scctvweekly=[entry for entry in models.Scctvweekly.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Scctvweekly:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"ScctvW"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
    
    elif month == 7 or month == 8 or month == 9 :
        startdate=str(year)+"-06-30"
        startdate = datetime.strptime(startdate,'%Y-%m-%d').date()
        enddate=str(year)+"-10-01"
        enddate = datetime.strptime(enddate,'%Y-%m-%d').date()
        Scctvdaily=[entry for entry in models.Scctvdaily.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Scctvdaily:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"ScctvD"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
        Scctvweekly=[entry for entry in models.Scctvweekly.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Scctvweekly:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"ScctvW"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
    else :
        startdate=str(year)+"-09-31"
        startdate = datetime.strptime(startdate,'%Y-%m-%d').date()
        enddate=str(year)+"-12-31"
        enddate = datetime.strptime(enddate,'%Y-%m-%d').date()
        Scctvdaily=[entry for entry in models.Scctvdaily.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Scctvdaily:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"ScctvD"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
        Scctvweekly=[entry for entry in models.Scctvweekly.objects.values().filter(date__gt=startdate,date__lt=enddate)]
        for item in Scctvweekly:
            temp = item['date']
            y = temp.year
            m = temp.month
            d = temp.day
            item.update( {"type":"ScctvW"})
            item.update({"y":y})
            item.update({"m":m})
            item.update({"d":d})
    
    com=Scctvdaily+[i for i in Scctvweekly]
    return render(request,'dgm/calendar.html',{'com':com})

def communication(request):
    # supdetails = models.Supervisor.objects.all().filter(dept='C')
    supdetails,eng=comdet()
    return render(request,'dgm/dashboardc.html',{'supdetails':supdetails,'eng':eng,'searched':None})
    
def surv(request):
    supdetails,eng=surdet()
    return render(request,'dgm/dashboards.html',{'supdetails':supdetails,'eng':eng,'searched':None})

def nav(request):
    supdetails,eng=navdet()
   
    return render(request,'dgm/dashboardn.html',{'supdetails':supdetails,'eng':eng,'searched':None})

def homev(request,uid):
    labels = []
    data = []
    
    request.session['type']='d'
    request.session['uid']=uid
    dgm= models.Dgm.objects.all().filter(dgm_id=uid).values()
    emp_id = uid
    head= models.Head.objects.all()

    # comlist = models.DgmReports.objects.filter(Q(r_id=1) | Q(r_id=2) | Q(r_id=3) | Q(r_id=4) | Q(r_id=5) | Q(r_id=6) | Q(r_id=15) |Q(r_id=16) | Q(r_id=17) | Q(r_id=30) |Q(r_id=31) |Q(r_id=32))
    
    # for datisd in comlist:
    #     com_labels.append(datisd.r_status)
    #     com_data.append(datisd.r_count)
    today=datetime.now().strftime('%Y-%m-%d')
    today=datetime.strptime(today, "%Y-%m-%d")

    month=today.month
    # print(type(month))
    year=today.year
    day=today.day
    if month >=1 and month <=3:
        lmonth=1
    elif month>=4 and month<=6:
        lmonth=4
    else:
        lmonth=7
    fdate=datetime(year, lmonth , 1).date()
    print(fdate)
    print(today.date())
    Cdvordaily=[entry for entry in models.Cdvordaily.objects.filter(Q( date__gte= fdate ) & Q(date__lte=today)).values().order_by('-date')]
    
    for item in Cdvordaily:
            item.update( {"type":"Cdvordaily"})
    Cdvorweekly=[entry for entry in models.Cdvorweekly.objects.filter(Q( date__gte = fdate ) & Q(date__lte=today)).values().order_by('-date')]
    # print(Cdvorweekly)
    for item in Cdvorweekly:
            item.update( {"type":"Cdvorweekly"})
    
    
    
    Cdvormonthly=[entry for entry in models.Cdvormonthly.objects.filter( Q(date__gte= fdate)  &  Q(date__lte= today.date()) ).values()]
    # print(Cdvormonthly)
    for item in Cdvormonthly:
            item.update( {"type":"Cdvormonthly"})        
    
    
    com=Cdvordaily+[i for i in Cdvorweekly]+[i for i in Cdvormonthly]
    com=sorted(com,key=itemgetter('date'))
    pending=[]
    completed=[]
    error=[]
    submit=0
    approve=0
    napprove=0
    for i in com:
        if i['remarks'] != '---Report not submitted---':
            # submitted.append(i)
            submit=submit+1
        if i['unit_incharge_approval'] == 'YES':    
            approve=approve+1
        elif i['unit_incharge_approval'] == 'NO':
            napprove=napprove+1

    # pcount=collections.Counter([d['date'] for d in pending])
    # pend=compute(request,pcount)
    # ccount=collections.Counter([d['date'] for d in completed])
    # comp=compute(request,ccount)
    # ecount=collections.Counter([d['date'] for d in error])
    # err=compute(request,ecount)

    Cdvordaily=[entry for entry in models.Cdvordlogs.objects.filter(Q( date__gte= fdate ) & Q(date__lte=today) & Q(remarks= 'Parameters normal at the first submit!')).values('remarks').annotate(dcount=Count('remarks'))]
    # print(Cdvordaily)
    # for item in Cdvordaily:
    #         item.update( {"type":"Cdvordaily"})
    Cdvorweekly=[entry for entry in models.Cdvorwlogs.objects.filter(Q( date__gte = fdate ) & Q(date__lte=today) & Q(remarks= 'Parameters normal at the first submit!')).values('remarks').annotate(dcount=Count('remarks'))]
    # print(Cdvorweekly)
    if Cdvorweekly == []:
        Cdvorweekly.append({'dcount':0})
    # for item in Cdvorweekly:
    #         item.update( {"type":"Cdvorweekly"})
    
    
    
    Cdvormonthly=[entry for entry in models.Cdvormlogs.objects.filter( Q(date__gte= fdate)  &  Q(date__lte= today.date())  & Q(remarks= 'Parameters normal at the first submit!')).values('remarks').annotate(dcount=Count('remarks'))]
    # print(Cdvormonthly)
    if Cdvormonthly == []:
        Cdvormonthly.append({'dcount':0})

    # for item in Cdvormonthly:
            # item.update( {"type":"Cdvormonthly"})        
    
    
    log=Cdvordaily[0]['dcount']+Cdvorweekly[0]['dcount']+ Cdvormonthly[0]['dcount']
    # log=sorted(log,key=itemgetter('date'))
    # print(log)
    firsttime_per=(float(log)/submit)*100
    sumd=sumw=summ=0
    
    Cdvordaily=[entry for entry in models.Cdvordlogs.objects.filter(Q( date__gte= fdate ) & Q(date__lte=today) & ~Q(remarks = 'Parameters normal at the first submit!') & ~Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    # print(Cdvordaily)
    # for item in Cdvordaily:
    #         sumd=sumd+item['dcount']
    Cdvorweekly=[entry for entry in models.Cdvorwlogs.objects.filter(Q( date__gte = fdate ) & Q(date__lte=today) & ~Q(remarks = 'Parameters normal at the first submit!') & ~Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    # print(Cdvorweekly)
    # if Cdvorweekly == []:
    #     Cdvorweekly.append({'dcount':0})
    # for item in Cdvorweekly:
    #         sumw=sumw+item['dcount']
    
    
    
    Cdvormonthly=[entry for entry in models.Cdvormlogs.objects.filter( Q(date__gte= fdate)  &  Q(date__lte= today.date()) & ~Q(remarks = 'Parameters normal at the first submit!') & ~Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    # print(Cdvormonthly)
    # if Cdvormonthly == []:
    #     Cdvormonthly.append({'dcount':0})
    # for item in Cdvormonthly:
    #         summ=summ+item['dcount']
    

    maintain=len(Cdvormonthly)+len(Cdvordaily)+len(Cdvorweekly)
   
    
    sumd=sumw=summ=0
    # surlist = models.DgmReports.objects.filter(Q(r_id=10) | Q(r_id=11) | Q(r_id=14) | Q(r_id=21) | Q(r_id=22) | Q(r_id=23) | Q(r_id=27) |Q(r_id=28) | Q(r_id=) | Q(r_id=30) |Q(r_id=31) |Q(r_id=32))
    
    # for datisd in comlist:
    #     com_labels.append(datisd.r_status)
    #     com_data.append(datisd.r_count)
    
    # print(pend[0][0])

    Cdvordaily=[entry for entry in models.Cdvordlogs.objects.filter(Q( date__gte= fdate ) & Q(date__lte=today) & Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    # print(Cdvordaily)
    for item in Cdvordaily:
            sumd=sumd+item['dcount']
    Cdvorweekly=[entry for entry in models.Cdvorwlogs.objects.filter(Q( date__gte = fdate ) & Q(date__lte=today) & Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    # print(Cdvorweekly)
    if Cdvorweekly == []:
        Cdvorweekly.append({'dcount':0})
    for item in Cdvorweekly:
            sumw=sumw+item['dcount']
    
    
    
    Cdvormonthly=[entry for entry in models.Cdvormlogs.objects.filter( Q(date__gte= fdate)  &  Q(date__lte= today.date()) & Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    # print(Cdvormonthly)
    if Cdvormonthly == []:
        Cdvormonthly.append({'dcount':0})
    for item in Cdvormonthly:
            summ=summ+item['dcount']

    rep=sumd+sumw+summ
    maintain_per=(float(maintain)/(maintain + log +rep))*100
    # log=log-rep
    nsubmit=len(com)-submit
    # print(maintain)
    




    Scctvdaily=[entry for entry in models.Scctvdaily.objects.filter(Q( date__gte= fdate ) & Q(date__lte=today)).values().order_by('-date')]
    
    for item in Scctvdaily:
            item.update( {"type":"Scctvdaily"})
    Scctvweekly=[entry for entry in models.Scctvweekly.objects.filter(Q( date__gte = fdate ) & Q(date__lte=today)).values().order_by('-date')]
    # print(Scctvweekly)
    for item in Scctvweekly:
            item.update( {"type":"Scctvweekly"})
    
    
    
    Scctvmonthly=[entry for entry in models.Scctvmonthly.objects.filter( Q(date__gte= fdate)  &  Q(date__lte= today.date()) ).values()]
    # print(Scctvmonthly)
    for item in Scctvmonthly:
            item.update( {"type":"Scctvmonthly"})        
    
    
    com=Scctvdaily+[i for i in Scctvweekly]+[i for i in Scctvmonthly]
    com=sorted(com,key=itemgetter('date'))
    pending=[]
    completed=[]
    error=[]
    scctvsubmit=0
    scctvapprove=0
    nscctvapprove=0
    for i in com:
        if i['remarks'] != '---Report not submitted---':
            # scctvsubmitted.append(i)
            
            scctvsubmit=scctvsubmit+1
        if i['unit_incharge_approval'] == 'YES':    
            scctvapprove=scctvapprove+1
        elif i['unit_incharge_approval'] == 'NO':
            nscctvapprove=nscctvapprove+1

    # pcount=collections.Counter([d['date'] for d in pending])
    # pend=compute(request,pcount)
    # ccount=collections.Counter([d['date'] for d in completed])
    # comp=compute(request,ccount)
    # ecount=collections.Counter([d['date'] for d in error])
    # err=compute(request,ecount)

    Scctvdaily=[entry for entry in models.Scctvdlogs.objects.filter(Q( date__gte= fdate ) & Q(date__lte=today) & Q(remarks= 'Parameters normal at the first submit!')).values('remarks').annotate(dcount=Count('remarks'))]
    # print(Scctvdaily)
    # for item in Scctvdaily:
    #         item.update( {"type":"Scctvdaily"})
    if Scctvdaily == []:
        Scctvdaily.append({'dcount':0})
    Scctvweekly=[entry for entry in models.Scctvwlogs.objects.filter(Q( date__gte = fdate ) & Q(date__lte=today) & Q(remarks= 'Parameters normal at the first submit!')).values('remarks').annotate(dcount=Count('remarks'))]
    # print(Scctvweekly)
    if Scctvweekly == []:
        Scctvweekly.append({'dcount':0})
    # for item in Scctvweekly:
    #         item.update( {"type":"Scctvweekly"})
    
    
    
    Scctvmonthly=[entry for entry in models.Scctvmlogs.objects.filter( Q(date__gte= fdate)  &  Q(date__lte= today.date())  & Q(remarks= 'Parameters normal at the first submit!')).values('remarks').annotate(dcount=Count('remarks'))]
    # print(Scctvmonthly)
    if Scctvmonthly == []:
        Scctvmonthly.append({'dcount':0})

    # for item in Scctvmonthly:
            # item.update( {"type":"Scctvmonthly"})        
    
    
    scctvlog=Scctvdaily[0]['dcount']+Scctvweekly[0]['dcount']+ Scctvmonthly[0]['dcount']
    # log=sorted(log,key=itemgetter('date'))
    # print(log)
    scctvfirsttime_per=(float(scctvlog)/scctvsubmit)*100
    sumd=sumw=summ=0
    
    Scctvdaily=[entry for entry in models.Scctvdlogs.objects.filter(Q( date__gte= fdate ) & Q(date__lte=today) & ~Q(remarks = 'Parameters normal at the first submit!') & ~Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    # print(Scctvdaily)
    # for item in Scctvdaily:
    #         sumd=sumd+item['dcount']
    Scctvweekly=[entry for entry in models.Scctvwlogs.objects.filter(Q( date__gte = fdate ) & Q(date__lte=today) & ~Q(remarks = 'Parameters normal at the first submit!') & ~Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    # print(Scctvweekly)
    # if Scctvweekly == []:
    #     Scctvweekly.append({'dcount':0})
    # for item in Scctvweekly:
    #         sumw=sumw+item['dcount']
    
    
    
    Scctvmonthly=[entry for entry in models.Scctvmlogs.objects.filter( Q(date__gte= fdate)  &  Q(date__lte= today.date()) & ~Q(remarks = 'Parameters normal at the first submit!') & ~Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    # print(Scctvmonthly)
    # if Scctvmonthly == []:
    #     Scctvmonthly.append({'dcount':0})
    # for item in Scctvmonthly:
    #         summ=summ+item['dcount']
    

    scctvmaintain=len(Scctvmonthly)+len(Scctvdaily)+len(Scctvweekly)
   
    
    sumd=sumw=summ=0
    # surlist = models.DgmReports.objects.filter(Q(r_id=10) | Q(r_id=11) | Q(r_id=14) | Q(r_id=21) | Q(r_id=22) | Q(r_id=23) | Q(r_id=27) |Q(r_id=28) | Q(r_id=) | Q(r_id=30) |Q(r_id=31) |Q(r_id=32))
    
    # for datisd in comlist:
    #     com_labels.append(datisd.r_status)
    #     com_data.append(datisd.r_count)
    
    # print(pend[0][0])

    Scctvdaily=[entry for entry in models.Scctvdlogs.objects.filter(Q( date__gte= fdate ) & Q(date__lte=today) & Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    print(Scctvdaily)
    for item in Scctvdaily:
            sumd=sumd+item['dcount']
    Scctvweekly=[entry for entry in models.Scctvwlogs.objects.filter(Q( date__gte = fdate ) & Q(date__lte=today) & Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    print(Scctvweekly)
    if Scctvweekly == []:
        Scctvweekly.append({'dcount':0})
    for item in Scctvweekly:
            sumw=sumw+item['dcount']
    
    
    
    Scctvmonthly=[entry for entry in models.Scctvmlogs.objects.filter( Q(date__gte= fdate)  &  Q(date__lte= today.date()) & Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    # print(Scctvmonthly)
    if Scctvmonthly == []:
        Scctvmonthly.append({'dcount':0})
    for item in Scctvmonthly:
            summ=summ+item['dcount']

    scctvrep=sumd+sumw+summ
    scctvmaintain_per=(float(scctvmaintain)/(scctvmaintain + scctvlog +scctvrep))*100
    # log=log-rep
    nscctvsubmit=len(com)-scctvsubmit
    print(scctvmaintain)

    
    
    
    
    
    Datisdaily=[entry for entry in models.Datisdaily.objects.filter(Q( date__gte= fdate ) & Q(date__lte=today)).values().order_by('-date')]
    
    for item in Datisdaily:
            item.update( {"type":"Datisdaily"})
    Dscndaily=[entry for entry in models.Dscndaily.objects.filter(Q( date__gte= fdate ) & Q(date__lte=today)).values().order_by('-date')]
    
    for item in Datisdaily:
            item.update( {"type":"Dscndaily"})
    Datisweekly=[entry for entry in models.Datisweekly.objects.filter(Q( date__gte = fdate ) & Q(date__lte=today)).values().order_by('-date')]
    # print(Datisweekly)
    for item in Datisweekly:
            item.update( {"type":"Datisweekly"})
    
    
    
    Dscnmonthly=[entry for entry in models.Dscnmonthly.objects.filter( Q(date__gte= fdate)  &  Q(date__lte= today.date()) ).values()]
    # print(Dscnmonthly)
    for item in Dscnmonthly:
            item.update( {"type":"Dscnmonthly"})        
    
    
    com=Datisdaily+[i for i in Datisweekly]+[i for i in Dscnmonthly]+[i for i in Dscndaily]
    com=sorted(com,key=itemgetter('date'))
    pending=[]
    completed=[]
    error=[]
    comsubmit=0
    comapprove=0
    ncomapprove=0
    for i in com:
        if i['remarks'] != '---Report not submitted---':
            # comsubmitted.append(i)
            
            comsubmit=comsubmit+1
        if i['unit_incharge_approval'] == 'YES':    
            comapprove=comapprove+1
        elif i['unit_incharge_approval'] == 'NO':
            ncomapprove=ncomapprove+1

    # pcount=collections.Counter([d['date'] for d in pending])
    # pend=compute(request,pcount)
    # ccount=collections.Counter([d['date'] for d in completed])
    # comp=compute(request,ccount)
    # ecount=collections.Counter([d['date'] for d in error])
    # err=compute(request,ecount)

    Datisdaily=[entry for entry in models.Datisdlogs.objects.filter(Q( date__gte= fdate ) & Q(date__lte=today) & Q(remarks= 'Parameters normal at the first submit!')).values('remarks').annotate(dcount=Count('remarks'))]
    # print(Datisdaily)
    # for item in Datisdaily:
    #         item.update( {"type":"Datisdaily"})
    if Datisdaily == []:
        Datisdaily.append({'dcount':0})
    Datisweekly=[entry for entry in models.Datiswlogs.objects.filter(Q( date__gte = fdate ) & Q(date__lte=today) & Q(remarks= 'Parameters normal at the first submit!')).values('remarks').annotate(dcount=Count('remarks'))]
    # print(Datisweekly)
    if Datisweekly == []:
        Datisweekly.append({'dcount':0})
    # for item in Datisweekly:
    #         item.update( {"type":"Datisweekly"})
    
    
    
    Dscnmonthly=[entry for entry in models.Dscnmlogs.objects.filter( Q(date__gte= fdate)  &  Q(date__lte= today.date())  & Q(remarks= 'Parameters normal at the first submit!')).values('remarks').annotate(dcount=Count('remarks'))]
    # print(Dscnmonthly)
    if Dscnmonthly == []:
        Dscnmonthly.append({'dcount':0})

    # for item in Dscnmonthly:
            # item.update( {"type":"Dscnmonthly"})        
    
    
    comlog=Datisdaily[0]['dcount']+Datisweekly[0]['dcount']+ Dscnmonthly[0]['dcount']
    # log=sorted(log,key=itemgetter('date'))
    # print(log)
    comfirsttime_per=(float(comlog)/comsubmit)*100
    sumd=sumw=summ=0
    
    Datisdaily=[entry for entry in models.Datisdlogs.objects.filter(Q( date__gte= fdate ) & Q(date__lte=today) & ~Q(remarks = 'Parameters normal at the first submit!') & ~Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    # print(Datisdaily)
    # for item in Datisdaily:
    #         sumd=sumd+item['dcount']
    Datisweekly=[entry for entry in models.Datiswlogs.objects.filter(Q( date__gte = fdate ) & Q(date__lte=today) & ~Q(remarks = 'Parameters normal at the first submit!') & ~Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    # print(Datisweekly)
    # if Datisweekly == []:
    #     Datisweekly.append({'dcount':0})
    # for item in Datisweekly:
    #         sumw=sumw+item['dcount']
    
    
    
    Dscnmonthly=[entry for entry in models.Dscnmlogs.objects.filter( Q(date__gte= fdate)  &  Q(date__lte= today.date()) & ~Q(remarks = 'Parameters normal at the first submit!') & ~Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    # print(Dscnmonthly)
    # if Dscnmonthly == []:
    #     Dscnmonthly.append({'dcount':0})
    # for item in Dscnmonthly:
    #         summ=summ+item['dcount']
    

    commaintain=len(Dscnmonthly)+len(Datisdaily)+len(Datisweekly)
   
    
    sumd=sumw=summ=0
    # surlist = models.DgmReports.objects.filter(Q(r_id=10) | Q(r_id=11) | Q(r_id=14) | Q(r_id=21) | Q(r_id=22) | Q(r_id=23) | Q(r_id=27) |Q(r_id=28) | Q(r_id=) | Q(r_id=30) |Q(r_id=31) |Q(r_id=32))
    
    # for datisd in comlist:
    #     com_labels.append(datisd.r_status)
    #     com_data.append(datisd.r_count)
    
    # print(pend[0][0])

    Datisdaily=[entry for entry in models.Datisdlogs.objects.filter(Q( date__gte= fdate ) & Q(date__lte=today) & Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    print(Datisdaily)
    for item in Datisdaily:
            sumd=sumd+item['dcount']
    Datisweekly=[entry for entry in models.Datiswlogs.objects.filter(Q( date__gte = fdate ) & Q(date__lte=today) & Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    print(Datisweekly)
    if Datisweekly == []:
        Datisweekly.append({'dcount':0})
    for item in Datisweekly:
            sumw=sumw+item['dcount']
    
    
    
    Dscnmonthly=[entry for entry in models.Dscnmlogs.objects.filter( Q(date__gte= fdate)  &  Q(date__lte= today.date()) & Q(remarks = 'Report not submitted')).values('p_id').annotate(dcount=Count('p_id'))]
    # print(Dscnmonthly)
    if Dscnmonthly == []:
        Dscnmonthly.append({'dcount':0})
    for item in Dscnmonthly:
            summ=summ+item['dcount']

    comrep=sumd+sumw+summ
    commaintain_per=(float(commaintain)/(commaintain + comlog +comrep))*100
    # log=log-rep
    ncomsubmit=len(com)-comsubmit
    print(commaintain)






    return render(request, 'dgm/dgm.html', {
        'dgmdet':dgm,
        'navsubmit':submit,
        'navapprove':approve,
        'navnapprove':napprove,
        'navpend':nsubmit,
        
        'navmaintain_per':maintain_per,
        'navfirst':firsttime_per,
        'navlog':log,
        'navmaintain':maintain,
        'navrep':rep,
        'scctvsubmit':scctvsubmit,
        'scctvapprove':scctvapprove,
        'scctvnapprove':nscctvapprove,
        'scctvpend':nscctvsubmit,
        
        'scctvmaintain_per':scctvmaintain_per,
        'scctvfirst':scctvfirsttime_per,
        'scctvlog':scctvlog,
        'scctvmaintain':scctvmaintain,
        'scctvrep':scctvrep,
        
        
        'comsubmit':comsubmit,
        'comapprove':comapprove,
        'comnapprove':ncomapprove,
        'compend':ncomsubmit,
        
        'commaintain_per':commaintain_per,
        'comfirst':comfirsttime_per,
        'comlog':comlog,
        'commaintain':commaintain,
        'comrep':comrep,
        

        # 'p_labels':pend[0][2],
        # 'p_data': pend[1][2],
        # 'c_labels':comp[0][2],
        # 'c_data': comp[1][2],
        # 'e_labels':err[0][2],
        # 'e_data': err[1][2],
        'id':uid,
        'headdet':head,
        # 'nav_labels':nav_labels,
        # 'nav_data': nav_data,
     })



def dgmhome(request,id):
	today = datetime.now().strftime('%d/%m/%Y')
    #request.session['type']='d'
    #request.session['uid']=uid
	return render(request,'./dgm/dgm.html')



def navigation(request):

    a_id=models.Dgm.objects.all().filter(a_id=1).values('a_id')[0]['a_id']
    cdvordaily=[entry for entry in models.Cdvordaily.objects.filter(a_id=a_id).values().order_by('-date')]
    for i in cdvordaily:
        i.update({'type':'Cdvordaily'})
    cdvorweekly=[entry for entry in models.Cdvorweekly.objects.filter(a_id=a_id).values().order_by('-date')]
    for i in cdvorweekly:
        i.update({'type':'Cdvorweekly'})
    cdvormonthly=[entry for entry in models.Cdvormonthly.objects.filter(a_id=a_id).values().order_by('-date')]
    for i in cdvormonthly:
        i.update({'type':'Cdvormonthly'})
    
    com=cdvordaily+[i for i in cdvorweekly]+[i for i in cdvormonthly]

    com=sorted(com,key=itemgetter('date'),reverse=True)
    p_count=0
    comp_count=0
    compwe_count=0
    # print(type(com))
    # eng=[entry for entry in models.Engineer.objects.filter(dgm_id=uid).values()]
    for i in com:
        if i['status']=='com':
            p_count=p_count+1
        elif i['status']=='COMPLETED':
            comp_count=comp_count+1
        elif i['status']=='COMPLETED WITH ERRORS':
            compwe_count=compwe_count+1
    print(p_count)
    print(comp_count)
    print(compwe_count)
    for i in com:
            # i.update({'type':'communication'})
            i.update({'token':encode(request,str(i['p_id']))})
    return render(request,'dgm/list_details.html',{'context':com,'name':'Navigation'})


def details(request,id,name):
    id=decode(request,id)
    if request.session.get('type')=='d':
            
        # print(name)
        
        str1='temp=models.'
        str2='.objects.filter(p_id='
        str3=').values()'
        str4='.objects.all('
        que=str1+name+str2+str(id)+str3
        exec(que,globals())
        str1='mrec=models.'
        que=str1+name+str4+str3+".order_by('-date')"
        exec(que,globals())
        #  UNCOMMENT WHEN DONE WITH ALL LOG TABLES
        logname=name+'logs'
        logname=logname.replace('daily','d')
        logname=logname.replace('monthly','m')
        logname=logname.replace('weekly','w')
        logname=logname.replace('yearly','y')
        print(logname)
        name=name[0].lower()+name[1:]
        # # logname=name+'logs'
        str1='logs=models.'
        str2='.objects.filter(p_id='
        str3=').values()'
        request.session['pid']=id
        request.session['name']=name
        que=str1+logname+str2+str(id)+str3+".order_by('-log_id')"
        exec(que,globals())
        # print("logs:")
        # print(logs)
        i=temp[0]
        i['e_token']=encode(request,str(i['emp_id']))
        i['p_token']=encode(request,str(i['p_id']))
        eng=models.Engineer.objects.filter(emp_id=temp[0]['emp_id']).values()
        # print(i)
        # redir='dgm:'+name
        if name =='datisdaily':
            redir='dgm:'+"communication"
            return render(request,'dgm/imp_details.html',{'eng':eng[0],'temp':i,'names':name,'redir':redir,'logs':logs,'mrec':mrec})
        
        elif name == 'datisweekly':
            redir='dgm:'+"communication"
            return render(request,'dgm/impw_details.html',{'eng':eng[0],'temp':i,'names':name,'redir':redir,'logs':logs,'mrec':mrec})    
        
        elif name == 'dscndaily':
            redir='dgm:'+"communication"
            return render(request,'dgm/dscn_imp_details.html',{'eng':eng[0],'temp':i,'names':name,'redir':redir,'logs':logs,'mrec':mrec})    
        elif name == 'dscnmonthly':
            redir='dgm:'+"communication"
            return render(request,'dgm/dscn_impm_details.html',{'eng':eng[0],'temp':i,'names':name,'redir':redir,'logs':logs,'mrec':mrec})    
        
        elif name == 'cdvordaily':
            redir='dgm:'+"navigation"
            return render(request,'dgm/cdvor_imp_details.html',{'eng':eng[0],'temp':i,'names':name,'redir':redir,'logs':logs,'mrec':mrec})    
        elif name == 'cdvormonthly':
            redir='dgm:'+"navigation"
            return render(request,'dgm/cdvor_impm_details.html',{'eng':eng[0],'temp':i,'names':name,'redir':redir,'logs':logs,'mrec':mrec})        
        
        # return render(request,'dgm/imp_details.html',{'temp':i,'names':name})
        elif name == 'cdvorweekly':
            redir='dgm:'+"navigation"
            return render(request,'dgm/cdvor_impw_details.html',{'eng':eng[0],'temp':i,'names':name,'redir':redir,'logs':logs,'mrec':mrec})    
        elif name == 'scctvdaily':
            redir='dgm:'+"surveillance"
            return render(request,'dgm/scctv_imp_details.html',{'eng':eng[0],'temp':i,'names':name,'redir':redir,'logs':logs,'mrec':mrec})    
        elif name == 'scctvmonthly':
            redir='dgm:'+"surveillance"
            return render(request,'dgm/scctv_impm_details.html',{'eng':eng[0],'temp':i,'names':name,'redir':redir,'logs':logs,'mrec':mrec})        
        
        # return render(request,'dgm/imp_details.html',{'temp':i,'names':name})
        elif name == 'scctvweekly':
            redir='dgm:'+"surveillance"
            return render(request,'dgm/scctv_impw_details.html',{'eng':eng[0],'temp':i,'names':name,'redir':redir,'logs':logs,'mrec':mrec}) 

def encode(request,s):

    f=frt(request.session['key'].encode('utf-8'))
    token = f.encrypt(s.encode('utf-8'))
    # print(token.decode('utf-8'))
    return token.decode('utf-8')

def decode(request,s):
    f=frt(request.session['key'].encode('utf-8'))
    token = f.decrypt(s.encode('utf-8'))
    # print(token.decode('utf-8'))
    return token.decode('utf-8')


# def compute(request,count):
#     i=datetime.strptime('2020413', '%Y%m%d')
#     # print(str(i.date()))
#     j=0
#     obj=[]
#     temp_label=[]
#     temp_obj=[]
#     label=[]
#     temp_status=[]
#     status=[]
#     c=1
#     today=datetime.now()
#     threshold=today-timedelta(days=8)
#     today=today.strftime('%Y-%m-%d')
#     # today=datetime.strptime('2020505', '%Y%m%d')
#     # print(today)
#     # if str(i.date()) == str(today):
#     #     print("yes")
#     # else:
#     #     print("no")

#     # print(i)
#     # print(type(i.date()))
#     # print(today)
#     # print(str(i.date()))
#     flag=0
#     days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
#     # print(type(i.date()))
#     # print(type(threshold.date()))
#     # p=i.date()<threshold.date()
#     # print(p)
#     while str(i.date()) != today:
        
        
#             temp_obj.append(count[i.date()])
#             if count[i] == None:
#                 temp_obj.append(0)
#             temp_label.append(days[i.date().weekday()])
            
#             # print(label[j],"   ",obj[j])
 
#             c=c+1
#             i=i+timedelta(days=1)
            
#             if c % 8 == 0 and i.date() <= threshold.date():
#                 obj.append(temp_obj)
#                 label.append(temp_label)
#                 # status.append(temp_status)
#                 temp_obj=[]
#                 temp_label=[]
#                 # temp_status=[]
#                 c=1
                
#                 continue
            
#             elif i.date() > threshold.date() and temp_label != None:
#                 # print("here")
#                 flag=1
#                 if c % 8 == 0 :
#                     obj.append(temp_obj)
#                     label.append(temp_label)
#                     # status.append(temp_status)
#                     temp_obj=[]
#                     temp_label=[]
#                     # temp_status=[]
#                     c=1
#                 continue
#     if flag==1:
#         # print("here23")
#         obj.append(temp_obj)
#         label.append(temp_label)
#         # status.append(temp_status)
#         temp_obj=[]
#         temp_label=[]
                
#                 # temp_status=[]
                
       
#     print('labels:',label)
#     print('data:',obj)
#     # print('status:',status)    
#     return [label,obj] 
    
def searchn(request):
    fromdate=request.POST['date']
    # fromdate = datetime.strptime(fromdate, '%Y-%m-%d').date
    todate=request.POST['date1']
    # todate = datetime.strptime(todate, '%Y-%m-%d')
    # print(todate)
    facility=request.POST['select']
    # frdate=datetime.strptime(fromdate,'%Y-%m-%d').date()
    facility=str(facility)
    facility=facility.lower()
    facility=facility.capitalize()
    facility=facility.split(" ")
    facility=''.join(facility)
    year,month,day = fromdate.split('-')
    month=re.sub("^0",'',month)
    day=re.sub("^0",'',day)
    print(month,"  ",day)
    # fromdate= datetime(int(year),int(month),int(day)).date()
    # year,month,day = fromdate.split('-')
    month=re.sub("^0",'',month)
    day=re.sub("^0",'',day)
    fromdate=str(year)+","+str(month)+","+str(day)
    
    
    year,month,day = todate.split('-')
    month=re.sub("^0",'',month)
    day=re.sub("^0",'',day)
    todate=str(year)+","+str(month)+","+str(day)
    # todate= datetime(int(year),int(month),int(day)).date()
    
    str1='temp=models.'
    str2='.objects'
    str4='.filter( Q(date__gte='
    str5=str(fromdate)
    # str5=re.sub('-0','-',str(fromdate))
    str5='date('+fromdate+')'
    str6= ') &  Q(date__lte=' 
    str7=str(todate)
    str7=re.sub('-0','-',str(todate))
    str7='date('+todate+')'
    str8='))'
    str3='.values()'
    # str4='.objects.all()'

   
        
    que=str1+facility+str2+str4+str5+str6+str7+str8+str3
    print(que)
    exec(que,globals())
    
    
    supdetails,eng=navdet()
    # print(facility)
    print(temp)
    return render(request,'dgm/dashboardn.html',{'supdetails':supdetails,'eng':eng,'searched':temp})



def searchc(request):
    fromdate=request.POST['date']
    # fromdate = datetime.strptime(fromdate, '%Y-%m-%d').date
    todate=request.POST['date1']
    # todate = datetime.strptime(todate, '%Y-%m-%d')
    # print(todate)
    facility=request.POST['select']
    # frdate=datetime.strptime(fromdate,'%Y-%m-%d').date()
    facility=str(facility)
    facility=facility.lower()
    facility=facility.capitalize()
    facility=facility.split(" ")
    facility=''.join(facility)
    year,month,day = fromdate.split('-')
    month=re.sub("^0",'',month)
    day=re.sub("^0",'',day)
    print(month,"  ",day)
    # fromdate= datetime(int(year),int(month),int(day)).date()
    # year,month,day = fromdate.split('-')
    month=re.sub("^0",'',month)
    day=re.sub("^0",'',day)
    fromdate=str(year)+","+str(month)+","+str(day)
    
    
    year,month,day = todate.split('-')
    month=re.sub("^0",'',month)
    day=re.sub("^0",'',day)
    todate=str(year)+","+str(month)+","+str(day)
    # todate= datetime(int(year),int(month),int(day)).date()
    
    str1='temp=models.'
    str2='.objects'
    str4='.filter( Q(date__gte='
    str5=str(fromdate)
    # str5=re.sub('-0','-',str(fromdate))
    str5='date('+fromdate+')'
    str6= ') &  Q(date__lte=' 
    str7=str(todate)
    str7=re.sub('-0','-',str(todate))
    str7='date('+todate+')'
    str8='))'
    str3='.values()'
    # str4='.objects.all()'

   
        
    que=str1+facility+str2+str4+str5+str6+str7+str8+str3
    print(que)
    exec(que,globals())
    
    
    supdetails,eng=comdet()
    # print(facility)
    print(temp)
    return render(request,'dgm/dashboardc.html',{'supdetails':supdetails,'eng':eng,'searched':temp})
    
def searchs(request):
    fromdate=request.POST['date']
    # fromdate = datetime.strptime(fromdate, '%Y-%m-%d').date
    todate=request.POST['date1']
    # todate = datetime.strptime(todate, '%Y-%m-%d')
    # print(todate)
    facility=request.POST['select']
    # frdate=datetime.strptime(fromdate,'%Y-%m-%d').date()
    facility=str(facility)
    facility=facility.lower()
    facility=facility.capitalize()
    facility=facility.split(" ")
    facility=''.join(facility)
    year,month,day = fromdate.split('-')
    month=re.sub("^0",'',month)
    day=re.sub("^0",'',day)
    print(month,"  ",day)
    # fromdate= datetime(int(year),int(month),int(day)).date()
    # year,month,day = fromdate.split('-')
    month=re.sub("^0",'',month)
    day=re.sub("^0",'',day)
    fromdate=str(year)+","+str(month)+","+str(day)
    
    
    year,month,day = todate.split('-')
    month=re.sub("^0",'',month)
    day=re.sub("^0",'',day)
    todate=str(year)+","+str(month)+","+str(day)
    # todate= datetime(int(year),int(month),int(day)).date()
    
    str1='temp=models.'
    str2='.objects'
    str4='.filter( Q(date__gte='
    str5=str(fromdate)
    # str5=re.sub('-0','-',str(fromdate))
    str5='date('+fromdate+')'
    str6= ') &  Q(date__lte=' 
    str7=str(todate)
    str7=re.sub('-0','-',str(todate))
    str7='date('+todate+')'
    str8='))'
    str3='.values()'
    # str4='.objects.all()'

   
        
    que=str1+facility+str2+str4+str5+str6+str7+str8+str3
    print(que)
    exec(que,globals())
    
    
    supdetails,eng=surdet()
    # print(facility)
    print(temp)
    return render(request,'dgm/dashboards.html',{'supdetails':supdetails,'eng':eng,'searched':temp})
    

def navdet():
    supdetails = models.Supervisor.objects.all().filter(dept='N')
    eng=models.Engineer.objects.values('emp_id','name').filter(dept='N')
    eng=list(eng)
    print(eng)
    for i in eng:
        i['submitted']=models.Cdvordaily.objects.filter(emp_id=i['emp_id']).count()+models.Cdvormonthly.objects.filter(emp_id=i['emp_id']).count()+models.Cdvorweekly.objects.filter(emp_id=i['emp_id']).count()
        i['accepted']=models.Cdvordaily.objects.all().filter( Q (unit_incharge_approval ='YES') & Q(emp_id=i['emp_id'])).count()+models.Cdvormonthly.objects.filter( Q(unit_incharge_approval='YES') & Q(emp_id=i['emp_id'])).count()+models.Cdvorweekly.objects.filter( Q(unit_incharge_approval ='YES') & Q(emp_id=i['emp_id'])).count()
        i['reject']=models.Cdvordaily.objects.filter(Q( unit_incharge_approval='NO') & Q(emp_id=i['emp_id'])).count()+models.Cdvormonthly.objects.filter(Q(unit_incharge_approval='NO') & Q(emp_id=i['emp_id'])).count()+models.Cdvorweekly.objects.filter( Q(unit_incharge_approval='NO') & Q(emp_id=i['emp_id'])).count()
        i['pending']=models.Cdvordaily.objects.filter(Q(unit_incharge_approval=None) & Q(emp_id=i['emp_id'])).count()+models.Cdvormonthly.objects.filter(Q(unit_incharge_approval=None) & Q(emp_id=i['emp_id'])).count()+models.Cdvorweekly.objects.filter( Q(unit_incharge_approval=None) & Q(emp_id=i['emp_id'])).count()
    # conc=list(chain(cdvordaily,cdvormonthly, cdvorweekly))
    # for i in conc:
    #     if i['unit_incharge_approval'] !=None:
    #         i['submitted']=1
    #     if i['unit_incharge_approval']=='YES':
    #             i['accepted']=1
    #     elif i['unit_incharge_approval']=='NO':
    #             i['reject']=1
    #     else:
    #         i['pending']=1
    # for i in conc:
    #     i['name']=models.Engineer.objects.values('name').filter(emp_id=i['emp_id'])[0]['name']

    # conc=collections.Counter('emp_id')
        
    print("here",eng)
    return supdetails,eng



def comdet():
    supdetails = models.Supervisor.objects.all().filter(dept='C')
    eng=models.Engineer.objects.values('emp_id','name').filter(dept='C')
    eng=list(eng)
    print(eng)
    for i in eng:
        i['submitted']=models.Dscndaily.objects.filter(emp_id=i['emp_id']).count()+models.Dscnmonthly.objects.filter(emp_id=i['emp_id']).count()+models.Dscnweekly.objects.filter(emp_id=i['emp_id']).count()+models.Datisdaily.objects.filter(emp_id=i['emp_id']).count()+models.Datisweekly.objects.filter(emp_id=i['emp_id']).count()
        i['accepted']=models.Dscndaily.objects.all().filter( Q (unit_incharge_approval ='YES') & Q(emp_id=i['emp_id'])).count()+models.Dscnmonthly.objects.filter( Q(unit_incharge_approval='YES') & Q(emp_id=i['emp_id'])).count()+models.Dscnweekly.objects.filter( Q(unit_incharge_approval ='YES') & Q(emp_id=i['emp_id'])).count()+models.Datisweekly.objects.filter( Q(unit_incharge_approval ='YES') & Q(emp_id=i['emp_id'])).count()+models.Datisdaily.objects.filter( Q(unit_incharge_approval ='YES') & Q(emp_id=i['emp_id'])).count()
        i['reject']=models.Dscndaily.objects.filter(Q( unit_incharge_approval='NO') & Q(emp_id=i['emp_id'])).count()+models.Dscnmonthly.objects.filter(Q(unit_incharge_approval='NO') & Q(emp_id=i['emp_id'])).count()+models.Dscnweekly.objects.filter( Q(unit_incharge_approval='NO') & Q(emp_id=i['emp_id'])).count()+models.Datisdaily.objects.filter( Q(unit_incharge_approval='NO') & Q(emp_id=i['emp_id'])).count()+models.Datisweekly.objects.filter( Q(unit_incharge_approval='NO') & Q(emp_id=i['emp_id'])).count()
        i['pending']=models.Dscndaily.objects.filter(Q(unit_incharge_approval=None) & Q(emp_id=i['emp_id'])).count()+models.Dscnmonthly.objects.filter(Q(unit_incharge_approval=None) & Q(emp_id=i['emp_id'])).count()+models.Dscnweekly.objects.filter( Q(unit_incharge_approval=None) & Q(emp_id=i['emp_id'])).count()++models.Datisdaily.objects.filter( Q(unit_incharge_approval=None) & Q(emp_id=i['emp_id'])).count()+models.Datisweekly.objects.filter( Q(unit_incharge_approval=None) & Q(emp_id=i['emp_id'])).count()
    # conc=list(chain(cdvordaily,cdvormonthly, cdvorweekly))
    # for i in conc:
    #     if i['unit_incharge_approval'] !=None:
    #         i['submitted']=1
    #     if i['unit_incharge_approval']=='YES':
    #             i['accepted']=1
    #     elif i['unit_incharge_approval']=='NO':
    #             i['reject']=1
    #     else:
    #         i['pending']=1
    # for i in conc:
    #     i['name']=models.Engineer.objects.values('name').filter(emp_id=i['emp_id'])[0]['name']

    # conc=collections.Counter('emp_id')
        
    print("here",eng)
    return supdetails,eng

def surdet():
    supdetails = models.Supervisor.objects.all().filter(dept='S')
    eng=models.Engineer.objects.values('emp_id','name').filter(dept='S')
    eng=list(eng)
    print(eng)
    for i in eng:
        i['submitted']=models.Scctvdaily.objects.filter(emp_id=i['emp_id']).count()+models.Scctvmonthly.objects.filter(emp_id=i['emp_id']).count()+models.Scctvweekly.objects.filter(emp_id=i['emp_id']).count()
        i['accepted']=models.Scctvdaily.objects.all().filter( Q (unit_incharge_approval ='YES') & Q(emp_id=i['emp_id'])).count()+models.Scctvmonthly.objects.filter( Q(unit_incharge_approval='YES') & Q(emp_id=i['emp_id'])).count()+models.Scctvweekly.objects.filter( Q(unit_incharge_approval ='YES') & Q(emp_id=i['emp_id'])).count()
        i['reject']=models.Scctvdaily.objects.filter(Q( unit_incharge_approval='NO') & Q(emp_id=i['emp_id'])).count()+models.Scctvmonthly.objects.filter(Q(unit_incharge_approval='NO') & Q(emp_id=i['emp_id'])).count()+models.Scctvweekly.objects.filter( Q(unit_incharge_approval='NO') & Q(emp_id=i['emp_id'])).count()
        i['pending']=models.Scctvdaily.objects.filter(Q(unit_incharge_approval=None) & Q(emp_id=i['emp_id'])).count()+models.Scctvmonthly.objects.filter(Q(unit_incharge_approval=None) & Q(emp_id=i['emp_id'])).count()+models.Scctvweekly.objects.filter( Q(unit_incharge_approval=None) & Q(emp_id=i['emp_id'])).count()
    # for i in conc:
    #     if i['unit_incharge_approval'] !=None:
    #         i['submitted']=1
    #     if i['unit_incharge_approval']=='YES':
    #             i['accepted']=1
    #     elif i['unit_incharge_approval']=='NO':
    #             i['reject']=1
    #     else:
    #         i['pending']=1
    # for i in conc:
    #     i['name']=models.Engineer.objects.values('name').filter(emp_id=i['emp_id'])[0]['name']

    # conc=collections.Counter('emp_id')
        
    print("here",eng)
    return supdetails,eng
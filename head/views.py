from django.shortcuts import render,HttpResponse

from datetime import date,datetime,timedelta
from django.db import connection
import folium
import os
import json
from login import models as models
# Create your views here.
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

def dispMap(request,airInfo):


    # Create map object
    m = folium.Map(location=[21.1458, 79.0882],zoom_start=5)
    

    # Adding feature group for Indian Border Outline
    fg = folium.FeatureGroup('mymap')
    fg.add_child(folium.GeoJson(data=(open('head/india.json','r',encoding='utf-8-sig').read())))
    m.add_child(fg)

    # Global tooltip
    tooltip = 'Click For More Info'

    # Create custom marker icon
    # logoIcon = folium.features.CustomIcon('logo.png', icon_size=(50, 50))

    # Vega data
    # vis = os.path.join('data', 'vis.json')

    # Geojson Data
    # overlay = os.path.join('data', 'overlay.json')

    # Create markers
    
    
    for i in airInfo:
        tooltipName = i['name']
        tooltipCode = i['code']
        tooltip = tooltipName + " - " + tooltipCode
        dgm=models.Dgm.objects.filter(a_id=i['a_id']).values()
        folium.Marker([i['longitude'], i['latitude']],
                popup=folium.Popup(
                ('<table border=1><h5><a href="/head/headv" target="_blank"><h5 style="text-align: center;">{tooltip}</a></h5><tr><th style="text-align: center;">ID</th><th style="text-align: center;">{did}</th></tr><tr><th style="text-align: center;">NAME</th><th style="text-align: center;">{dname}</th></tr><tr><th style="text-align: center;">CONTACT</th><th style="text-align: center;">{dcontact}</th></tr><tr><th style="text-align: center;">EMAIL</th><th style="text-align: center;">{demail}</th></tr></table>').format(tooltip=tooltip,did=dgm[0]['dgm_id'],dname=dgm[0]['name'],name=i['name'],dcontact=dgm[0]['contact'],demail=dgm[0]['email']),max_width=250,min_width=150),
                tooltip=tooltip,
                icon=folium.Icon(color='red')).add_to(m)
    # folium.Marker([42.333600, -71.109500],
    #             popup='<strong>Location Two</strong>',
    #             tooltip=tooltip,
    #             icon=folium.Icon(icon='cloud')).add_to(m),
    # folium.Marker([42.377120, -71.062400],
    #             popup='<strong>Location Three</strong>',
    #             tooltip=tooltip,
    #             icon=folium.Icon(color='purple')).add_to(m),
    # folium.Marker([42.374150, -71.122410],
    #             popup='<strong>Location Four</strong>',
    #             tooltip=tooltip,
    #             icon=folium.Icon(color='green', icon='leaf')).add_to(m),
    # folium.Marker([42.375140, -71.032450],
    #             popup='<strong>Location Five</strong>',
    #             tooltip=tooltip).add_to(m),
                # icon=logoIcon)
    # folium.Marker([42.315140, -71.072450],
    #             popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)), width=450, height=250))).add_to(m)

    # Circle marker
    # folium.CircleMarker(
    #     location=[42.466470, -70.942110],
    #     radius=50,
    #     popup='My Birthplace',
    #     color='#428bca',
    #     fill=True,
    #     fill_color='#428bca'
    # ).add_to(m)

    # Geojson overlay
    # folium.GeoJson(overlay, name='cambridge').add_to(m)

    m.save('./head/templates/head/map.html')
    return render(request,"./head/map.html")



def headv(request,uid=1101):
    labels = []
    data = []
    
    request.session['type']='h'
    request.session['uid']=uid
    # dgm= models.Dgm.objects.all().filter(dgm_id=uid).values()
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



    # totsubmit=submit+scctvsubmit+comsubmit
    # totapprove=approve+scctvapprove+comapprove
    # totnapprove=


    return render(request, './head/head.html', {
        # 'dgmdet':dgm,
        'navsubmit':submit,
        'navapprove':approve,
        'navnapprove':napprove,
        'navpend':nsubmit,
        
        
        'totsubmit':submit+scctvsubmit+comsubmit,
        'totapprove':approve+scctvapprove+comapprove,
        'totnapprove':napprove+nscctvapprove+ncomapprove,
        'totpen':nsubmit+nscctvsubmit+ncomsubmit,
        
        
        
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

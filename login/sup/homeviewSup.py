from django.shortcuts import render

from datetime import date,datetime,timedelta
from django.db import connection
from cryptography.fernet import Fernet as frt
from supervisor.views import main
from operator import itemgetter

# Create your views here.

from django.http import HttpResponse
from .. import models
from django.db import connection
from django.db.models import Q
def run_sup(request,uid):
    today = datetime.now().strftime('%d/%m/%Y')
    request.session['type']='s'
    request.session['uid']=uid
    # request.session['passw']=passw
    # print(request.session['uid'])
    supInfo=models.Supervisor.objects.filter(supervisor_id=uid).values()
    airInfo=models.Airport.objects.filter(a_id=supInfo[0]['a_id']).values('name')
    print(airInfo)
    dgm=models.Dgm.objects.filter(a_id=supInfo[0]['a_id']).values()
    id=uid
    # datisdaily=[entry for entry in models.Datisdaily.objects.filter(unit_incharge_approval=None).values()]
    
    # datisweekly=[entry for entry in models.Datisweekly.objects.filter(unit_incharge_approval=None).values()]
    # datis=datisdaily+[i for i in datisweekly]
    # datis=sorted(datis,key=itemgetter('date'),reverse=True)
    

    # print(datisdaily)
    if request.session.get('dept')=='N':
        Cdvordaily=[entry for entry in models.Cdvordaily.objects.filter(unit_incharge_approval=None).values().order_by('-date')]
        for item in Cdvordaily:
                item.update( {"type":"Cdvordaily"})
                item.update({"repdead":item['date']})
        Cdvorweekly=[entry for entry in models.Cdvorweekly.objects.filter(unit_incharge_approval=None).values().order_by('-date')]
        for item in Cdvorweekly:
                item.update( {"type":"Cdvorweekly"})
                item.update({"repdead":week(item['date'])})
        
        ndbdaily=[entry for entry in models.Ndbdaily.objects.filter(unit_incharge_approval=None).values().order_by('-date')]
        for item in ndbdaily:
                item.update( {"type":"Ndbdaily"})
        
        Ndbweekly=[entry for entry in models.Cdvorweekly.objects.filter(unit_incharge_approval=None).values().order_by('-date')]
        for item in Ndbweekly:
                item.update( {"type":"Ndbweekly"})
        Ndbmonthly=[entry for entry in models.Ndbmonthly.objects.filter(unit_incharge_approval=None).values().order_by('-date')]
        for item in Ndbmonthly:
                item.update( {"type":"Ndbmonthly"})
        Dmedaily=[entry for entry in models.Dmedaily.objects.filter(unit_incharge_approval=None).values().order_by('-date')]
        for item in Dmedaily:
                item.update( {"type":"Dmedaily"})
        
        Dmeweekly=[entry for entry in models.Dmeweekly.objects.filter(unit_incharge_approval=None).values().order_by('-date')]
        for item in Dmeweekly:
                item.update( {"type":"Dmeweekly"})
        Dmemonthly=[entry for entry in models.Dmemonthly.objects.filter(unit_incharge_approval=None).values().order_by('-date')]
        for item in Dmemonthly:
                item.update( {"type":"Dmemonthly"})
        
        Cdvormonthly=[entry for entry in models.Cdvormonthly.objects.filter(unit_incharge_approval=None).values().order_by('-date')]
        for item in Cdvormonthly:
                item.update( {"type":"Cdvormonthly"})  
                item.update({"repdead":month(item['date'])})      
        
        
        com=Cdvordaily+[i for i in Cdvorweekly]+[i for i in Dmeweekly]+[i for i in Dmedaily]+[i for i in Dmemonthly]+[i for i in Ndbweekly]+[i for i in ndbdaily]+[i for i in Ndbmonthly]+[i for i in Cdvormonthly]
        com=sorted(com,key=itemgetter('date'),reverse=True)
        
        eng=[entry for entry in models.Engineer.objects.filter(supervisor_id=uid).values()]
        for i in com:

            i.update({'token':main.encode(request,str(i['p_id']))})

        
    
    
    
    elif request.session.get('dept')=='C':
        datisdaily=[entry for entry in models.Datisdaily.objects.filter(Q(unit_incharge_approval=None) | Q(status='PENDING')).values().order_by('-date')]
        for item in datisdaily:
                item.update( {"type":"Datisdaily"})
                item.update({"repdead":item['date']})
        datisweekly=[entry for entry in models.Datisweekly.objects.filter(Q(unit_incharge_approval=None) | Q(status='PENDING')).values().order_by('-date')]
        for item in datisweekly:
                item.update( {"type":"Datisweekly"})
                item.update({"repdead":week(item['date'])})
        vhfdaily=[entry for entry in models.Vhfdaily.objects.filter(Q(unit_incharge_approval=None) | Q(status='PENDING')).values().order_by('-date')]
        for item in vhfdaily:
                item.update( {"type":"Vhfdaily"})
                
                item.update({"repdead":item['date']})
        # vhfweekly=[entry for entry in models.Vhfweekly.objects.filter(unit_incharge_approval=None).values().order_by('-date')]
        # for item in vhfweekly:
        #         item.update( {"type":"Vhfweekly"})
        # vhfmonthly=[entry for entry in models.Vhfmonthly.objects.filter(Q(unit_incharge_approval=None) | Q(status='PENDING')).values().order_by('-date')]
        # for item in vhfmonthly:
        #         item.update( {"type":"Vhfmonthly"})
        #         item.update({"repdead":month(item['date'])})
        dscndaily=[entry for entry in models.Dscndaily.objects.filter(Q(unit_incharge_approval=None) | Q(status='PENDING')).values().order_by('-date')]
        for item in dscndaily:
                item.update( {"type":"Dscndaily"})
                # item.update({"repdead":dailydeadline})
                item.update({"repdead":item['date']})
        dscnweekly=[entry for entry in models.Dscnweekly.objects.filter(Q(unit_incharge_approval=None) | Q(status='PENDING')).values().order_by('-date')]
        for item in dscnweekly:
                item.update( {"type":"Dscnweekly"})
                item.update({"repdead":week(item['date'])})
        dscnmonthly=[entry for entry in models.Dscnmonthly.objects.filter(Q(unit_incharge_approval=None) | Q(status='PENDING')).values().order_by('-date')]
        for item in dscnmonthly:
                item.update( {"type":"Dscnmonthly"})
                item.update({"repdead":month(item['date'])})
        
        com=[i for i in datisdaily]+[i for i in datisweekly]+[i for i in dscnweekly]+[i for i in dscndaily]+[i for i in dscnmonthly]+[i for i in vhfdaily]
        com=sorted(com,key=itemgetter('date'),reverse=True)
        
        
        for i in com:

            i.update({'token':main.encode(request,str(i['p_id']))})
        
    
    else:
        Scctvdaily=[entry for entry in models.Scctvdaily.objects.filter(unit_incharge_approval=None).values().order_by('-date')]
        for item in Scctvdaily:
                item.update( {"type":"Scctvdaily"})
                item.update({"repdead":item['date']})
        Scctvweekly=[entry for entry in models.Scctvweekly.objects.filter(unit_incharge_approval=None).values().order_by('-date')]
        for item in Scctvweekly:
                item.update( {"type":"Scctvweekly"})
                item.update({"repdead":week(item['date'])})
        Scctvmonthly=[entry for entry in models.Scctvmonthly.objects.filter(unit_incharge_approval=None).values().order_by('-date')]
        for item in Scctvmonthly:
                item.update( {"type":"Scctvmonthly"})
                item.update({"repdead":month(item['date'])})
        com=[i for i in Scctvweekly]+[i for i in Scctvdaily]+[i for i in Scctvmonthly]
        com=sorted(com,key=itemgetter('date'),reverse=True)
        for i in com:

            i.update({'token':main.encode(request,str(i['p_id']))})
        
        
    
    
    
    eng=[entry for entry in models.Engineer.objects.filter(supervisor_id=uid).values()] 


    
    for i in eng:
        # token=main.encode(i['p_id'])
        # i.update('token':main.encode(i['p_id']))
        i.update({'token':main.encode(request,str(i['emp_id']))})
    context=dhomeview_sup()
    print(eng)
    
    context.update({'sup':supInfo[0],'dgm':dgm[0],'datis':com,'eng':eng,'air':airInfo[0]})
    # print(context['datisd_deadline'])
    return render(request,'./supervisor/home.html',context)


def dhomeview_sup() :
  
    cursor = connection.cursor() 
    # s0 = models.Engineer.objects.all()
    # s0 = s0.values('a_id')
    # s0 = s0.filter(emp_id=id)

    # _q = models.Airport.objects
    # _q = _q.filter(a_id__in=s0)
    # name1 = _q.all()
                
    # q = models.Engineer.objects
    # q = q.values('name','designation','a_id')
    # q = q.filter(emp_id=id)
    # empdetails = q.all()
    ddr =0           

    status = "" 
        #!!!!!!!!!!!!!!!!!datis daily!!!!!!!!!!!!!!!!!!!!!!!!
    currdate = date.today()
    currtime = datetime.now().strftime("%H:%M:%S")            
    datisdsub_on = cursor.execute("select date from datisdaily where date = %s",[date.today()])    
    if datisdsub_on :
        status = models.Datisdaily.objects.all()
        status = status.values('date','status')
        status = status.order_by('-date')
        status = status.values('status')
        status = status.values('status').filter(a_id=1)[0]['status']
        if status == "PENDING" :
            datisdsub_on = currdate
            datisd_deadline = currdate
            ddr=0
        else :
            datisd_deadline = currdate + timedelta(days=1)
            datisdsub_on = currdate
            ddr =1 
        
    else :
        datisd_deadline = models.Datisdaily.objects.all()
        datisd_deadline = datisd_deadline.values('date')
        datisd_deadline = datisd_deadline.order_by('-date')
        datisd_deadline = datisd_deadline.values('date').filter(a_id=1)[0]['date']
        datisdsub_on = datisd_deadline
        datisd_deadline = datisd_deadline + timedelta(days=2)
        if (datisd_deadline <= date.today()) :    
            # remarks = "---Report not submitted---"
            # status = "COMPLETED"
            # val = ((date.today()-timedelta(days=1)),id,status,'2',remarks)
            # sql = "INSERT INTO datisdaily (date,emp_id,status,f_id,remarks) values (%s ,%s,%s, %s,%s)"
            # cursor.execute(sql,val)  
            datisdsub_on = date.today()-timedelta(days=1)    
        else : 
            datisd_deadline = date.today()
    # print("here")
    datisd_deadline1=datisd_deadline.strftime('%d/%m/%Y')
    datisdsub_on1=datisdsub_on.strftime('%d/%m/%Y')
    context={'ddr':ddr,'currdate':currdate,'datisdsub_on':datisdsub_on1,'datisd_deadline':datisd_deadline1}
    return context
def week(cd):
        ded=cd+timedelta(7)
        return ded
def month(cd):
        ded=cd+timedelta(30)
        return ded
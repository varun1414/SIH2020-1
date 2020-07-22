from django.shortcuts import render,redirect
from django.db import connection
from datetime import date,datetime,timedelta
from login import models as models
from django.core.mail import send_mail
from django.contrib import messages
from login import views 
from operator import itemgetter

# Create your views here.
def sent(request):
    if request.session.has_key('uid'):
        id = request.session['uid']
        mail = request.POST['feedback'] 
        send_mail('urgent',mail,'aai.urgent@gmail.com',['kelkarkulbhushan@gmail.com'],fail_silently=False)
        return redirect(request.META['HTTP_REFERER'])
        #return routebackscctvd(request, id )

def logoutd(request,id):
   try:
      del request.session['uid']
      request.session.flush()
   except:
      pass
   return render(request,'login/login.html')

def routebackscctvd(request, id) :
  if request.session.has_key('uid'):
    cursor = connection.cursor() 
    s0 = models.Engineer.objects.all()
    s0 = s0.values('a_id')
    s0 = s0.filter(emp_id=id)

    _q = models.Airport.objects
    _q = _q.filter(a_id__in=s0)
    name1 = _q.all()
                
    q = models.Engineer.objects
    q = q.values('name','designation','a_id')
    q = q.filter(emp_id=id)
    empdetails = q.all()
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='S')
    
    ddr =0            
    statusd = ""
    scctvd_deadline = ""
     
        #!!!!!!!!!!!!!!!!!scctv daily!!!!!!!!!!!!!!!!!!!!!!!!
    currdate = date.today()
    currtime = datetime.now().strftime("%H:%M:%S")            
    scctvdsub_on = cursor.execute("select date from scctvdaily where date = %s",[date.today()])    
    if scctvdsub_on :
        statusd = models.Scctvdaily.objects.all()
        statusd = statusd.values('date','status')
        statusd = statusd.order_by('-date')
        statusd = statusd.values('status')
        statusd = statusd.values('status').filter(a_id=1)[0]['status']
        if statusd == "PENDING" :
            scctvdsub_on = currdate
            scctvd_deadline = currdate
            ddr=0
        elif statusd == "COMPLETED" :
            scctvd_deadline = currdate + timedelta(days=1)
            scctvdsub_on = currdate
            ddr =1 
        elif statusd == "COMPLETED WITH ERRORS" :
            scctvd_deadline = date.today() + timedelta(days=1)
            scctvdsub_on = currdate
            ddr = 1
   
    else :
        scctvd_deadline = models.Scctvdaily.objects.all()
        scctvd_deadline = scctvd_deadline.values('date')
        scctvd_deadline = scctvd_deadline.order_by('-date')
        scctvd_deadline = scctvd_deadline.values('date').filter(a_id=1)[0]['date']
        scctvdsub_on = scctvd_deadline
        scctvd_deadline = scctvd_deadline + timedelta(days=2)
        tempdate = scctvdsub_on + timedelta(days=1)
        i = 1 
        while i == 1 and tempdate != date.today() : 
         if (scctvd_deadline <= date.today()) :    
            #remarks = "---Report not submitted---"
            #statusd = "COMPLETED"
            #val = (tempdate,currtime,'1',id,statusd,'2',remarks)
            #sql = "INSERT INTO scctvdaily (date,time,a_id,emp_id,status,f_id,remarks) values (%s ,%s,%s,%s,%s, %s,%s)"
            #cursor.execute(sql,val)  
            scctvdsub_on = date.today()-timedelta(days=1)    
            tempdate = tempdate + timedelta(days=1)
         else : 
            break
        scctvd_deadline = date.today()
       
    #!!!!!!!!!!!!!!!!!!!!!!!scctv weekly!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    p_id = models.Scctvweekly.objects.all()
    p_id = p_id.values('p_id')
    p_id = p_id.order_by('-p_id')
    p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
    currdate = date.today()
    wdate = models.Scctvweekly.objects.all()
    wdate = wdate.values('date')
    wdate = wdate.order_by('-date')
    wdate1 = wdate
    wdate = wdate.values('date').filter(a_id=1)[0]['date']
    wdate1 = wdate1.values('date').filter(a_id=1)[1]['date']
    wdate = str(wdate)
    wdate = datetime.strptime(wdate, "%Y-%m-%d").date()
    temp = wdate
    temp1 = wdate1 + timedelta(days=7)
    wdate = wdate + timedelta(days=7) 
    dwr = 0
    scctvwsub_on = temp
    scctvwsub_deadline =  wdate 
    status = ""
    status = models.Scctvweekly.objects.all()
    status = status.values('date','status','unit_incharge_approval')
    status = status.order_by('-date')
    uia = status
    uia = uia.values('unit_incharge_approval')
    uia = uia.values('unit_incharge_approval').filter(a_id=1)[0]['unit_incharge_approval']
    status = status.values('status')
    status = status.values('status').filter(a_id=1)[0]['status']
    flag = cursor.execute("select date from scctvweekly where date = %s",[date.today()])    
        
    if currdate > wdate :  #if it goes beyond 7 days
        dwr = 0
    if flag :    
        if  temp1 < temp : #report submitted after deadline
            scctvwsub_deadline = temp1    
            if status == "COMPLETED" or status == "COMPLETED WITH ERRORS" :
                dwr=1
                print(temp1)  
            elif status == "PENDING" :
                dwr=0
            
        elif temp == temp1 and temp == currdate : # report submitted on same day as deadline
            scctvwsub_deadline = temp    
            if status == "COMPLETED" or status == "COMPLETED WITH ERRORS" :
                dwr=1  
            elif status == "PENDING" :
                dwr=0
            
        elif temp1 < wdate and temp1 > temp : #report submitted before the deadline 
            scctvwsub_deadline = temp1   
            if status == "COMPLETED" or status == "COMPLETED WITH ERRORS" :
                dwr=1  
            elif status == "PENDING" :
                dwr=0
   
   
    p_id = models.Scctvmonthly.objects.all()
    p_id = p_id.values('p_id')
    p_id = p_id.order_by('-p_id')
    p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
   
    wdatem = models.Scctvmonthly.objects.all()
    wdatem = wdatem.values('date')
    wdatem = wdatem.order_by('-date')
    wdate1 = wdatem
    wdatem = wdatem.values('date').filter(a_id=1)[0]['date']
    wdate1 = wdate1.values('date').filter(a_id=1)[1]['date']
    wdatem = str(wdatem)
    wdatem = datetime.strptime(wdatem, "%Y-%m-%d").date()
    temp = wdatem
    temp1 = wdate1 + timedelta(days=30)
    wdatem = wdatem + timedelta(days=30) 
    dsmr = 0
    scctvmsub_on = temp
    scctvmsub_deadline =  wdatem 
    statusdm = ""
    statusdm = models.Scctvmonthly.objects.all()
    statusdm = statusdm.values('date','status','unit_incharge_approval')
    statusdm = statusdm.order_by('-date')
    uia = statusdm
    uia = uia.values('unit_incharge_approval')
    uia = uia.values('unit_incharge_approval').filter(a_id=1)[0]['unit_incharge_approval']
    statusdm = statusdm.values('status')
    statusdm = statusdm.values('status').filter(a_id=1)[0]['status']
    flag = cursor.execute("select date from scctvmonthly where date = %s",[date.today()])    
    if currdate > wdatem and flag == 0 :  #if it goes beyond 7 days
        pending = wdatem 
        while pending <= (currdate - timedelta(days=1)) :
            f = cursor.execute("select date from scctvmlogs where date = %s",[pending])    
            if f == 0 : 
                remarks = "Report not submitted"
                value = "No Entry" 
                val = (id,p_id,remarks,value,pending,currtime)
                sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s ,%s, %s,%s)"
                cursor.execute(sql,val)
            pending = pending + timedelta(days=1)    
        dsmr = 0
        
    if flag :    
        if  temp1 < temp : #report submitted after deadline
            scctvm_deadline = temp1    
            if statusdm == "COMPLETED" or statusdm == "COMPLETED WITH ERRORS" :
                dsmr=1  
            elif statusdm == "PENDING" :
                dsmr=0
            
        elif temp == temp1 and temp == currdate : # report submitted on a day same as deadline
            scctvmsub_deadline = temp    
            if statusdm == "COMPLETED" or statusdm == "COMPLETED WITH ERRORS" :
                dsmr=1  
            elif statusdm == "PENDING" :
                dsmr=0
            
        elif temp1 < wdatem and temp1 > temp : #report submitted before the deadline 
            scctvmsub_deadline = temp1   
            if statusdm == "COMPLETED" or statusdm == "COMPLETED WITH ERRORS" :
                dsmr=1  
            elif statusdm == "PENDING" :
                dsmr=0
    print(dsmr)
    print(scctvmsub_on)        
        
    print(wdatem)
    
    
    
    
    Scctvdaily=[entry for entry in models.Scctvdaily.objects.filter(emp_id=id).values().order_by('-date')]
    for item in Scctvdaily:
        item.update( {"type":"scctvdaily"})
                
    scctvweekly=[entry for entry in models.Scctvweekly.objects.filter(emp_id=id).values().order_by('-date')]
    for item in scctvweekly:
        item.update( {"type":"scctvweekly"})
    
    scctvmonthly=[entry for entry in models.Scctvmonthly.objects.filter(emp_id=id).values().order_by('-date')]
    for item in scctvmonthly:
        item.update( {"type":"scctvmonthly"})
    com=Scctvdaily+[i for i in scctvweekly]+[i for i in scctvmonthly]
    com=sorted(com,key=itemgetter('date'),reverse=True)
    for i in com:
        i.update({'token':i['p_id']})
    print(com)
        # return render(request,'./engineer/F.html',{'status':status,'Scctvmsub_deadline':Scctvmsub_deadline,'Scctvmsub_on':Scctvmsub_on,'dsmr':dsmr,'dswr':dswr,'Scctvwsub_on':Scctvwsub_on,'Scctvwsub_deadline':Scctvwsub_deadline,'Scctvd_deadline':Scctvd_deadline,'Scctvdsub_on':Scctvdsub_on,'dsdr':dsdr,'ddr':ddr,'dwr':dwr,'vdr':vdr,'vmr':vmr,'vyr':vyr,'currdate':currdate,'name':name1,'id':id,'empdet':empdetails,'Scctvdsub_on':Scctvdsub_on,'Scctvd_deadline':Scctvd_deadline,'Scctvwsub_on':Scctvwsub_on,'Scctvwsub_deadline':Scctvwsub_deadline,'vhfdsub_on':vhfdsub_on,'vhfd_deadline':vhfd_deadline,'vhfmsub_on':vhfmsub_on,'vhfmsub_deadline':vhfmsub_deadline,'vhfysub_on':vhfysub_on,'vhfysub_deadline':vhfysub_deadline})'''
    return render(request,'./engineer/homes.html',{'com':com,'wdate':wdate,'wdatem':wdatem,'supdetails':supdetails,'statusd':statusd,'statusdm':statusdm,'status':status,'ddr':ddr,'dwr':dwr,'dmr':dsmr,'currdate':currdate,'name':name1,'id':id,'empdet':empdetails,'scctvdsub_on':scctvdsub_on,'scctvd_deadline':scctvd_deadline,'scctvwsub_on':scctvwsub_on,'scctvwsub_deadline':scctvwsub_deadline,'scctvmsub_on':scctvmsub_on,'scctvmsub_deadline':scctvmsub_deadline})
  else : 
    return render(request,'login/login.html')
 
   


def scctvd(request, id) :
 if request.session.has_key('uid'):
   uid=request.session['uid'] 
   if int(uid) == int(id):
     cursor = connection.cursor() 
     currdate = date.today()
     scctv_d = models.Scctvdaily.objects.all()
    #  scctv_d = scctv_d.values('p_id','date','status','time','room_temp','status_of_ac','status_of_ups','status_of_servera','status_of_serverb','remarks')
     scctv_d = scctv_d.filter(emp_id=id)
     scctvd = scctv_d.order_by('-p_id')
     scctv_d = scctv_d.filter(date=currdate)     
      #'datetime_of_servers_wrt_gps_clk','status_of_disk_array','vhftx_atis_status','vhfrx_atis_status','scctv_update','audio_quality','remarks','unit_incharge_approval')
     if scctv_d :
        scctvdlogs = models.Scctvdlogs.objects.all()
        scctvdlogs = scctvdlogs.filter(date=date.today()).order_by('-log_id')
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='S')
        return render(request,'engineer/scctv/scctvdailyrep.html',{'supdetails':supdetails,'scctv_d':scctvd,'id':id,'scctvd':scctvd[0],'scctvdlogs':scctvdlogs}) 
     else :
        messages.add_message(request,30, 'You cannot make changes to pending report!')
        return routebackscctvd(request, id)
   else :
       return routebackscctvd(request, uid)
 else : 
   return render(request,'login/login.html')

def homed(request, id, p_id) :
 if request.session.has_key('uid'):
   uid=request.session['uid'] 
   if int(uid) == int(id):
     cursor = connection.cursor() 
     currdate = date.today()
     scctv_d = models.Scctvdaily.objects.all().filter(emp_id=id)
     scctvd = scctv_d.order_by('-p_id')
     scctv_d = scctv_d.filter(p_id=p_id)     
     status = scctv_d.values('status')[0]['status']
     f=0
     
     if status == "COMPLETED WITH ERRORS" or status == "PENDING" :
         f = 1 
     if scctv_d :
        scctvdlogs = models.Scctvdlogs.objects.all().filter(date=date.today()).order_by('-log_id')
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='S')

        return render(request,'engineer/scctv/scctvdailyrep.html',{'f':f,'supdetails':supdetails,'scctv_d':scctvd,'id':id,'scctvd':scctv_d[0],'scctvdlogs':scctvdlogs,'f':f}) 
     else :
        messages.add_message(request,30, 'You cannot make changes to pending report!')
        return routebackscctvd(request, id)
   else :
       return routebackscctvd(request, uid)
 else : 
   return render(request,'login/login.html')
   
def scctvdailyrec(request, id) :
 if request.session.has_key('uid'):
  uid=request.session['uid'] 
  if int(uid) == int(id):
     cursor = connection.cursor() 
     scctv_d = models.Scctvdaily.objects.all()
    #  scctv_d = scctv_d.values('p_id','date','time','status','room_temp','status_of_ac','status_of_ups','status_of_servera','status_of_serverb','unit_incharge_approval','approval_date','approval_time')
     scctv_d = scctv_d.filter(emp_id=id).order_by('-p_id')     
     #'datetime_of_servers_wrt_gps_clk','status_of_disk_array','vhftx_atis_status','vhfrx_atis_status','scctv_update','audio_quality','remarks','unit_incharge_approval')
     return render(request,'engineer/scctv/scctvdrecords.html',{'scctv_d':scctv_d,'id':id}) 
  else :
     messages.add_message(request,30, 'Unauthorized Access')
     return routebackscctvd(request, uid)
 else : 
   return render(request,'login/login.html')

def scctvdrep(request, id) :
 cursor = connection.cursor() 
 if request.session.has_key('uid') : 
   temp = cursor.execute("select date from scctvdaily where date = %s",[date.today()])    
   uid=request.session['uid'] 
   if int(uid) == int(id) and temp == 0:
     supdetails = models.Supervisor.objects.all()
     supdetails = supdetails.values('name','contact','email').filter(dept='C')
     scctv_d = models.Scctvdaily.objects.all()
    #  scctv_d = scctv_d.values('p_id','date','time','room_temp','status_of_ac','status_of_ups','status_of_servera','status_of_serverb','remarks')
     scctv_d = scctv_d.filter(emp_id=id).order_by('-p_id') 
     return render(request,'engineer/scctv/scctvrepsub.html',{'id':id,'scctv_d':scctv_d,'supdetails':supdetails}) 
   else :
      messages.add_message(request,30, 'Unauthorized Access')
      return routebackscctvd(request, uid)  
 else : 
     return render(request,'login/login.html')
 
def editscctvdaily(request, p_id) :
 if request.session.has_key('uid'):
   temp = models.Scctvdaily.objects.all().values('status').order_by('-date').filter(date=date.today())[0]['status']
   emp_id = models.Scctvdaily.objects.all().values('emp_id').filter(p_id=p_id)[0]['emp_id']
   uid=request.session['uid'] 
   if int(uid) == int(emp_id) and temp == "PENDING" :
     emp_id = models.Scctvdaily.objects.all()
     emp_id = emp_id.values('emp_id').filter(p_id=p_id)[0]['emp_id']
     scctvd = models.Scctvdaily.objects.all()
     scctv_d = scctvd.filter(emp_id=emp_id).order_by('-p_id')     
     scctvd = scctvd.filter(p_id=p_id)
     scctv_id = scctvd.values('p_id').filter(p_id=p_id)[0]['p_id']
     scctvdlogs = models.Scctvdlogs.objects.all()
     scctvdlogs = scctvdlogs.filter(date=date.today()).order_by('-log_id')    
     supdetails = models.Supervisor.objects.all()
     supdetails = supdetails.values('name','contact','email').filter(dept='S')
     return render(request,'engineer/scctv/editscctvrepsub.html',{'supdetails':supdetails,'scctvd':scctvd,'id':scctv_id,'scctv_d':scctv_d,'scctvdlogs':scctvdlogs}) 
   else :
     return routebackscctvd(request, uid)  
 else : 
     return render(request,'login/login.html')
 
def upscctvdaily(request, id) :
 if request.session.has_key('uid'):
   uid=request.session['uid'] 
   emp_id = models.Scctvdaily.objects.all()
   emp_id = emp_id.values('emp_id').filter(p_id=id)[0]['emp_id']
   if int(uid) == int(emp_id) :
    currtime = datetime.now().strftime("%H:%M:%S")
    currdate= date.today()
    cursor = connection.cursor() 
    p_id = models.Scctvdaily.objects.all()
    p_id = p_id.values('p_id')
    p_id = p_id.order_by('-p_id')
    p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
    ups=request.POST['ups']
    ser = request.POST['ser']
    vrm = request.POST['vrm']
    vrs=request.POST['vrs']
    rrs=request.POST['rrs']
    vms=request.POST['vms']
    ivms=request.POST['ivms']
    equip=request.POST['equip']
    remarks=request.POST['remarks']
    
    temp=models.Scctvdaily.objects.get(p_id=id)
    temp.ups_battery_indication=ups
    temp.servers_on_condition=ser
    temp.nas_status_in_vmsorvrm=vrm
    temp.recording_active_status_vrs_server=vrs
    temp.recording_active_status_rrs_server=rrs
    temp.database_status_vms=vms
    temp.cameras_ivms=ivms
    temp.eqpt_cleaning=equip
    temp.date=date.today()
    temp.time=datetime.now().strftime("%H:%M:%S")
    temp.save()
    p_id = models.Scctvdaily.objects.all()
    p_id = p_id.values('p_id')
    p_id = p_id.order_by('-p_id')
    p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
    
    if ups == "FULL" and ser == "OK" and vrm == 'OK' and vrs == 'EQUALS TO TOTAL CAMERA' and ivms == 'OK' and vms == "OK" and equip == 'CARRIED OUT' and rrs == "PAUSE" :
          f=1
          status = "COMPLETED"
          value = "All parameters NORMAL"
          val = (emp_id,id,remarks,value,currdate,currtime)
          sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s ,%s,%s, %s)"
          cursor.execute(sql,val)
          cursor.execute("update scctvdaily set unit_incharge_approval = %s where p_id = %s",[None,p_id])
          cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['11'])
          cursor.execute("update dgmreports set r_count = r_count - 1 where r_id = %s",['10'])
  
    else :
          f=2   
          status = "PENDING"
          # added new lines and new variable remarks1
          val = (emp_id,p_id,"Procedure Followed",remarks,currdate,currtime)
          sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
          cursor.execute(sql,val)  
          
    cursor.execute("update scctvdaily set status = %s where p_id = %s",[status,p_id])
    
    if ups == 'DISCHARGED' :
         f=0
         remarks1 = "UPS Battery Indication is 'DISCHARGED' "
         val = (emp_id,id,remarks1,ups,currdate,currtime)
         sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)

        
    if ser == 'NOT OK' :
         f=0
         remarks1 = "ALL SERVERS NOT IN ON STATE"
         val = (emp_id,id,remarks1,ser,currdate,currtime)
         sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)
        #  print(statusofac)
    if vrm == 'NOT OK' :
         f=0
         remarks1 = "NAS status in VMS/VRM is NOT OK "
         val = (emp_id,id,remarks1,vrm,currdate,currtime)
         sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)
    if vrs == 'NONE' :
         f=0
         remarks1 = "status of all VRS servers is NONE"
         val = (emp_id,id,remarks1,vrs,currdate,currtime)
         sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)
    if rrs!= 'PAUSE':
         f=0
         remarks1 = "Status of RRS camera is "+rrs
         val = (emp_id,id,remarks1,rrs,currdate,currtime)
         sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)
    if vms == "NOT OK"  :
         f=0
         remarks1 = "Status of vms server is NOT OK"
         val = (emp_id,id,remarks1,vms,currdate,currtime)
         sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)

    if ivms == "NOT OK"  :
         remarks1 = "Status of ivms server is NOT OK"
         val = (emp_id,id,remarks1,ivms,currdate,currtime)
         sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)
    
    if equip=="NOT CARRIED OUT" :
         remarks1 = "Cleaning of equipments not carried out"
         val = (emp_id,id,remarks1,equip,currdate,currtime)
         sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)
    
    scctv_d = models.Scctvdaily.objects.all()
    scctv_d = scctv_d.filter(emp_id=emp_id)  
    scctvd = scctv_d.order_by('-p_id')   
    scctv_d = scctv_d.filter(date=currdate)     
    scctvdlogs = models.Scctvdlogs.objects.all()
    scctvdlogs = scctvdlogs.filter(date=date.today()).order_by('-log_id')    
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='S')
     
    return render(request,'engineer/scctv/scctvdailyrep.html',{'supdetails':supdetails,'scctv_d':scctvd,'id':emp_id,'scctvd':scctv_d[0],'scctvdlogs':scctvdlogs})
 else : 
     return render(request,'login/login.html')
    
def scctvdrepsubm(request, id) :
 if request.session.has_key('uid'):  
    cursor = connection.cursor()
    currdate= date.today()
    currtime = datetime.now().strftime("%H:%M:%S")
    a_id = models.Engineer.objects.all()
    a_id = a_id.values('a_id').filter(emp_id=id)[0]['a_id']
    a_id=str(a_id)
    id=str(id)
    ups=request.POST['ups']
    ser = request.POST['ser']
    vrm = request.POST['vrm']
    vrs=request.POST['vrs']
    rrs=request.POST['rrs']
    vms=request.POST['vms']
    ivms=request.POST['ivms']
    equip=request.POST['equip']
    status=""
    
    temp=models.Scctvdaily(ups_battery_indication=ups,
            servers_on_condition=ser,
            nas_status_in_vmsorvrm=vrm,
            recording_active_status_vrs_server=vrs,
            recording_active_status_rrs_server=rrs,
            database_status_vms=vms,
            cameras_ivms=ivms,
            eqpt_cleaning=equip,
            
            date=date.today(),
            time=datetime.now().strftime("%H:%M:%S"),
            a_id=a_id,
            emp_id=id,
            f_id=2
         )
    temp.save()
    p_id = models.Scctvdaily.objects.all()
    p_id = p_id.values('p_id')
    p_id = p_id.order_by('-p_id')
    p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
    
    if ups == "FULL" and ser == "OK" and vrm == 'OK' and vrs == 'EQUALS TO TOTAL CAMERA' and ivms == 'OK' and vms == "OK" and equip == 'CARRIED OUT' and rrs == "PAUSE" :
          f=1
          status = "COMPLETED"
          remarks = "Parameters normal at the first submit!"
          value = "All parameters NORMAL"
          val = (id,p_id,remarks,value,currdate,currtime)
          sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
          cursor.execute(sql,val)
          cursor.execute("update scctvdaily set unit_incharge_approval = %s where p_id = %s",[None,p_id])
          cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['11'])
  
   
    else :
          f=2   
          status = "PENDING"
          cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['10'])
  
    cursor.execute("update scctvdaily set status = %s where p_id = %s",[status,p_id])
    
    if ups == 'DISCHARGED' :
        
         remarks = "UPS Battery Indication is 'DISCHARGED' "
         val = (id,p_id,remarks,ups,currdate,currtime)
         sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)
    if ser == 'NOT OK' :
         remarks = "ALL SERVERS NOT IN ON STATE"
         val = (id,p_id,remarks,ser,currdate,currtime)
         sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)
        #  print(statusofac)
    if vrm == 'NOT OK' :
         remarks = "NAS status in VMS/VRM is NOT OK "
         val = (id,p_id,remarks,vrm,currdate,currtime)
         sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)
    if vrs == 'NONE' :
         remarks = "status of all VRS servers is NONE"
         val = (id,p_id,remarks,vrs,currdate,currtime)
         sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)
    if rrs!= 'PAUSE':
         remarks = "Status of RRS camera is "+rrs
         val = (id,p_id,remarks,rrs,currdate,currtime)
         sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)
    if vms == "NOT OK"  :
         remarks = "Status of vms server is NOT OK"
         val = (id,p_id,remarks,vms,currdate,currtime)
         sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)
    
    if equip=="NOT CARRIED OUT" :
         remarks = "Cleaning of equipments not carried out"
         val = (id,p_id,remarks,equip,currdate,currtime)
         sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)
    
    scctv_d = models.Scctvdaily.objects.all()
    # scctv_d = scctv_d.values('p_id','date','time','status','room_temp','status_of_ac','status_of_ups','status_of_servera','status_of_serverb','remarks')
    scctv_d = scctv_d.filter(emp_id=id)  
    scctvd = scctv_d.order_by('-p_id')   
    scctv_d = scctv_d.filter(date=currdate)     
    scctvdlogs = models.Scctvdlogs.objects.all()
    scctvdlogs = scctvdlogs.filter(date=date.today()).order_by('-log_id')    
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='S')
     
     #'datetime_of_servers_wrt_gps_clk','status_of_disk_array','vhftx_atis_status','vhfrx_atis_status','scctv_update','audio_quality','remarks','unit_incharge_approval')
    return render(request,'engineer/scctv/scctvdailyrep.html',{'supdetails':supdetails,'scctv_d':scctvd,'id':id,'scctvd':scctv_d[0],'scctvdlogs':scctvdlogs})
 else : 
     return render(request,'login/login.html')
 
def repsuberrors(request,p_id, id):
 if request.session.has_key('uid'): 
   uid=request.session['uid'] 
#    print("here")
   if int(uid) == int(id) :
    # cursor = connection.cursor() 
    scctvd = models.Scctvdaily.objects.all()
    # scctvd = scctvd.values('p_id','emp_id','date','time','room_temp','status','status_of_ac','status_of_ups','status_of_servera','status_of_serverb','remarks')
    scctvd = scctvd.filter(p_id=p_id)
    print(scctvd)
    return render(request,'engineer/scctv/scctvfinalrep.html',{'scctvd':scctvd[0],'p_id':p_id,'id':id}) 
   else :
    return routebackscctvd(request, uid)  
#  else : 
#     return render(request,'login/login.html')
 
def finalrepsub(request,p_id, id): 
    f=1
    cursor = connection.cursor()
    currdate= date.today()
    currtime = datetime.now().strftime("%H:%M:%S")
    value = request.POST['remarks']
    remarks = "Final submit with errors"
    val = (id,p_id,remarks,value,currdate,currtime)
    sql = "INSERT INTO scctvdlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
    cursor.execute(sql,val)
    cursor.execute("update scctvdaily set status = %s where p_id = %s",["COMPLETED WITH ERRORS",p_id])
    cursor.execute("update scctvdaily set unit_incharge_approval = %s where p_id = %s",[None,p_id])
    cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['14'])
    cursor.execute("update dgmreports set r_count = r_count - 1 where r_id = %s",['10'])
  
    if request.session.has_key('uid'):
        cursor = connection.cursor() 
        currdate = date.today()
        scctv_d = models.Scctvdaily.objects.all()
        # scctv_d = scctv_d.values('p_id','date','time','status','room_temp','status_of_ac','status_of_ups','status_of_servera','status_of_serverb','remarks')
        scctv_d = scctv_d.filter(emp_id=id)
        scctvd = scctv_d.order_by('-p_id')
        scctv_d = scctv_d.filter(date=currdate)     
        scctvdlogs = models.Scctvdlogs.objects.all()
        scctvdlogs = scctvdlogs.filter(date=date.today()).order_by('-log_id')    
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='S')
        return render(request,'engineer/scctv/scctvdailyrep.html',{'supdetails':supdetails,'scctv_d':scctvd,'id':id,'f':f,'scctvd':scctv_d[0],'scctvdlogs':scctvdlogs}) 
    else : 
        return render(request,'login/login.html')

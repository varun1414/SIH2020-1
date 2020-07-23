from django.shortcuts import render
from django.db import connection
from datetime import date,datetime,timedelta
from login import models as models
from django.core.mail import send_mail
from django.contrib import messages
from login import views 
from operator import itemgetter

def cdvordrep(request, id) :
 cursor = connection.cursor() 
 if request.session.has_key('uid') : 
   temp = cursor.execute("select date from cdvordaily where date = %s",[date.today()])    
   uid=request.session['uid'] 
   if int(uid) == int(id) and temp == 0:
     supdetails = models.Supervisor.objects.all()
     supdetails = supdetails.values('name','contact','email').filter(dept='N')
     cdvor_d = models.Cdvordaily.objects.all()
     cdvor_d = cdvor_d.values('p_id','date','time','azimuth_angle','number_30hz_modulation','number_9960hz_modulation','number_9960hz_deviation','field_intensity','remarks')
     cdvor_d = cdvor_d.filter(emp_id=id).order_by('-p_id') 
     return render(request,'engineer/cdvor/cdvorrepsub.html',{'id':id,'cdvor_d':cdvor_d,'supdetails':supdetails}) 
   else :
     messages.add_message(request,30, 'Unauthorized Access')
     return routebackdatisd(request, uid)  
 else : 
     return render(request,'login/login.html')

def cdvordrepsubm(request, id) :
 if request.session.has_key('uid'):  
    cursor = connection.cursor()
    currdate= date.today()
    currtime = datetime.now().strftime("%H:%M:%S")
    a_id = models.Engineer.objects.all()
    a_id = a_id.values('a_id').filter(emp_id=id)[0]['a_id']
    azimuth_angle=''
    number_30hz_modulation=''
    number_9960hz_modulation=''
    number_9960hz_deviation=''
    field_intensity=''
    azimuth_angle=request.POST['Azimuth angle']
    number_30hz_modulation = request.POST['30Hz modulation']
    number_9960hz_modulation = request.POST['9960Hz modulation']
    number_9960hz_deviation = request.POST['9960Hz deviation']
    field_intensity = request.POST['Field intensity']
    status = ""
    sql = "INSERT INTO cdvordaily (a_id,emp_id,status,f_id,date,time,Azimuth_angle,30Hz_modulation,9960Hz_modulation,9960Hz_deviation,field_intensity) VALUES (%s, %s,%s,%s,%s,%s,%s, %s, %s, %s, %s)"
    val = (a_id,id,status,'1',date.today(),datetime.now().strftime("%H:%M:%S"),azimuth_angle,number_30hz_modulation,number_9960hz_modulation,number_9960hz_deviation,field_intensity)
    cursor.execute(sql, val)
   
    p_id = models.Cdvordaily.objects.all()
    p_id = p_id.values('p_id')
    p_id = p_id.order_by('-p_id')
    p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
    
    if azimuth_angle < '25' and (number_30hz_modulation >='28' and number_30hz_modulation <= '30') and (number_9960hz_modulation >= '28' and number_9960hz_modulation <= '30') and (number_9960hz_deviation >= '15' and number_9960hz_deviation <= '17') and (field_intensity >= '-1' and field_intensity <= '1'):
          f=1
          status = "COMPLETED"
          remarks = "Parameters normal at the first submit!"
          value = "All parameters NORMAL"
          val = (id,p_id,remarks,value,currdate,currtime)
          sql = "INSERT INTO cdvordlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
          cursor.execute(sql,val)
          cursor.execute("update cdvordaily set unit_incharge_approval = %s where p_id = %s",[None,p_id])
          cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['8'])
          
    else :
          f=2   
          status = "PENDING"
          cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['7'])
          
    cursor.execute("update cdvordaily set status = %s where p_id = %s",[status,p_id])
    f=0
    
    if azimuth_angle >= '25' :
         remarks = "Azimuth angle exceeds 25 degrees"
         val = (id,p_id,remarks,azimuth_angle,currdate,currtime)
         sql = "INSERT INTO cdvordlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)
    if number_30hz_modulation < '28' or number_30hz_modulation > '30' :
         remarks = "30Hz modulation not in specified range"
         val = (id,p_id,remarks,number_30hz_modulation,currdate,currtime)
         sql = "INSERT INTO cdvordlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)
         print(number_30hz_modulation)
    if number_9960hz_modulation <'28' or number_9960hz_modulation > '30' :
         remarks = "9960Hz modulation not in specified range"
         val = (id,p_id,remarks,number_9960hz_modulation,currdate,currtime)
         sql = "INSERT INTO cdvordlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)
    if number_9960hz_deviation < '15' or number_9960hz_deviation > '17':
         remarks = "9960Hz modulation not in specified range"
         val = (id,p_id,remarks,number_9960hz_deviation,currdate,currtime)
         sql = "INSERT INTO cdvordlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)
    if field_intensity < '-1' or field_intensity > '1':
         remarks = "Field intensity not in specified range"
         val = (id,p_id,remarks,field_intensity,currdate,currtime)
         sql = "INSERT INTO cdvordlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s,%s,%s,%s,%s)"
         cursor.execute(sql,val)
    
    cdvor_d = models.Cdvordaily.objects.all()
    cdvor_d = cdvor_d.values('p_id','date','time','status','azimuth_angle','number_30hz_modulation','number_9960hz_modulation','number_9960hz_deviation','field_intensity','remarks')
    cdvor_d = cdvor_d.filter(emp_id=id)  
    cdvord = cdvor_d.order_by('-p_id')   
    cdvor_d = cdvor_d.filter(date=currdate)     
    cdvordlogs = models.Cdvordlogs.objects.all()
    cdvordlogs = cdvordlogs.filter(date=date.today()).order_by('-log_id')    
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='C')
     
     #'datetime_of_servers_wrt_gps_clk','status_of_disk_array','vhftx_atis_status','vhfrx_atis_status','datis_update','audio_quality','remarks','unit_incharge_approval')
    return render(request,'engineer/cdvor/cdvordailyrep.html',{'supdetails':supdetails,'cdvor_d':cdvor_d,'id':id,'cdvord':cdvord,'cdvordlogs':cdvordlogs})
 else : 
     return render(request,'login/login.html')

def cdvord(request, id) :
 if request.session.has_key('uid'):
   uid=request.session['uid'] 
   if int(uid) == int(id):
     cursor = connection.cursor() 
     currdate = date.today()
     cdvor_d = models.Cdvordaily.objects.all()
     cdvor_d = cdvor_d.values('p_id','date','status','time','azimuth_angle','number_30hz_modulation','number_9960hz_modulation','number_9960hz_deviation','field_intensity','remarks')
     cdvor_d = cdvor_d.filter(emp_id=id)
     cdvord = cdvor_d.order_by('-p_id')
     cdvor_d = cdvor_d.filter(date=currdate)     
      #'datetime_of_servers_wrt_gps_clk','status_of_disk_array','vhftx_atis_status','vhfrx_atis_status','datis_update','audio_quality','remarks','unit_incharge_approval')
     if cdvor_d :
        cdvordlogs = models.Cdvordlogs.objects.all()
        cdvordlogs = cdvordlogs.filter(date=date.today()).order_by('-log_id')
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='N')
        return render(request,'engineer/cdvor/cdvordailyrep.html',{'supdetails':supdetails,'cdvor_d':cdvor_d,'id':id,'cdvord':cdvord,'cdvordlogs':cdvordlogs}) 
     else :
        messages.add_message(request,30, 'You cannot make changes to pending report!')
        return routebackcdvord(request, id)
   else :
     messages.add_message(request,30, 'You cannot make changes to pending report!')
     return routebackcdvord(request, uid)
 else : 
   return render(request,'login/login.html')

def routebackcdvord(request, id) :
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
    supdetails = supdetails.values('name','contact','email').filter(dept='N')
    
    cdr =0            
    statusd = ""
    cdvord_deadline = ""
        #!!!!!!!!!!!!!!!!!cdvor daily!!!!!!!!!!!!!!!!!!!!!!!!
    currdate = date.today()
    currtime = datetime.now().strftime("%H:%M:%S")            
    cdvordsub_on = cursor.execute("select date from cdvordaily where date = %s",[date.today()])    
    if cdvordsub_on :
        statusd = models.Cdvordaily.objects.all()
        statusd = statusd.values('date','status')
        statusd = statusd.order_by('-date')
        statusd = statusd.values('status')
        statusd = statusd.values('status').filter(a_id=1)[0]['status']
        if statusd == "PENDING" :
            cdvordsub_on = currdate
            cdvord_deadline = currdate
            cdr=0
        elif statusd == "COMPLETED" :
            cdvord_deadline = currdate + timedelta(days=1)
            cdvordsub_on = currdate
            cdr =1 
        elif statusd == "COMPLETED WITH ERRORS" :
            cdvord_deadline = date.today() + timedelta(days=1)
            cdvordsub_on = currdate
            cdr = 1
   
    else :
        cdvord_deadline = models.Cdvordaily.objects.all()
        cdvord_deadline = cdvord_deadline.values('date')
        cdvord_deadline = cdvord_deadline.order_by('-date')
        cdvord_deadline = cdvord_deadline.values('date').filter(a_id=1)[0]['date']
        cdvordsub_on = cdvord_deadline
        cdvord_deadline = cdvord_deadline + timedelta(days=2)
        tempdate = cdvordsub_on + timedelta(days=1)
        i = 1 
        while i == 1 and tempdate != date.today() : 
         if (cdvord_deadline <= date.today()) :    
            #remarks = "---Report not submitted---"
            #statusd = "COMPLETED"
            #val = (tempdate,currtime,'1',id,statusd,'2',remarks)
            #sql = "INSERT INTO datisdaily (date,time,a_id,emp_id,status,f_id,remarks) values (%s ,%s,%s,%s,%s, %s,%s)"
            #cursor.execute(sql,val)  
            cdvordsub_on = date.today()-timedelta(days=1)    
            tempdate = tempdate + timedelta(days=1)
         else : 
            break
        cdvord_deadline = date.today()
       
    #!!!!!!!!!!!!!!!!!!!!!!!cdvor weekly!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    p_id = models.Cdvorweekly.objects.all()
    p_id = p_id.values('p_id')
    p_id = p_id.order_by('-p_id')
    p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
    currdate = date.today()
    wdate = models.Cdvorweekly.objects.all()
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
    cwr = 0
    cdvorwsub_on = temp
    cdvorwsub_deadline =  wdate 
    status = ""
    status = models.Cdvorweekly.objects.all()
    status = status.values('date','status','unit_incharge_approval')
    status = status.order_by('-date')
    uia = status
    uia = uia.values('unit_incharge_approval')
    uia = uia.values('unit_incharge_approval').filter(a_id=1)[0]['unit_incharge_approval']
    status = status.values('status')
    status = status.values('status').filter(a_id=1)[0]['status']
    flag = cursor.execute("select date from cdvorweekly where date = %s",[date.today()])    
        
    if currdate > wdate :  #if it goes beyond 7 days
        cwr = 0
    if flag :    
        if  temp1 < temp : #report submitted after deadline
            cdvorwsub_deadline = temp1    
            if status == "COMPLETED" or status == "COMPLETED WITH ERRORS" :
                cwr=1
            elif status == "PENDING" :
                cwr=0
            
        elif temp == temp1 and temp == currdate : # report submitted on same day as deadline
            cdvorwsub_deadline = temp    
            if status == "COMPLETED" or status == "COMPLETED WITH ERRORS" :
                cwr=1  
            elif status == "PENDING" :
                cwr=0
            
        elif temp1 < wdate and temp1 > temp : #report submitted before the deadline 
            cdvorwsub_deadline = temp1   
            if status == "COMPLETED" or status == "COMPLETED WITH ERRORS" :
                cwr=1  
            elif status == "PENDING" :
                cwr=0
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!cdvor monthly!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    p_id = models.Cdvormonthly.objects.all()
    p_id = p_id.values('p_id')
    p_id = p_id.order_by('-p_id')
    p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
    currdate = date.today()
    wdatem = models.Cdvormonthly.objects.all()
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
    cmr = 0
    cdvormsub_on = temp
    cdvormsub_deadline =  wdatem 
    statusm = ""  # status
    statusm = models.Cdvormonthly.objects.all()
    statusm = statusm.values('date','status','unit_incharge_approval')
    statusm = statusm.order_by('-date')
    uia = statusm
    uia = uia.values('unit_incharge_approval')
    uia = uia.values('unit_incharge_approval').filter(a_id=1)[0]['unit_incharge_approval']
    statusm = statusm.values('status')
    statusm = statusm.values('status').filter(a_id=1)[0]['status']
    flag = cursor.execute("select date from cdvormonthly where date = %s",[date.today()])    
    if currdate > wdatem and flag == 0 :  #if it goes beyond 30 days
        pending = wdatem 
        while pending <= (currdate - timedelta(days=1)) :
            f = cursor.execute("select date from cdvormlogs where date = %s",[pending])    
            if f == 0 : 
                remarks = "Report not submitted"
                value = "No Entry" 
                val = (id,p_id,remarks,value,pending,currtime)
                sql = "INSERT INTO cdvormlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s ,%s, %s,%s)"
                cursor.execute(sql,val)
            pending = pending + timedelta(days=1)    
        cmr = 0
              
    if flag :   
        if  temp1 < temp : #report submitted after deadline
            cdvormsub_deadline = temp1    
            if statusm == "COMPLETED" or statusm == "COMPLETED WITH ERRORS" :
                cmr=1  
            elif statusm == "PENDING" :
                cmr=0
            
        elif temp == temp1 and temp == currdate : # report submitted on a day same as deadline
            cdvormsub_deadline = temp    
            if statusm == "COMPLETED" or statusm == "COMPLETED WITH ERRORS" :
                print("hello")
                cmr=1  
            elif statusm == "PENDING" :
                cmr=0
            
        elif temp1 < wdatem and temp1 > temp : #report submitted before the deadline 
            cdvormsub_deadline = temp1   
            if statusm == "COMPLETED" or statusm == "COMPLETED WITH ERRORS" :
                cmr=1  
            elif statusm == "PENDING" :
                cmr=0
    
    cdvordaily=[entry for entry in models.Cdvordaily.objects.filter(emp_id=id).values().order_by('-date')]
    for item in cdvordaily:
        item.update( {"type":"Cdvordaily"})
                
    cdvorweekly=[entry for entry in models.Cdvorweekly.objects.filter(emp_id=id).values().order_by('-date')]
    for item in cdvorweekly:
        item.update( {"type":"Cdvorweekly"})

    cdvormonthly=[entry for entry in models.Cdvormonthly.objects.filter(emp_id=id).values().order_by('-date')]
    for item in cdvormonthly:
        item.update( {"type":"Cdvormonthly"})

    com=cdvordaily+[i for i in cdvorweekly] + [i for i in cdvormonthly]
    com=sorted(com,key=itemgetter('date'),reverse=True)
    for i in com:
        i.update({'token':i['p_id']})
    return render(request,'./engineer/homen.html',{'cmr':cmr,'com':com,'wdate':wdate,'supdetails':supdetails,'statusd':statusd,'status':status,'cdr':cdr,'cwr':cwr,'currdate':currdate,'name':name1,'id':id,'empdet':empdetails,'cdvordsub_on':cdvordsub_on,'cdvord_deadline':cdvord_deadline,'cdvorwsub_on':cdvorwsub_on,'cdvorwsub_deadline':cdvorwsub_deadline,'statusm':statusm,'cmr':cmr,'wdatem':wdatem,'cdvormsub_on':cdvormsub_on,'cdvormsub_deadline':cdvormsub_deadline})
  else :
    return render(request,'login/login.html')  

def cdvordailyrec(request, id) :
 if request.session.has_key('uid'):
  uid=request.session['uid'] 
  if int(uid) == int(id):
     cursor = connection.cursor() 
     cdvor_d = models.Cdvordaily.objects.all()
     cdvor_d = cdvor_d.values('p_id','date','time','status','azimuth_angle','number_30hz_modulation','number_9960hz_modulation','number_9960hz_deviation','field_intensity','unit_incharge_approval','approval_date','approval_time')
     cdvor_d = cdvor_d.filter(emp_id=id).order_by('-p_id')     
     #'datetime_of_servers_wrt_gps_clk','status_of_disk_array','vhftx_atis_status','vhfrx_atis_status','datis_update','audio_quality','remarks','unit_incharge_approval')
     return render(request,'engineer/cdvor/cdvordrecords.html',{'cdvor_d':cdvor_d,'id':id}) 
  else :
     messages.add_message(request,30, 'Unauthorized Access')
     return routebackcdvord(request, uid)
 else : 
   return render(request,'login/login.html')

def editcdvordaily(request, p_id) :
 if request.session.has_key('uid'):
   temp = models.Cdvordaily.objects.all().values('status').order_by('-date').filter(date=date.today())[0]['status']
   emp_id = models.Cdvordaily.objects.all().values('emp_id').filter(p_id=p_id)[0]['emp_id']
   uid=request.session['uid'] 
   if int(uid) == int(emp_id) and temp == "PENDING" :
     emp_id = models.Cdvordaily.objects.all()
     emp_id = emp_id.values('emp_id').filter(p_id=p_id)[0]['emp_id']
     cdvord = models.Cdvordaily.objects.all()
     cdvord = cdvord.values('p_id','emp_id','date','time','status','azimuth_angle','number_30hz_modulation','number_9960hz_modulation','number_9960hz_deviation','field_intensity','remarks')
     cdvor_d = cdvord.filter(emp_id=emp_id).order_by('-p_id')     
     cdvord = cdvord.filter(p_id=p_id)
     cdvor_id = cdvord.values('p_id').filter(p_id=p_id)[0]['p_id']
     cdvordlogs = models.Cdvordlogs.objects.all()
     cdvordlogs = cdvordlogs.filter(date=date.today()).order_by('-log_id')    
     supdetails = models.Supervisor.objects.all()
     supdetails = supdetails.values('name','contact','email').filter(dept='N')
     return render(request,'engineer/cdvor/editcdvorrepsub.html',{'supdetails':supdetails,'cdvord':cdvord,'id':cdvor_id,'cdvor_d':cdvor_d,'cdvordlogs':cdvordlogs}) 
   else :
     return routebackcdvord(request, uid)  
 else : 
     return render(request,'login/login.html')

def upcdvordaily(request, id) :
 if request.session.has_key('uid'): 
   uid=request.session['uid'] 
   emp_id = models.Cdvordaily.objects.all()
   emp_id = emp_id.values('emp_id').filter(p_id=id)[0]['emp_id']
   if int(uid) == int(emp_id) :
    currtime = datetime.now().strftime("%H:%M:%S")
    currdate= date.today()
    cursor = connection.cursor() 
    p_id = models.Cdvordaily.objects.all()
    p_id = p_id.values('p_id')
    p_id = p_id.order_by('-p_id')
    p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
    azimuth_angle=''
    number_30hz_modulation=''
    number_9960hz_modulation=''
    number_9960hz_deviation=''
    field_intensity=''
    azimuth_angle=int(request.POST['Azimuth angle'])
    number_30hz_modulation = int(request.POST['30Hz modulation'])
    number_9960hz_modulation = int(request.POST['9960Hz modulation'])
    number_9960hz_deviation = int(request.POST['9960Hz deviation'])
    field_intensity = int(request.POST['Field intensity'])
        
    remarks=request.POST['remarks']
    
    # failure cases:
    if azimuth_angle >= 25 :
         cursor.execute("update cdvordaily set Azimuth_angle = %s where p_id = %s",[azimuth_angle,id])
         remarks1 = "Azimuth angle not normal(update)"
         val = (emp_id,p_id,remarks1,azimuth_angle,currdate,currtime)
         sql = "INSERT INTO cdvordlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
         cursor.execute(sql,val)  
    else :
         cursor.execute("update cdvordaily set Azimuth_angle = %s where p_id = %s",[azimuth_angle,id])
                
    if number_30hz_modulation < 28 or number_30hz_modulation > 30 :
         cursor.execute("update cdvordaily set 30Hz_modulation = %s where p_id = %s",[number_30hz_modulation,id])
         remarks1 = "30Hz modulation not normal(update)"
         val = (emp_id,p_id,remarks1,number_30hz_modulation,currdate,currtime)
         sql = "INSERT INTO cdvordlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
         cursor.execute(sql,val)
    else :
         cursor.execute("update cdvordaily set 30Hz_modulation = %s where p_id = %s",[number_30hz_modulation,id])
         
    if number_9960hz_modulation < 28 or number_9960hz_modulation > 30 :
         cursor.execute("update cdvordaily set 9960Hz_modulation = %s where p_id = %s",[number_9960hz_modulation,id])
         remarks1 = "9960Hz modulation not normal(update)"
         val = (emp_id,p_id,remarks1,number_9960hz_modulation,currdate,currtime)
         sql = "INSERT INTO cdvordlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
         cursor.execute(sql,val)
    else :
         cursor.execute("update cdvordaily set 9960Hz_modulation = %s where p_id = %s",[number_9960hz_modulation,id])
       
    if number_9960hz_deviation < 15 or number_9960hz_deviation > 17 :
         cursor.execute("update cdvordaily set 9960Hz_deviation = %s where p_id = %s",[number_9960hz_deviation,id])
         remarks1 = "9960Hz deviation not normal(update)"
         val = (emp_id,p_id,remarks1,number_9960hz_deviation,currdate,currtime)
         sql = "INSERT INTO cdvordlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
         cursor.execute(sql,val)
    else :
         cursor.execute("update cdvordaily set 9960Hz_deviation = %s where p_id = %s",[number_9960hz_deviation,id])
         
    if field_intensity < -1 or field_intensity > 1 :
         cursor.execute("update cdvordaily set field_intensity = %s where p_id = %s",[field_intensity,id])
         remarks1 = "field intensity not normal(update)"
         val = (emp_id,p_id,remarks1,field_intensity,currdate,currtime)
         sql = "INSERT INTO cdvordlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
         cursor.execute(sql,val) 
    else :
         cursor.execute("update cdvordaily set field_intensity = %s where p_id = %s",[field_intensity,id])
     
     # if after editing , all values correct    
    if (azimuth_angle < 25 and number_30hz_modulation >= 28 and number_30hz_modulation <= 30 and number_9960hz_modulation >= 28 and number_9960hz_modulation <= 30 and number_9960hz_deviation >= 15 and number_9960hz_deviation <= 17 and field_intensity >= -1 and field_intensity <= 1):
          value = "All parameters NORMAL"
          val = (emp_id,p_id,value,remarks,currdate,currtime)
          sql = "INSERT INTO cdvordlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
          cursor.execute(sql,val)
          cursor.execute("update cdvordaily set Azimuth_angle = %s where p_id = %s",[azimuth_angle,id])
          cursor.execute("update cdvordaily set 30Hz_modulation = %s where p_id = %s",[number_30hz_modulation,id])
          cursor.execute("update cdvordaily set 9960Hz_modulation = %s where p_id = %s",[number_9960hz_modulation,id])
          cursor.execute("update cdvordaily set 9960Hz_deviation = %s where p_id = %s",[number_9960hz_deviation,id])
          cursor.execute("update cdvordaily set field_intensity = %s where p_id = %s",[field_intensity,id])
          cursor.execute("update cdvordaily set status = %s where p_id = %s",["COMPLETED",id])
          cursor.execute("update cdvordaily set unit_incharge_approval = %s where p_id = %s",[None,id])
          cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['8'])
          cursor.execute("update dgmreports set r_count = r_count - 1 where r_id = %s",['7'])
  
   
    else :
          val = (emp_id,p_id,"Procedure Followed",remarks,currdate,currtime)
          sql = "INSERT INTO cdvordlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
          cursor.execute(sql,val)  
          
    #cursor.execute("update datisdaily set remarks = %s where p_id = %s",[remarks1,id])
    cdvor_d = models.Cdvordaily.objects.all()    
    cdvor_d = cdvor_d.values('p_id','date','status','time','azimuth_angle','number_30hz_modulation','number_9960hz_modulation','number_9960hz_deviation','field_intensity','remarks')
 
    cdvord = cdvor_d
    cdvord = cdvord.filter(emp_id=emp_id).order_by('-p_id')
    cdvor_d = cdvor_d.filter(date=currdate)
    cdvordlogs = models.Cdvordlogs.objects.all()
    cdvordlogs = cdvordlogs.filter(date=date.today()).order_by('-log_id')    
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='N')
    return render(request,'engineer/cdvor/cdvordailyrep.html',{'cdvordlogs':cdvordlogs,'supdetails':supdetails,'cdvor_d':cdvor_d,'id':emp_id,'cdvord':cdvord}) 
   else :
     return routebackcdvord(request, uid)  
 else : 
     return render(request,'login/login.html')

def repsuberrors(request,p_id, id):
 if request.session.has_key('uid'): 
   uid=request.session['uid'] 
   if int(uid) == int(id) :
    cursor = connection.cursor() 
    cdvord = models.Cdvordaily.objects.all()
    cdvord = cdvord.values('p_id','emp_id','date','time','azimuth_angle','number_30hz_modulation','number_9960hz_modulation','number_9960hz_deviation','field_intensity','remarks')
    cdvord = cdvord.filter(p_id=p_id)
    return render(request,'engineer/cdvor/cdvorfinalrep.html',{'cdvord':cdvord,'p_id':p_id,'id':id}) 
   else :
    return routebackcdvord(request, uid)  
 else : 
    return render(request,'login/login.html')

def finalrepsub(request,p_id, id): 
    f=1
    cursor = connection.cursor()
    currdate= date.today()
    currtime = datetime.now().strftime("%H:%M:%S")
    value = request.POST['remarks']
    remarks = "Final submit with errors"
    val = (id,p_id,remarks,value,currdate,currtime)
    sql = "INSERT INTO cdvordlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
    cursor.execute(sql,val)
    cursor.execute("update cdvordaily set status = %s where p_id = %s",["COMPLETED WITH ERRORS",p_id])
    cursor.execute("update cdvordaily set unit_incharge_approval = %s where p_id = %s",[None,p_id])
    cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['9'])
    cursor.execute("update dgmreports set r_count = r_count - 1 where r_id = %s",['7'])
  
    if request.session.has_key('uid'):
        cursor = connection.cursor() 
        currdate = date.today()
        cdvor_d = models.Cdvordaily.objects.all()
        cdvor_d = cdvor_d.values('p_id','date','time','status','azimuth_angle','number_30hz_modulation','number_9960hz_modulation','number_9960hz_deviation','field_intensity','remarks')
        cdvor_d = cdvor_d.filter(emp_id=id)
        cdvord = cdvor_d.order_by('-p_id')
        cdvor_d = cdvor_d.filter(date=currdate)     
        cdvordlogs = models.Cdvordlogs.objects.all()
        cdvordlogs = cdvordlogs.filter(date=date.today()).order_by('-log_id')    
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='N')
        return render(request,'engineer/cdvor/cdvordailyrep.html',{'supdetails':supdetails,'cdvor_d':cdvor_d,'id':id,'f':f,'cdvord':cdvord,'cdvordlogs':cdvordlogs}) 
    else : 
        return render(request,'login/login.html')

def homecd(request, id, p_id) :
 if request.session.has_key('uid'):
   uid=request.session['uid'] 
   if int(uid) == int(id):
     cursor = connection.cursor() 
     currdate = date.today()
     cdvor_d = models.Cdvordaily.objects.all().filter(emp_id=id)
     cdvord = cdvor_d.order_by('-p_id')
     cdvor_d = cdvor_d.filter(p_id=p_id)     
     status = cdvor_d.values('status')[0]['status']
     f=0 
     if status == "COMPLETED WITH ERRORS" or status == "PENDING" :
         f = 1 
     if cdvor_d :
        cdvordlogs = models.Cdvordlogs.objects.all().filter(p_id=p_id).order_by('-log_id')
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='N')
        return render(request,'engineer/cdvor/cdvordailyrep.html',{'supdetails':supdetails,'cdvor_d':cdvor_d,'id':id,'cdvord':cdvord,'cdvordlogs':cdvordlogs,'f':f}) 
     else :
        messages.add_message(request,30, 'You cannot make changes to pending report!')
        return routebackcdvord(request, id)
   else :
       return routebackcdvord(request, uid)
 else : 
   return render(request,'login/login.html')

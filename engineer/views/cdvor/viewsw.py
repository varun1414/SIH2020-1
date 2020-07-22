from django.shortcuts import render
from django.db import connection
from datetime import date,datetime,timedelta
from engineer.views.cdvor.viewsd import routebackcdvord
from login import models as models
from django.contrib import messages

def cdvorwrep(request, id) :
    cursor = connection.cursor() 
    if request.session.has_key('uid'):
        temp = cursor.execute("select date from cdvorweekly where date = %s",[date.today()])    
        uid=request.session['uid'] 
        if int(uid) == int(id) and temp == 0:
            cdvor_w = models.Cdvorweekly.objects.all()
            cdvor_w = cdvor_w.values('p_id','date','time','ps_5v','ps_12v','ps_28v','outside_temp','sideband_frequency','remarks')
            cdvor_w = cdvor_w.filter(emp_id=id).order_by('-p_id')
            supdetails = models.Supervisor.objects.all()
            supdetails = supdetails.values('name','contact','email').filter(dept='N')
            return render(request,'engineer/cdvor/cdvorwrepsub.html',{'cdvor_w':cdvor_w,'id':id,'supdetails':supdetails}) 
        else: 
            return routebackcdvord(request, uid)
    else: 
        return render(request,'login/login.html')

def cdvorwrepsubw(request, id): 
    if request.session.has_key('uid'):
        a_id = models.Engineer.objects.all()
        a_id = a_id.values('a_id').filter(emp_id=id)[0]['a_id'] 
        currtime = datetime.now().strftime("%H:%M:%S")
        emp_id = models.Engineer.objects.all()
        emp_id = emp_id.values('emp_id').filter(emp_id=id)[0]['emp_id']
        currdate= date.today()
        cursor = connection.cursor() 
        ps_5v =''
        ps_12v =''
        ps_28v =''
        outside_temp =''
        sideband_frequency =''
        ps_5v = float(request.POST['PS 5V'])
        ps_12v = float(request.POST['PS 12V'])
        ps_28v = float(request.POST['PS 28V'])
        outside_temp = float(request.POST['Outside temp'])
        sideband_frequency = float(request.POST['Sideband frequency'])
        
        sql = "INSERT INTO cdvorweekly (date,time,a_id,f_id,emp_id,status,ps_5v, ps_12v, ps_28v, outside_temp, sideband_frequency) VALUES (%s,%s,%s,%s,%s,%s, %s,%s, %s, %s, %s)"
        val = (currdate,currtime,a_id,'1',id,"",ps_5v,ps_12v,ps_28v,outside_temp,sideband_frequency)
        cursor.execute(sql, val)
        p_id = models.Cdvorweekly.objects.all()
        p_id = p_id.values('p_id')
        p_id = p_id.order_by('-p_id')
        p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
        print(p_id)
        f=2
        if ps_5v < 4.75 or ps_5v > 5.25:
            f=3
            remarks = "PS 5V not in range"
            val = (id,p_id,remarks,ps_5v,currdate,currtime)
            sql = "INSERT INTO cdvorwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
            cursor.execute(sql,val)
        
        if ps_12v < 11.5 or ps_12v > 12.5:
            f=3
            remarks = "PS 12V not in range"
            val = (id,p_id,remarks,ps_12v,currdate,currtime)
            sql = "INSERT INTO cdvorwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
            cursor.execute(sql,val)
            
        if ps_28v < 27 or ps_28v > 29 :
            f=3
            remarks = "PS 28V not in range"
            val = (id,p_id,remarks,ps_28v,currdate,currtime)
            sql = "INSERT INTO cdvorwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
            cursor.execute(sql,val)
        if outside_temp < -25 or outside_temp > 70:
            f=3
            remarks = "Outside temperature not in range"
            val = (id,p_id,remarks,outside_temp,currdate,currtime)
            sql = "INSERT INTO cdvorwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
            cursor.execute(sql,val) 
        if sideband_frequency != 10001:
            f=3
            remarks = "sideband frequency not equal to 10001 Hz"
            val = (id,p_id,remarks,sideband_frequency,currdate,currtime)
            sql = "INSERT INTO cdvorwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
            cursor.execute(sql,val)
        
        if f == 2:
            status = "COMPLETED"
            remarks = "Parameters normal at the first submit!"
            value = "All parameters NORMAL"
            val = (id,p_id,remarks,value,currdate,currtime)
            sql = "INSERT INTO cdvorwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
            cursor.execute(sql,val)
            cursor.execute("update cdvorweekly set unit_incharge_approval = %s where p_id = %s",[None,p_id])
            cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['19'])
          
        else :
            status = "PENDING"   
            cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['18'])
   
        print(status)    
        cursor.execute("update cdvorweekly set status = %s where p_id = %s",[status,p_id])
        cdvor_w = models.Cdvorweekly.objects.all()
        cdvor_w = cdvor_w.values('p_id','date','time','status','ps_5v','ps_12v','ps_28v','outside_temp','sideband_frequency','remarks')
        cdvorw = cdvor_w.filter(emp_id=id).order_by('-p_id')
        cdvor_w = cdvor_w.filter(date=currdate)
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='N')
        cdvorwlogs = models.Cdvorwlogs.objects.all()
        cdvorwlogs = cdvorwlogs.filter(date=date.today()).order_by('-log_id')    
        
        return render(request,'engineer/cdvor/cdvorweeklyrep.html',{'cdvorwlogs':cdvorwlogs,'cdvor_w':cdvor_w,'id':id,'cdvorw':cdvorw,'supdetails':supdetails})      
    else : 
        return render(request,'login/login.html')

def editcdvorweekly(request, p_id) :
 if request.session.has_key('uid'):
   temp = models.Cdvorweekly.objects.all().values('status').order_by('-date').filter(date=date.today())[0]['status']
   emp_id = models.Cdvorweekly.objects.all().values('emp_id').filter(p_id=p_id)[0]['emp_id']
   uid=request.session['uid'] 
   if int(uid) == int(emp_id) and temp == "PENDING" :
    cursor = connection.cursor() 
    emp_id = models.Cdvorweekly.objects.all()
    emp_id = emp_id.values('emp_id').filter(p_id=p_id)[0]['emp_id']
    cdvorw = models.Cdvorweekly.objects.all()
    cdvorw = cdvorw.values('p_id','date','time','status','emp_id','ps_5v','ps_12v','ps_28v','outside_temp','sideband_frequency','remarks')
    cdvor_w = cdvorw.filter(emp_id=emp_id).order_by('-p_id')
    cdvorw = cdvorw.filter(p_id=p_id)
    cdvor_id = cdvorw.values('p_id').filter(p_id=p_id)[0]['p_id']
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='N')
    cdvorwlogs = models.Cdvorwlogs.objects.all()
    cdvorwlogs = cdvorwlogs.filter(date=date.today()).order_by('-log_id')    
    return render(request,'engineer/cdvor/editcdvorwrepsub.html',{'cdvorwlogs':cdvorwlogs,'cdvorw':cdvorw,'id':cdvor_id,'cdvor_w':cdvor_w,'supdetails':supdetails})
   else : 
    return routebackcdvord(request, uid)
 else : 
    return render(request,'login/login.html')

def cdvorw(request, id) :
 if request.session.has_key('uid'):
   uid=request.session['uid'] 
   if int(uid) == int(id):
    cdvor_w = models.Cdvorweekly.objects.all()
    cdvor_w = cdvor_w.values('p_id','date','time','status','ps_5v','ps_12v','ps_28v','outside_temp','sideband_frequency','remarks')
    cdvor_w = cdvor_w.filter(emp_id=id)
    cdvorw = cdvor_w.order_by('-p_id')
    cdvor_w = cdvor_w.filter(date=date.today())
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='N')
    cdvorwlogs = models.Cdvorwlogs.objects.all()
    cdvorwlogs = cdvorwlogs.filter(date=date.today()).order_by('-log_id')    
    if cdvor_w :
       return render(request,'engineer/cdvor/cdvorweeklyrep.html',{'cdvorwlogs':cdvorwlogs,'supdetails':supdetails,'cdvor_w':cdvor_w,'id':id,'cdvorw':cdvorw}) 
    else :
       messages.add_message(request,30, 'You cannot make changes to pending report!')
       return routebackcdvord(request, id)
   else : 
     return routebackcdvord(request, uid)
   
 else : 
    return render(request,'login/login.html')

def repsubwerrors(request,p_id,id):
 if request.session.has_key('uid'):
   uid=request.session['uid'] 
   if int(uid) == int(id):
    cursor = connection.cursor() 
    cdvorw = models.Cdvorweekly.objects.all()
    cdvorw = cdvorw.values('p_id','date','time','status','emp_id','ps_5v','ps_12v','ps_28v','outside_temp','sideband_frequency','remarks')
    cdvorw = cdvorw.filter(p_id=p_id)
    return render(request,'engineer/cdvor/cdvorwfinalrep.html',{'cdvorw':cdvorw,'p_id':p_id,'id':id})
   else : 
    return routebackcdvord(request, uid)
 else : 
   return render(request,'login/login.html')

def upcdvorweekly(request, id) :
    p_id = models.Cdvorweekly.objects.all()
    p_id = p_id.values('p_id')
    p_id = p_id.order_by('-p_id')
    p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
    currdate= date.today()
    currtime = datetime.now().strftime("%H:%M:%S")
    emp_id = models.Cdvorweekly.objects.all()
    emp_id = emp_id.values('emp_id').filter(p_id=id)[0]['emp_id']
    cursor = connection.cursor() 
    
    remarks=request.POST['remarks']
    
    ps_5v = float(request.POST['PS 5V'])
    ps_12v = float(request.POST['PS 12V'])
    ps_28v = float(request.POST['PS 28V'])
    outside_temp = float(request.POST['Outside temp'])
    sideband_frequency = float(request.POST['Sideband frequency'])
    
    f=2
    # Failure cases
    
    if ps_5v < 4.75 or ps_5v > 5.25:
        f=3
        cursor.execute("update cdvorweekly set PS_5V = %s where p_id = %s",[ps_5v,id])
        remarks1 = "PS 5V reading not correct (update)" 
        val = (emp_id,p_id,remarks1,ps_5v,currdate,currtime)
        sql = "INSERT INTO cdvorwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else:
        cursor.execute("update cdvorweekly set PS_5V = %s where p_id = %s",[ps_5v,id])    
    
    if ps_12v < 11.5 or ps_12v > 12.5:
        f=3
        cursor.execute("update cdvorweekly set PS_12V = %s where p_id = %s",[ps_12v,id])
        remarks1 = "PS 12V not in correct range(update)"
        val = (emp_id,p_id,remarks1,ps_12v,currdate,currtime)
        sql = "INSERT INTO cdvorwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else:
        cursor.execute("update cdvorweekly set PS_12V = %s where p_id = %s",[ps_12v,id])
            
    if ps_28v < 27 or ps_28v > 29:
        f=3
        cursor.execute("update cdvorweekly set PS_28V = %s where p_id = %s",[ps_28v,id])
        remarks1 = "PS 28V value not in normal range(update)"
        val = (emp_id,p_id,remarks1,ps_28v,currdate,currtime)
        sql = "INSERT INTO cdvorwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else :
        cursor.execute("update cdvorweekly set PS_28V = %s where p_id = %s",[ps_28v,id])
    
    if outside_temp < -25 or outside_temp > 70:
        f=3
        cursor.execute("update cdvorweekly set outside_temp = %s where p_id = %s",[outside_temp,id])
        remarks1 = "Temperature not in range -25 to 70(update)"
        val = (emp_id,p_id,remarks1,outside_temp,currdate,currtime)
        sql = "INSERT INTO cdvorwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val) 
    else :
        cursor.execute("update cdvorweekly set outside_temp = %s where p_id = %s",[outside_temp,id])
    
    if sideband_frequency != 10001 :
        f=3
        cursor.execute("update cdvorweekly set sideband_frequency = %s where p_id = %s",[sideband_frequency,id])
        remarks1 = "Sideband frequency not equal to 10001(update)"
        val = (emp_id,p_id,remarks1,sideband_frequency,currdate,currtime)
        sql = "INSERT INTO cdvorwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    else :
        cursor.execute("update cdvorweekly set sideband_frequency = %s where p_id = %s",[sideband_frequency,id])

    if ((ps_5v >= 4.75 and ps_5v <= 5.25) and (ps_12v >= 11.5 and ps_12v <= 12.5) and (ps_28v >= 27 and ps_28v <= 29) and (outside_temp >= -25 and outside_temp <= 70) and (sideband_frequency == 10001)) :
        cursor.execute("update cdvorweekly set PS_5V = %s where p_id = %s",[ps_5v,id]) 
        cursor.execute("update cdvorweekly set PS_12V = %s where p_id = %s",[ps_12v,id])  
        cursor.execute("update cdvorweekly set PS_28V = %s where p_id = %s",[ps_28v,id]) 
        cursor.execute("update cdvorweekly set outside_temp = %s where p_id = %s",[outside_temp,id])
        cursor.execute("update cdvorweekly set sideband_frequency = %s where p_id = %s",[sideband_frequency,id])
        cursor.execute("update cdvorweekly set status = %s where p_id = %s",["COMPLETED",id])
        val = (emp_id,p_id,"All parameters NORMAL",remarks,currdate,currtime)
        sql = "INSERT INTO cdvorwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
        cursor.execute("update cdvorweekly set unit_incharge_approval = %s where p_id = %s",[None,id])
        cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['19'])
        cursor.execute("update dgmreports set r_count = r_count - 1 where r_id = %s",['18'])
  
    else : 
        val = (emp_id,p_id,"Procedure Followed",remarks,currdate,currtime)
        sql = "INSERT INTO cdvorwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
      
    cdvor_w = models.Cdvorweekly.objects.all()
    cdvor_w = cdvor_w.values('p_id','date','time','status','ps_5v','ps_12v','ps_28v','outside_temp','sideband_frequency','remarks')
    cdvorw = cdvor_w.filter(emp_id=emp_id).order_by('-p_id')
    cdvor_w = cdvor_w.filter(date=currdate)
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='N')
    cdvorwlogs = models.Cdvorwlogs.objects.all()
    cdvorwlogs = cdvorwlogs.filter(date=date.today()).order_by('-log_id')    
    return render(request,'engineer/cdvor/cdvorweeklyrep.html',{'cdvorwlogs':cdvorwlogs,'cdvor_w':cdvor_w,'id':emp_id,'cdvorw':cdvorw,'supdetails':supdetails})      

def cdvorweeklyrec(request, id):
    if request.session.has_key('uid'):
        uid=request.session['uid'] 
        if int(uid) == int(id):
            cursor = connection.cursor() 
            cdvor_w = models.Cdvorweekly.objects.all()
            cdvor_w = cdvor_w.values('p_id','date','time','status','ps_5v','ps_12v','ps_28v','outside_temp','sideband_frequency','unit_incharge_approval','approval_date','approval_time')
            cdvor_w = cdvor_w.filter(emp_id=id).order_by('-p_id')
            return render(request,'engineer/cdvor/cdvorwrecords.html',{'cdvor_w':cdvor_w,'id':id}) 
        else: 
            return routebackcdvord(request, uid)
    else: 
        return render(request,'login/login.html')

def homew(request, id, p_id) :
  if request.session.has_key('uid'):
   uid=request.session['uid'] 
   if int(uid) == int(id):
    cdvor_w = models.Cdvorweekly.objects.all().filter(emp_id=id)
    cdvorw = cdvor_w.order_by('-p_id')
    cdvor_w = cdvor_w.filter(p_id=p_id)
    status = cdvor_w.values('status')[0]['status']
    f = 0 
    if status == "COMPLETED WITH ERRORS" or status == "PENDING":
        f = 1

    supdetails = models.Supervisor.objects.all().values('name','contact','email').filter(dept='N')
    cdvorwlogs = models.Cdvorwlogs.objects.all().filter(p_id=p_id).order_by('-log_id') 
    if cdvor_w :
       return render(request,'engineer/cdvor/cdvorweeklyrep.html',{'cdvorwlogs':cdvorwlogs,'supdetails':supdetails,'cdvor_w':cdvor_w,'id':id,'cdvorw':cdvorw,'f':f}) 
    else :
       return routebackcdvord(request, id)
   else : 
     return routebackcdvord(request, uid)
   
  else : 
    return render(request,'login/login.html')

def finalwrepsub(request,p_id,id):
    f=1
    print(f)
    cursor = connection.cursor()
    currdate= date.today()
    currtime = datetime.now().strftime("%H:%M:%S")
    value = request.POST['remarks']
    remarks = "Final submit with errors"
    val = (id,p_id,remarks,value,currdate,currtime)
    sql = "INSERT INTO cdvorwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
    cursor.execute(sql,val)
    cursor.execute("update cdvorweekly set status = %s where p_id = %s",["COMPLETED WITH ERRORS",p_id])
    cursor.execute("update cdvorweekly set unit_incharge_approval = %s where p_id = %s",[None,p_id])
    cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['20'])
    cursor.execute("update dgmreports set r_count = r_count - 1 where r_id = %s",['18'])
  
    #code for notification to supervisor will come over here 
    if request.session.has_key('uid'):
        cursor = connection.cursor() 
        currdate = date.today()
        cdvor_w = models.Cdvorweekly.objects.all()
        cdvor_w = cdvor_w.values('p_id','date','time','status','ps_5v','ps_12v','ps_28v','outside_temp','sideband_frequency','remarks')
        cdvorw = cdvor_w.filter(emp_id=id).order_by('-p_id')
        cdvor_w = cdvor_w.filter(date=currdate)
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='N')
        cdvorwlogs = models.Cdvorwlogs.objects.all()
        cdvorwlogs = cdvorwlogs.filter(date=date.today()).order_by('-log_id')    
    
        return render(request,'engineer/cdvor/cdvorweeklyrep.html',{'cdvorwlogs':cdvorwlogs,'cdvor_w':cdvor_w,'id':id,'f':f,'cdvorw':cdvorw,'supdetails':supdetails})      
    else : 
        return render(request,'login/login.html')

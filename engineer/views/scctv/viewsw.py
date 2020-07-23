from django.shortcuts import render
from django.db import connection
from datetime import date,datetime,timedelta
from engineer.views.scctv.viewsd import routebackscctvd
from login import models as models
from django.contrib import messages

def scctvweeklyrec(request, id):
 if request.session.has_key('uid'):
  uid=request.session['uid'] 
  if int(uid) == int(id):
     cursor = connection.cursor() 
     scctv_w = models.Scctvweekly.objects.all()
    #  scctv_w = scctv_w.values('p_id','date','time','status','serveraorb','ups_ip','ups_op','dust_free','lan_status','unit_incharge_approval','approval_date','approval_time')
     scctv_w = scctv_w.filter(emp_id=id).order_by('-p_id')
     return render(request,'engineer/scctv/scctvwrecords.html',{'scctv_w':scctv_w,'id':id}) 
  else : 
     return routebackscctvd(request, uid)
 else : 
   return render(request,'login/login.html')
    
def scctvw(request, id) :
 if request.session.has_key('uid'):
   uid=request.session['uid'] 
   if int(uid) == int(id):
    scctv_w = models.Scctvweekly.objects.all()
    # scctv_w = scctv_w.values('p_id','date','time','status','serveraorb','ups_ip','ups_op','dust_free','lan_status','remarks')
    scctv_w = scctv_w.filter(emp_id=id)
    scctvw = scctv_w.order_by('-p_id')
    scctv_w = scctv_w.filter(date=date.today())
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='S')
    scctvwlogs = models.Scctvwlogs.objects.all()
    scctvwlogs = scctvwlogs.filter(date=date.today()).order_by('-log_id')    
    if scctv_w :
       return render(request,'engineer/scctv/scctvweeklyrep.html',{'scctvwlogs':scctvwlogs,'supdetails':supdetails,'scctv_w':scctvw,'id':id,'scctvw':scctv_w[0]}) 
    else :
       return routebackscctvd(request, id)
   else : 
     return routebackscctvd(request, uid)
   
 else : 
    return render(request,'login/login.html')

def homew(request, id, p_id) :
  if request.session.has_key('uid'):
   uid=request.session['uid'] 
   if int(uid) == int(id):
    scctv_w = models.Scctvweekly.objects.all().filter(emp_id=id)
    scctvw = scctv_w.order_by('-p_id')
    scctv_w = scctv_w.filter(p_id=p_id)
    status = scctv_w.values('status')[0]['status']
    f = 0 
    if status == "COMPLETED WITH ERRORS" or status == "PENDING":
        f = 1

    supdetails = models.Supervisor.objects.all().values('name','contact','email').filter(dept='S')
    scctvwlogs = models.Scctvwlogs.objects.all().filter(date=date.today()).order_by('-log_id') 
    if scctv_w :
       return render(request,'engineer/scctv/scctvweeklyrep.html',{'scctvwlogs':scctvwlogs,'supdetails':supdetails,'scctv_w':scctvw,'id':id,'scctvw':scctv_w[0],'f':f}) 
    else :
       return routebackscctvd(request, id)
   else : 
     return routebackscctvd(request, uid)
   
  else : 
    return render(request,'login/login.html')

  

def scctvwrep(request, id) :
 cursor = connection.cursor() 
 if request.session.has_key('uid'):
   temp = cursor.execute("select date from scctvweekly where date = %s",[date.today()])    
   uid=request.session['uid'] 
   if int(uid) == int(id) and temp == 0:
    scctv_w = models.Scctvweekly.objects.all()
    # scctv_w = scctv_w.values('p_id','date','time','serveraorb','ups_ip','ups_op','dust_free','lan_status','remarks')
    scctv_w = scctv_w.filter(emp_id=id).order_by('-p_id')
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='S')
    return render(request,'engineer/scctv/scctvwrepsub.html',{'scctv_w':scctv_w,'id':id,'supdetails':supdetails}) 
   else : 
    return routebackscctvd(request, uid)
 else : 
    return render(request,'login/login.html')
    
def scctvwrepsubw(request, id) : 
 if request.session.has_key('uid'):
    a_id = models.Engineer.objects.all()
    a_id = a_id.values('a_id').filter(emp_id=id)[0]['a_id'] 
    currtime = datetime.now().strftime("%H:%M:%S")
    emp_id = models.Scctvweekly.objects.all()
    emp_id = emp_id.values('emp_id').filter(emp_id=id)[0]['emp_id']
    currdate= date.today()
    cursor = connection.cursor() 
    
    upsip=int(request.POST['upsip'])
    upsop=int(request.POST['upsop'])
    upsbat=request.POST['upsbat']
    ser=request.POST['ser']
    nas=request.POST['nas']
    sw=request.POST['sw']
    ivms=request.POST['ivms']
    free=int(request.POST['free'])
    
    status=""
    temp=models.Scctvweekly(ups_ip_voltage=upsip,
            ups_op_voltage=upsop,
            ups_battery_status=upsbat,
            server_status=ser,
            camera_nas_status_in_vrs=nas,
            workstns_n_client_softw_check=sw,
            cameras_client_ivms_softw=ivms,
            nas_free_capacity=free,
            
            
            date=date.today(),
            time=datetime.now().strftime("%H:%M:%S"),
            a_id=a_id,
            emp_id=id,
            f_id=3
         )
    temp.save()
    # sql = "INSERT INTO scctvweekly (date,time,a_id,f_id,emp_id,status,serverAorB,UPS_ip,UPS_op,Dust_free,LAN_status) VALUES (%s,%s,%s,%s,%s,%s, %s,%s, %s, %s, %s)"
    # val = (currdate,currtime,a_id,'2',id,"",serveraorb,upsip,upsop,dustfree,lanstatus)
    # cursor.execute(sql, val)
    p_id = models.Scctvweekly.objects.all()
    p_id = p_id.values('p_id')
    p_id = p_id.order_by('-p_id')
    p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
    print(p_id)
    

    if (upsip <= 235 and  upsip >= 225 and upsop <= 230 and upsop >= 220 and upsbat == "FULL" and ser == "ON" and nas == "OK" and sw == "OK" and ivms == "OK" and free != 0 ):
        status = "COMPLETED"
        remarks = "Parameters normal at the first submit!"
        value = "All parameters NORMAL"
        val = (id,p_id,remarks,value,currdate,currtime)
        sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
        cursor.execute(sql,val)
        cursor.execute("update scctvweekly set unit_incharge_approval = %s where p_id = %s",[None,p_id])
        cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['22'])
    else :
        status = "PENDING"
        cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['21'])
  
    cursor.execute("update scctvweekly set status = %s where p_id = %s",[status,p_id])
    f=0
    if not(upsip <= 235 and upsip >= 225):  
        
            f=3
            remarks = "UPS ip not in range"
            val = (id,p_id,remarks,upsip,currdate,currtime)
            sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
            cursor.execute(sql,val)
    
    
    if not(upsop <= 230 and upsop >= 220):
        f=3
        remarks = "UPS_op not in corrent range"
        val = (id,p_id,remarks,upsop,currdate,currtime)
        sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
        
    if not(ser == "ON") :
        f=3
        remarks = "Server value not normal"
        val = (id,p_id,remarks,ser,currdate,currtime)
        sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    if not(upsbat == "FULL"):
        f=3
        remarks = "UPS battery not full"
        val = (id,p_id,remarks,upsbat,currdate,currtime)
        sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val) 
    if not(nas == "OK") :
        f=3
        remarks = "camera_NAS_status_in_VRS not OK"
        val = (id,p_id,remarks,nas,currdate,currtime)
        sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    
    if not(sw == "OK") :
        f=3
        remarks = "workstns_n_client_softw_check not OK"
        val = (id,p_id,remarks,sw,currdate,currtime)
        sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    if not(ivms == "OK") :
        f=3
        remarks = "ivms not OK"
        val = (id,p_id,remarks,ivms,currdate,currtime)
        sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    if not(free != 0) :
        f=3
        remarks = "NAS_free_capacity not OK"
        val = (id,p_id,remarks,free,currdate,currtime)
        sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    
    
    
   
    print(status)    
    cursor.execute("update scctvweekly set status = %s where p_id = %s",[status,p_id])
    scctv_w = models.Scctvweekly.objects.all()
    # scctv_w = scctv_w.values('p_id','date','time','status','serveraorb','ups_ip','ups_op','dust_free','lan_status','remarks')
    scctvw = scctv_w.filter(emp_id=id).order_by('-p_id')
    scctv_w = scctv_w.filter(date=currdate)
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='S')
    scctvwlogs = models.Scctvwlogs.objects.all()
    scctvwlogs = scctvwlogs.filter(date=date.today()).order_by('-log_id')    
    
    return render(request,'engineer/scctv/scctvweeklyrep.html',{'scctvwlogs':scctvwlogs,'scctv_w':scctvw,'id':id,'scctvw':scctv_w[0],'supdetails':supdetails})      
 else : 
    return render(request,'login/login.html')
 
def editscctvweekly(request, p_id) :
 if request.session.has_key('uid'):
   temp = models.Scctvweekly.objects.all().values('status').order_by('-date').filter(date=date.today())[0]['status']
   emp_id = models.Scctvweekly.objects.all().values('emp_id').filter(p_id=p_id)[0]['emp_id']
   uid=request.session['uid'] 
   if int(uid) == int(emp_id) and temp == "PENDING" :
    cursor = connection.cursor() 
    emp_id = models.Scctvweekly.objects.all()
    emp_id = emp_id.values('emp_id').filter(p_id=p_id)[0]['emp_id']
    scctvw = models.Scctvweekly.objects.all()
    # scctvw = scctvw.values('p_id','date','time','status','emp_id','serveraorb','ups_ip','ups_op','dust_free','lan_status','remarks')
    scctv_w = scctvw.filter(emp_id=emp_id).order_by('-p_id')
    scctvw = scctvw.filter(p_id=p_id)
    scctv_id = scctvw.values('p_id').filter(p_id=p_id)[0]['p_id']
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='S')
    scctvwlogs = models.Scctvwlogs.objects.all()
    scctvwlogs = scctvwlogs.filter(date=date.today()).order_by('-log_id')    
    return render(request,'engineer/scctv/editscctvwrepsub.html',{'scctvwlogs':scctvwlogs,'scctvw':scctvw[0],'id':scctv_id,'scctv_w':scctv_w,'supdetails':supdetails})
   else : 
    return routebackscctvd(request, uid)
 else : 
    return render(request,'login/login.html')
 
def upscctvweekly(request, id) :
    p_id = models.Scctvweekly.objects.all()
    p_id = p_id.values('p_id')
    p_id = p_id.order_by('-p_id')
    p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
    currdate= date.today()
    currtime = datetime.now().strftime("%H:%M:%S")
    emp_id = models.Scctvweekly.objects.all()
    emp_id = emp_id.values('emp_id').filter(p_id=id)[0]['emp_id']
    cursor = connection.cursor() 
    upsip=int(request.POST['upsip'])
    upsop=int(request.POST['upsop'])
    upsbat=request.POST['upsbat']
    ser=request.POST['ser']
    nas=request.POST['nas']
    sw=request.POST['sw']
    ivms=request.POST['ivms']
    free=float(request.POST['free'])
    remarks = request.POST['remarks']
    temp=models.Scctvweekly.objects.get(p_id=id)
    temp.ups_ip_voltage=upsip
    temp.ups_op_voltage=upsop
    temp.ups_battery_status=upsbat
    temp.server_status=ser
    temp.camera_nas_status_in_vrs=nas
    temp.workstns_n_client_softw_check=sw
    temp.cameras_client_ivms_softw=ivms
    temp.nas_free_capacity=free
    
    temp.date=date.today()
    temp.time=datetime.now().strftime("%H:%M:%S")
            
            
         
    temp.save()
    
    if (upsip <= 235 and  upsip >= 225 and upsop <= 230 and upsop >= 220 and upsbat == "FULL" and ser == "ON" and nas == "OK" and sw == "OK" and ivms == "OK" and free != 0 ):
        status = "COMPLETED"
        value = "All parameters NORMAL"
        val = (emp_id,id,remarks,value,currdate,currtime)
        sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
        cursor.execute(sql,val)
        cursor.execute("update scctvweekly set unit_incharge_approval = %s where p_id = %s",[None,p_id])
        cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['22'])
        cursor.execute("update dgmreports set r_count = r_count - 1 where r_id = %s",['21'])
  
    else :
        status = "PENDING"
        val = (emp_id,p_id,"Procedure Followed",remarks,currdate,currtime)
        sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
        cursor.execute(sql,val)  
         
    cursor.execute("update scctvweekly set status = %s where p_id = %s",[status,p_id])
    f=0
    
    if not(upsip <= 235 and upsip >= 225):  
        f=3
        remarks1 = "UPS ip not in range"
        val = (emp_id,id,remarks1,upsip,currdate,currtime)
        sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    
    
    if not(upsop <= 230 and upsop >= 220):
        f=3
        remarks1 = "UPS_op not in corrent range"
        val = (emp_id,id,remarks1,upsop,currdate,currtime)
        sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
        
    if not(ser == "ON") :
        f=3
        remarks1 = "Server value not normal"
        val = (emp_id,id,remarks1,ser,currdate,currtime)
        sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    if not(upsbat == "FULL"):
        f=3
        remarks1 = "UPS battery not full"
        val = (emp_id,id,remarks1,upsbat,currdate,currtime)
        sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val) 
    if not(nas == "OK") :
        f=3
        remarks1 = "camera_NAS_status_in_VRS not OK"
        val = (emp_id,id,remarks1,nas,currdate,currtime)
        sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    
    if not(sw == "OK") :
        f=3
        remarks1 = "workstns_n_client_softw_check not OK"
        val = (emp_id,id,remarks1,sw,currdate,currtime)
        sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    if not(ivms == "OK") :
        f=3
        remarks1 = "ivms not OK"
        val = (emp_id,id,remarks1,ivms,currdate,currtime)
        sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    if not(free != 0) :
        f=3
        remarks1 = "NAS_free_capacity not OK"
        val = (emp_id,id,remarks1,free,currdate,currtime)
        sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
        cursor.execute(sql,val)
    print(status)    
    cursor.execute("update scctvweekly set status = %s where p_id = %s",[status,p_id])
    scctv_w = models.Scctvweekly.objects.all()
    # scctv_w = scctv_w.values('p_id','date','time','status','serveraorb','ups_ip','ups_op','dust_free','lan_status','remarks')
    scctvw = scctv_w.filter(emp_id=emp_id).order_by('-p_id')
    scctv_w = scctv_w.filter(date=currdate)
    supdetails = models.Supervisor.objects.all()
    supdetails = supdetails.values('name','contact','email').filter(dept='S')
    scctvwlogs = models.Scctvwlogs.objects.all()
    scctvwlogs = scctvwlogs.filter(date=date.today()).order_by('-log_id')    
    
    return render(request,'engineer/scctv/scctvweeklyrep.html',{'scctvwlogs':scctvwlogs,'scctv_w':scctvw,'id':emp_id,'scctvw':scctv_w[0],'supdetails':supdetails})      


def repsubwerrors(request,p_id,id):
 if request.session.has_key('uid'):
   uid=request.session['uid'] 
   print("here")
   if int(uid) == int(id):
    cursor = connection.cursor() 
    scctvw = models.Scctvweekly.objects.all()
    # scctvw = scctvw.values('p_id','date','time','status','emp_id','serveraorb','ups_ip','ups_op','dust_free','lan_status','remarks')
    scctvw = scctvw.filter(p_id=p_id)
    print(scctvw)
    return render(request,'engineer/scctv/scctvwfinalrep.html',{'scctvw':scctvw[0],'p_id':p_id,'id':id})
   else : 
    return routebackscctvd(request, uid)
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
    sql = "INSERT INTO scctvwlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
    cursor.execute(sql,val)
    cursor.execute("update scctvweekly set status = %s where p_id = %s",["COMPLETED WITH ERRORS",p_id])
    cursor.execute("update scctvweekly set unit_incharge_approval = %s where p_id = %s",[None,p_id])
    cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['23'])
    cursor.execute("update dgmreports set r_count = r_count - 1 where r_id = %s",['21'])
  
    #code for notification to supervisor will come over here 
    if request.session.has_key('uid'):
        cursor = connection.cursor() 
        currdate = date.today()
        scctv_w = models.Scctvweekly.objects.all()
        # scctv_w = scctv_w.values('p_id','date','time','status','serveraorb','ups_ip','ups_op','dust_free','lan_status','remarks')
        scctvw = scctv_w.filter(emp_id=id).order_by('-p_id')
        scctv_w = scctv_w.filter(date=currdate)
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='S')
        scctvwlogs = models.Scctvwlogs.objects.all()
        scctvwlogs = scctvwlogs.filter(date=date.today()).order_by('-log_id')    
    
        return render(request,'engineer/scctv/scctvweeklyrep.html',{'scctvwlogs':scctvwlogs,'scctv_w':scctvw,'id':id,'f':f,'scctvw':scctv_w[0],'supdetails':supdetails})      
    else : 
        return render(request,'login/login.html')



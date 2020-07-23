from django.shortcuts import render
from django.db import connection
from datetime import date,datetime
# Create your views here.
from login import models as models
from django.contrib import messages


def scctvmonthlyrec(request, id):
 if request.session.has_key('uid'):
   uid=request.session['uid'] 
   if int(uid) == int(id):
     cursor = connection.cursor() 
     scctv_m = models.scctvmonthly.objects.all()
    #  scctv_m = scctv_m.values('p_id','date','time','status','cleaning_scctv_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check')
     scctv_m = scctv_m.filter(emp_id=id).order_by('-p_id')     
     return render(request,'engineer/scctv/scctvmrecords.html',{'scctv_m':scctv_m,'id':id}) 
   else :
     messages.add_message(request,30, 'Unauthorized Access')
     return routebackdatisd(request, uid)
 else : 
   return render(request,'login/login.html')

def scctvm(request, id) :
 if request.session.has_key('uid'):
  uid=request.session['uid'] 
  if int(uid) == int(id):
      scctv_m = models.Scctvmonthly.objects.all()
      # scctv_m = scctv_m.values('p_id','date','time','status','serveraorb','ups_ip','ups_op','dust_free','lan_status','remarks')
      scctv_m = scctv_m.filter(emp_id=id)
      scctvm = scctv_m.order_by('-p_id')
      scctv_m = scctv_m.filter(date=date.today())
      supdetails = models.Supervisor.objects.all()
      supdetails = supdetails.values('name','contact','email').filter(dept='S')
      scctvmlogs = models.Scctvmlogs.objects.all()
      scctvmlogs = scctvmlogs.filter(date=date.today()).order_by('-log_id')
      print(scctv_m)    
      if scctv_m :
         return render(request,'engineer/scctv/scctvmonthlyrep.html',{'scctvmlogs':scctvmlogs,'supdetails':supdetails,'scctv_m':scctv_m,'id':id,'scctvm':scctvm}) 
      else :
         return routebackscctvd(request, id)
  else : 
     return routebackscctvd(request, uid)
   
 else : 
    return render(request,'login/login.html')

def scctvmrep(request, id) :
 cursor = connection.cursor() 
 if request.session.has_key('uid') : 
   temp = cursor.execute("select date from scctvmonthly where date = %s",[date.today()])    
   uid=request.session['uid'] 
   if int(uid) == int(id) and temp == 0:
     supdetails = models.Supervisor.objects.all()
     supdetails = supdetails.values('name','contact','email').filter(dept='S')
     scctv_m = models.Scctvmonthly.objects.all()
    #  scctv_m = scctv_m.values('p_id','date','time','status','cleaning_scctv_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check')
     scctv_m = scctv_m.filter(emp_id=id).order_by('-p_id') 
     return render(request,'engineer/scctv/scctvmrepsub.html',{'id':id,'scctv_m':scctv_m,'supdetails':supdetails}) 
   else :
      messages.add_message(request,30, 'Unauthorized Access')
      return routebackdatisd(request, uid)  
 else : 
     return render(request,'login/login.html')
 
     
def scctvmrepsub(request, id):
   a_id = models.Engineer.objects.all()
   a_id = a_id.values('a_id').filter(emp_id=id)[0]['a_id'] 
   currtime = datetime.now().strftime("%H:%M:%S")
   emp_id = models.Scctvmonthly.objects.all()
   emp_id = emp_id.values('emp_id').filter(emp_id=id)[0]['emp_id']
   currdate= date.today()
   cursor = connection.cursor() 
   upsip=int(request.POST['upsip'])
   ups15=int(request.POST['ups15'])
   upsop=int(request.POST['upsop'])
   ser=request.POST['ser']
   vrs=request.POST['vrs']
   upson=int(request.POST['upson'])
   upsoff=int(request.POST['upsoff'])
   free=int(request.POST['free'])
   ofc=request.POST['ofc']
   status=""
   eqpt=request.POST['eqpt']
   user=request.POST['user']
   temp=models.Scctvmonthly(ups_ip_voltage=upsip,
            ups_op_voltage=upsop,
            ups_battery_op_voltage_acpwron=upson,
            ups_battery_op_voltage_acpwroff=upsoff,
            ups_battery_op_voltage_after15min_acpwroff=ups15,
            server_status=ser,
            cameras_in_vrs_server=vrs,
            
            
            nas_free_capacity=free,
            ofclinkto_l2l3_switches=ofc,
            cleaning_camera_eqpt=eqpt,
            user_rights_check=user,
            date=date.today(),
            time=datetime.now().strftime("%H:%M:%S"),
            a_id=a_id,
            emp_id=id,
            f_id=3
         )
   temp.save()
   p_id = models.Scctvmonthly.objects.all()
   p_id = p_id.values('p_id')
   p_id = p_id.order_by('-p_id')
   p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']

   
   if (upsip<= 235 and  upsip >= 225 and upsop <= 230 and upsop >= 220 and upson <= 213 and upson >= 203 and upsoff <= 191 and upsoff >= 181 and ups15 <= 181 and ups15 >= 171 and ser == "ON" and vrs == "OK" and free != 0 and ofc == "BLINKING GREEN" and eqpt == "CARRIED OUT" and user == "OK" ):
       
        status = "COMPLETED"
        remarks = "Parameters normal at the first submit!"
        value = "All parameters NORMAL"
        val = (id,p_id,remarks,value,currdate,currtime)
        sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
        cursor.execute(sql,val)
        cursor.execute("update scctvmonthly set unit_incharge_approval = %s where p_id = %s",[None,p_id])
        cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['28'])
   else :
        status = "PENDING"
        cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['27'])
  
   cursor.execute("update scctvmonthly set status = %s where p_id = %s",[status,p_id])
   f=0
   if not(upsip <= 235 and upsip >= 225):  
      
          f=3
          remarks = "UPS ip not in range"
          val = (id,p_id,remarks,upsip,currdate,currtime)
          sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
          cursor.execute(sql,val)
   if not(ofc == "BLINKING GREEN" ):  
      
          f=3
          remarks = "OFClinkto_L2L3_switches not green"
          val = (id,p_id,remarks,ofc,currdate,currtime)
          sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
          cursor.execute(sql,val)
   if not(eqpt == "CARRIED OUT"):  
      
          f=3
          remarks = "eqt cleaning not done"
          val = (id,p_id,remarks,eqpt,currdate,currtime)
          sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
          cursor.execute(sql,val)
   if not(user == "OK"):  
      
          f=3
          remarks = "user_rights_check not ok"
          val = (id,p_id,remarks,user,currdate,currtime)
          sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
          cursor.execute(sql,val)  
   
   
   if not(upsop <= 230 and upsop >= 220):
      f=3
      remarks = "UPS_op not in corrent range"
      val = (id,p_id,remarks,upsop,currdate,currtime)
      sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
      cursor.execute(sql,val)
      
   if not(ser == "ON") :
      f=3
      remarks = "Server value not normal"
      val = (id,p_id,remarks,ser,currdate,currtime)
      sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
      cursor.execute(sql,val)
   if not(upson <= 213 and upson >= 203):
      f=3
      remarks = "UPS_acpwrON not in correct range"
      val = (id,p_id,remarks,upson,currdate,currtime)
      sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
      cursor.execute(sql,val) 
   if not(vrs == "OK") :
      f=3
      remarks = "VRS not OK"
      val = (id,p_id,remarks,vrs,currdate,currtime)
      sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
      cursor.execute(sql,val)
  
   if not(upsoff <= 191 and upsoff >= 181) :
      f=3
      remarks = "UPS_acpwrOFF not in correct range not OK"
      val = (id,p_id,remarks,upsoff,currdate,currtime)
      sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
      cursor.execute(sql,val)
   if not(ups15 <= 181 and ups15 >= 171) :
      f=3
      remarks = "ups_battery_op_voltage_after15min_ACpwrOFF not in range"
      val = (id,p_id,remarks,ups15,currdate,currtime)
      sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
      cursor.execute(sql,val)
   if not(free != 0) :
      f=3
      remarks = "NAS_free_capacity not OK"
      val = (id,p_id,remarks,free,currdate,currtime)
      sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
      cursor.execute(sql,val)
  
   if f == 2:
      status = "COMPLETED"
      remarks = "Parameters normal at the first submit!"
      value = "All parameters NORMAL"
      val = (id,p_id,remarks,value,currdate,currtime)
      sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
      cursor.execute(sql,val)
      cursor.execute("update scctvmonthly set unit_incharge_approval = %s where p_id = %s",[None,p_id])
  
  
   
   print(status)    
   cursor.execute("update scctvmonthly set status = %s where p_id = %s",[status,p_id])
   scctv_w = models.Scctvmonthly.objects.all()
    # scctv_w = scctv_w.values('p_id','date','time','status','serveraorb','ups_ip','ups_op','dust_free','lan_status','remarks')
   scctvw = scctv_w.filter(emp_id=id).order_by('-p_id')
   scctv_w = scctv_w.filter(date=currdate)
   supdetails = models.Supervisor.objects.all()
   supdetails = supdetails.values('name','contact','email').filter(dept='S')
  #  scctvmlogs = models.Scctvmlogs.objects.all()
  #  scctvmlogs = scctvmlogs.filter(date=date.today()).order_by('-log_id')    
  
  
   scctv_m = models.Scctvmonthly.objects.all()
  #  scctv_m = scctv_m.values('p_id','date','time','status','cleaning_scctv_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check')
   scctv_m = scctv_m.filter(emp_id=id)  
   scctvm = scctv_m.order_by('-p_id')   
   scctv_m = scctv_m.filter(date=currdate)     
   scctvmlogs = models.Scctvmlogs.objects.all()
   scctvmlogs = scctvmlogs.filter(date=date.today()).order_by('-log_id')    
   supdetails = models.Supervisor.objects.all()
   supdetails = supdetails.values('name','contact','email').filter(dept='S')

   return render(request,'engineer/scctv/scctvmonthlyrep.html',{'scctvm':scctvm,'id':id,'supdetails':supdetails,'scctvmlogs':scctvmlogs,'scctv_m':scctv_m}) 
       
def editscctvmonthly(request,p_id):
  if request.session.has_key('uid'):
   temp = models.Scctvmonthly.objects.all().values('status').order_by('-date').filter(date=date.today())[0]['status']
   emp_id = models.Scctvmonthly.objects.all().values('emp_id').filter(p_id=p_id)[0]['emp_id']
   uid=request.session['uid'] 
   if int(uid) == int(emp_id) and temp == "PENDING" :
     emp_id = models.Scctvmonthly.objects.all()
     emp_id = emp_id.values('emp_id').filter(p_id=p_id)[0]['emp_id']
     scctvm = models.Scctvmonthly.objects.all()
    #  scctvm = scctvm.values('p_id','emp_id','date','time','status','cleaning_scctv_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check')
     scctv_m = scctvm.filter(emp_id=emp_id)  
     scctv_m = scctvm.order_by('-p_id')   
     scctvm = scctvm.filter(date=date.today())     
     scctvmlogs = models.Scctvmlogs.objects.all()
     scctvmlogs = scctvmlogs.filter(date=date.today()).order_by('-log_id')    
     supdetails = models.Supervisor.objects.all()
     supdetails = supdetails.values('name','contact','email').filter(dept='S')
     return render(request,'engineer/scctv/editscctvmrepsub.html',{'supdetails':supdetails,'scctvm':scctv_m[0],'id':p_id,'scctv_m':scctv_m,'scctvmlogs':scctvmlogs}) 
   else :
     return routebackdatisd(request, uid)  
  else : 
     return render(request,'login/login.html')

def scctvmrec(request, id):
 if request.session.has_key('uid'):
  uid=request.session['uid'] 
  if int(uid) == int(id):
     cursor = connection.cursor() 
     scctv_m = models.Scctvmonthly.objects.all()
    #  scctv_w = scctv_w.values('p_id','date','time','status','serveraorb','ups_ip','ups_op','dust_free','lan_status','unit_incharge_approval','approval_date','approval_time')
     scctv_m = scctv_m.filter(emp_id=id).order_by('-p_id')
     return render(request,'engineer/scctv/scctvmrecords.html',{'scctv_m':scctv_m,'id':id}) 
  else : 
     return routebackscctvd(request, uid)
 else : 
   return render(request,'login/login.html')
 
def upscctvmonthly(request, id):
   cursor = connection.cursor() 
   currtime = datetime.now().strftime("%H:%M:%S")
   emp_id = models.Scctvmonthly.objects.all()
   emp_id = emp_id.values('emp_id').filter(p_id=id)[0]['emp_id']
   currdate= date.today()
   cursor = connection.cursor() 
   upsip=int(request.POST['upsip'])
   ups15=int(request.POST['ups15'])
   upsop=int(request.POST['upsop'])
   ser=request.POST['ser']
   vrs=request.POST['vrs']
   upson=int(request.POST['upson'])
   upsoff=int(request.POST['upsoff'])
   free=float(request.POST['free'])
   ofc=request.POST['ofc']
   status=""
   eqpt=request.POST['eqpt']
   user=request.POST['user']
   remarks=request.POST['remarks']
   temp=models.Scctvmonthly.objects.get(p_id=id)
   temp.ups_ip_voltage=upsip
   temp.ups_op_voltage=upsop
   temp.ups_battery_op_voltage_acpwron=upson
   temp. ups_battery_op_voltage_acpwroff=upsoff
   temp.ups_battery_op_voltage_after15min_acpwroff=ups15
   temp.server_status=ser
   temp.cameras_in_vrs_server=vrs
    
    
   temp. nas_free_capacity=free
   temp.ofclinkto_l2l3_switches=ofc
   temp.cleaning_camera_eqpt=eqpt
   temp. user_rights_check=user
   temp.date=date.today()
   temp.time=datetime.now().strftime("%H:%M:%S")

         
   temp.save()
   p_id = models.Scctvmonthly.objects.all()
   p_id = p_id.values('p_id')
   p_id = p_id.order_by('-p_id')
   p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']

   
   if (upsip<= 235 and  upsip >= 225 and upsop <= 230 and upsop >= 220 and upson <= 213 and upson >= 203 and upsoff <= 191 and upsoff >= 181 and ups15 <= 181 and ups15 >= 171 and ser == "ON" and vrs == "OK" and free != 0 and ofc == "BLINKING GREEN" and eqpt == "CARRIED OUT" and user == "OK" ):
       
        status = "COMPLETED"
        remarks = "Parameters normal at the first submit!"
        value = "All parameters NORMAL"
        val = (emp_id,id,remarks,value,currdate,currtime)
        sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
        cursor.execute(sql,val)
        cursor.execute("update scctvmonthly set unit_incharge_approval = %s where p_id = %s",[None,p_id])
        cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['28'])
        cursor.execute("update dgmreports set r_count = r_count - 1 where r_id = %s",['27'])
   else :
        status = "PENDING"
        val = (emp_id,p_id,"Procedure Followed",remarks,currdate,currtime)
        sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
        cursor.execute(sql,val) 
         
        
   cursor.execute("update scctvmonthly set status = %s where p_id = %s",[status,p_id])
   f=0
   if not(upsip <= 235 and upsip >= 225):  
      
          f=3
          remarks = "UPS ip not in range"
          val = (emp_id,id,remarks,upsip,currdate,currtime)
          sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
          cursor.execute(sql,val)
   if not(ofc == "BLINKING GREEN" ):  
      
          f=3
          remarks = "OFClinkto_L2L3_switches not green"
          val = (emp_id,id,remarks,ofc,currdate,currtime)
          sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
          cursor.execute(sql,val)
   if not(eqpt == "CARRIED OUT"):  
      
          f=3
          remarks = "eqt cleaning not done"
          val = (emp_id,id,remarks,eqpt,currdate,currtime)
          sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
          cursor.execute(sql,val)
   if not(user == "OK"):  
      
          f=3
          remarks = "user_rights_check not ok"
          val = (emp_id,id,remarks,user,currdate,currtime)
          sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
          cursor.execute(sql,val)  
   
   
   if not(upsop <= 230 and upsop >= 220):
      f=3
      remarks = "UPS_op not in corrent range"
      val = (emp_id,id,remarks,upsop,currdate,currtime)
      sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
      cursor.execute(sql,val)
      
   if not(ser == "ON") :
      f=3
      remarks = "Server value not normal"
      val = (emp_id,id,remarks,ser,currdate,currtime)
      sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
      cursor.execute(sql,val)
   if not(upson <= 213 and upson >= 203):
      f=3
      remarks = "UPS_acpwrON not in correct range"
      val = (emp_id,id,remarks,upson,currdate,currtime)
      sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
      cursor.execute(sql,val) 
   if not(vrs == "OK") :
      f=3
      remarks = "VRS not OK"
      val = (emp_id,id,remarks,vrs,currdate,currtime)
      sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
      cursor.execute(sql,val)
  
   if not(upsoff <= 191 and upsoff >= 181) :
      f=3
      remarks = "UPS_acpwrOFF not in correct range not OK"
      val = (emp_id,id,remarks,upsoff,currdate,currtime)
      sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
      cursor.execute(sql,val)
   if not(ups15 <= 181 and ups15 >= 171) :
      f=3
      remarks = "ups_battery_op_voltage_after15min_ACpwrOFF not in range"
      val = (emp_id,id,remarks,ups15,currdate,currtime)
      sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
      cursor.execute(sql,val)
   if not(free != 0) :
      f=3
      remarks = "NAS_free_capacity not OK"
      val = (emp_id,id,remarks,free,currdate,currtime)
      sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
      cursor.execute(sql,val)
  
   if f == 2:
      status = "COMPLETED"
      remarks = "Parameters normal at the first submit!"
      value = "All parameters NORMAL"
      val = (emp_id,id,remarks,value,currdate,currtime)
      sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
      cursor.execute(sql,val)
      cursor.execute("update scctvmonthly set unit_incharge_approval = %s where p_id = %s",[None,p_id])
  
  
   
   print(status)    
   cursor.execute("update scctvmonthly set status = %s where p_id = %s",[status,p_id])
   scctv_m = models.Scctvmonthly.objects.all()
    # scctv_w = scctv_w.values('p_id','date','time','status','serveraorb','ups_ip','ups_op','dust_free','lan_status','remarks')
   scctvm = scctv_m.filter(emp_id=emp_id).order_by('-p_id')
   scctv_m = scctv_m.filter(date=currdate)
   supdetails = models.Supervisor.objects.all()
   supdetails = supdetails.values('name','contact','email').filter(dept='S')
  #  scctvmlogs = models.Scctvmlogs.objects.all()
  #  scctvmlogs = scctvmlogs.filter(date=date.today()).order_by('-log_id')    
  
  
   scctv_m = models.Scctvmonthly.objects.all()
  #  scctv_m = scctv_m.values('p_id','date','time','status','cleaning_scctv_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check')
   scctv_m = scctv_m.filter(emp_id=emp_id)  
   scctvm = scctv_m.order_by('-p_id')   
   scctv_m = scctv_m.filter(date=currdate)     
   scctvmlogs = models.Scctvmlogs.objects.all()
   scctvmlogs = scctvmlogs.filter(date=date.today()).order_by('-log_id')    
   supdetails = models.Supervisor.objects.all()
   supdetails = supdetails.values('name','contact','email').filter(dept='S')

   return render(request,'engineer/scctv/scctvmonthlyrep.html',{'scctv_m':scctv_m,'id':emp_id,'supdetails':supdetails,'scctvmlogs':scctvmlogs,'scctvm':scctvm}) 

def repsuberrors(request,p_id, id):
 if request.session.has_key('uid'): 
   uid=request.session['uid'] 
#    print("here")
   if int(uid) == int(id) :
    # cursor = connection.cursor() 
    scctvd = models.Scctvmonthly.objects.all()
    # scctvd = scctvd.values('p_id','emp_id','date','time','room_temp','status','status_of_ac','status_of_ups','status_of_servera','status_of_serverb','remarks')
    scctvd = scctvd.filter(p_id=p_id)
    print(scctvd)
    return render(request,'engineer/scctv/scctvmfinalrep.html',{'scctvm':scctvd[0],'p_id':p_id,'id':id}) 
   else :
    return routebackscctvd(request, uid)  
 else : 
    return render(request,'login/login.html')


def finalmrepsub(request,p_id,id) :
    f=1
    cursor = connection.cursor()
    currdate= date.today()
    currtime = datetime.now().strftime("%H:%M:%S")
    value = request.POST['remarks']
    remarks = "Final submit with errors"
    val = (id,p_id,remarks,value,currdate,currtime)
    sql = "INSERT INTO scctvmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
    cursor.execute(sql,val)
    cursor.execute("update scctvmonthly set status = %s where p_id = %s",["COMPLETED WITH ERRORS",p_id])
    cursor.execute("update scctvmonthly set unit_incharge_approval = %s where p_id = %s",[None,p_id])
    cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['29'])
    cursor.execute("update dgmreports set r_count = r_count - 1 where r_id = %s",['27'])
    
    if request.session.has_key('uid'):
        cursor = connection.cursor() 
        currdate = date.today()
        scctv_m = models.Scctvmonthly.objects.all()
      #   scctv_m = scctv_m.values('p_id','date','time','status','cleaning_scctv_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check')
        scctv_m = scctv_m.filter(emp_id=id)  
        scctvm = scctv_m.order_by('-p_id')   
        scctv_m = scctv_m.filter(date=currdate)     
        scctvmlogs = models.Scctvmlogs.objects.all()
        scctvmlogs = scctvmlogs.filter(date=date.today()).order_by('-log_id')    
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='S')
        return render(request,'engineer/scctv/scctvmonthlyrep.html',{'supdetails':supdetails,'scctv_m':scctv_m,'id':id,'f':f,'scctvm':scctvm,'scctvmlogs':scctvmlogs}) 
    else : 
        return render(request,'login/login.html')

def homem(request, id, p_id) :
 if request.session.has_key('uid'):
   uid=request.session['uid'] 
   if int(uid) == int(id):
     cursor = connection.cursor() 
     currdate = date.today()
     scctv_m = models.Scctvmonthly.objects.all().filter(emp_id=id)
     scctvm = scctv_m.order_by('-p_id')
     scctv_m = scctv_m.filter(p_id=p_id)     
     status = scctv_m.values('status')[0]['status']
     f=0 
     if status == "COMPLETED WITH ERRORS" or status == "PENDING" :
         f = 1 
     if scctv_m :
        scctvmlogs = models.Scctvmlogs.objects.all().filter(p_id=p_id).order_by('-log_id')
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='S')
        return render(request,'engineer/scctv/scctvmonthlyrep.html',{'supdetails':supdetails,'scctv_m':scctv_m,'id':id,'scctvm':scctvm,'scctvmlogs':scctvmlogs,'f':f}) 
     else :
        messages.add_message(request,30, 'You cannot make changes to pending report!')
        return routebackscctv(request, id)
   else :
       return routebackscctv(request, uid)
 else : 
   return render(request,'login/login.html')


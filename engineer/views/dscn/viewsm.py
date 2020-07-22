from django.shortcuts import render
from django.db import connection
from datetime import date,datetime
# Create your views here.
from login import models as models
from django.contrib import messages

def dscnmonthlyrec(request, id):
 if request.session.has_key('uid'):
   uid=request.session['uid'] 
   if int(uid) == int(id):
     cursor = connection.cursor() 
     dscn_m = models.Dscnmonthly.objects.all()
     dscn_m = dscn_m.values('p_id','date','time','status','cleaning_dscn_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check','approval_date','approval_time')
     dscn_m = dscn_m.filter(emp_id=id).order_by('-p_id')     
     return render(request,'engineer/dscn/dscnmrecords.html',{'dscn_m':dscn_m,'id':id}) 
   else :
     messages.add_message(request,30, 'Unauthorized Access')
     return routebackdatisd(request, uid)
 else : 
   return render(request,'login/login.html')

def dscnm(request, id) :
 if request.session.has_key('uid'):
   uid=request.session['uid'] 
   if int(uid) == int(id):
     currtime = datetime.now().strftime("%H:%M:%S")
     currdate = date.today()
     dscn_m = models.Dscnmonthly.objects.all()
     dscn_m = dscn_m.values('p_id','date','emp_id','time','status','cleaning_dscn_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check','unit_incharge_approval','remarks')
     dscn_m = dscn_m.filter(emp_id=id)
     dscnm = dscn_m.order_by('-p_id')   
     dscn_m = dscn_m.filter(date=currdate)   
     uia = dscn_m.values('unit_incharge_approval')[0]['unit_incharge_approval']  
     dscnmlogs = models.Dscnmlogs.objects.all()
     dscnmlogs = dscnmlogs.filter(date=date.today()).order_by('-log_id')    
     supdetails = models.Supervisor.objects.all()
     f = 1
     if uia == "NO" :
      f = 0
     supdetails = supdetails.values('name','contact','email').filter(dept='C')
     if dscnm :        
       return render(request,'engineer/dscn/dscnmonrep.html',{'dscn_m':dscn_m,'f':f,'id':id,'dscnm':dscnm,'supdetails':supdetails,'dscnmlogs':dscnmlogs}) 
     else :
       messages.add_message(request,30, 'You cannot make changes to pending report!')
       return routebackdatisd(request, id)
   else :
     return routebackdatisd(request, uid)
 else : 
     return render(request,'login/login.html')

def dscnmrep(request, id) :
 cursor = connection.cursor() 
 if request.session.has_key('uid') : 
   temp = cursor.execute("select date from dscnmonthly where date = %s",[date.today()])    
   uid=request.session['uid'] 
   if int(uid) == int(id) and temp == 0:
     supdetails = models.Supervisor.objects.all()
     supdetails = supdetails.values('name','contact','email').filter(dept='C')
     dscn_m = models.Dscnmonthly.objects.all()
     dscn_m = dscn_m.values('p_id','date','time','status','cleaning_dscn_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check','remarks')
     dscn_m = dscn_m.filter(emp_id=id).order_by('-p_id') 
     return render(request,'engineer/dscn/dscnmrepsub.html',{'id':id,'dscn_m':dscn_m,'supdetails':supdetails}) 
   else :
      messages.add_message(request,30, 'Unauthorized Access')
      return routebackdatisd(request, uid)  
 else : 
     return render(request,'login/login.html')
 
     
def dscnmrepsub(request, id):
   a_id = models.Engineer.objects.all()
   a_id = a_id.values('a_id').filter(emp_id=id)[0]['a_id'] 
   currtime = datetime.now().strftime("%H:%M:%S")
   emp_id = models.Vhfmonthly.objects.all()
   emp_id = emp_id.values('emp_id').filter(emp_id=id)[0]['emp_id']
   currdate= date.today()
   cursor = connection.cursor() 
   cdae = request.POST['cdae']
   bbt = request.POST['bbt']
   ubvl = request.POST['ubvl']
   ancc = request.POST['ancc']
   er=request.POST['er']
   ev = request.POST['ev']
   esac=request.POST['esac']
   sql = "INSERT INTO dscnmonthly (date,time,a_id,status,emp_id,f_id,Cleaning_DSCN_associated_eqpt,Battery_backup_time_of_UPS1nUPS2,UPS_battery_voltage_on_load,Antenna_n_cable_check,Earth_resistance,EorN_voltage,eqpt_status_after_check) VALUES (%s,%s, %s,%s,%s,%s, %s, %s, %s, %s,%s, %s,%s)"
   val = (currdate,currtime,a_id,"COMPLETED",id,'3',cdae,bbt,ubvl,ancc,er,ev,esac)
   cursor.execute(sql, val)
   p_id = models.Dscnmonthly.objects.all()
   p_id = p_id.values('p_id')
   p_id = p_id.order_by('-p_id')
   p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
   remarks = "Parameters submitted to the supervisor"
   value = "Parameters as submitted in the report"
   val = (id,p_id,remarks,value,currdate,currtime)
   sql = "INSERT INTO dscnmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
   cursor.execute(sql,val)
   dscn_m = models.Dscnmonthly.objects.all()
   dscn_m = dscn_m.values('p_id','date','time','status','cleaning_dscn_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check','remarks')
   dscn_m = dscn_m.filter(emp_id=id)  
   dscnm = dscn_m.order_by('-p_id')   
   dscn_m = dscn_m.filter(date=currdate)     
   dscnmlogs = models.Dscnmlogs.objects.all()
   dscnmlogs = dscnmlogs.filter(date=date.today()).order_by('-log_id')    
   supdetails = models.Supervisor.objects.all()
   supdetails = supdetails.values('name','contact','email').filter(dept='C')
   cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['31'])
   f = 1
   return render(request,'engineer/dscn/dscnmonrep.html',{'dscn_m':dscn_m,'id':id,'f':f,'supdetails':supdetails,'dscnmlogs':dscnmlogs,'dscnm':dscnm}) 
       
def editdscnmonthly(request,p_id):
  if request.session.has_key('uid'):
   temp = models.Dscnmonthly.objects.all().values('status').order_by('-date').filter(date=date.today())[0]['status']
   emp_id = models.Dscnmonthly.objects.all().values('emp_id').filter(p_id=p_id)[0]['emp_id']
   uid=request.session['uid'] 
   if int(uid) == int(emp_id) and temp == "PENDING" :
     emp_id = models.Dscnmonthly.objects.all()
     emp_id = emp_id.values('emp_id').filter(p_id=p_id)[0]['emp_id']
     dscnm = models.Dscnmonthly.objects.all()
     dscnm = dscnm.values('p_id','emp_id','date','time','status','cleaning_dscn_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check')
     dscn_m = dscnm.filter(emp_id=emp_id)  
     dscn_m = dscnm.order_by('-p_id')   
     dscnm = dscnm.filter(date=date.today())     
     dscnmlogs = models.Dscnmlogs.objects.all()
     dscnmlogs = dscnmlogs.filter(date=date.today()).order_by('-log_id')    
     supdetails = models.Supervisor.objects.all()
     supdetails = supdetails.values('name','contact','email').filter(dept='C')
     return render(request,'engineer/dscn/editdscnmrepsub.html',{'supdetails':supdetails,'dscnm':dscnm,'id':p_id,'dscn_m':dscn_m,'dscnmlogs':dscnmlogs}) 
   else :
     return routebackdatisd(request, uid)  
  else : 
     return render(request,'login/login.html')
 
def updscnmonthly(request, id):
   cursor = connection.cursor() 
   currtime = datetime.now().strftime("%H:%M:%S")
   emp_id = models.Dscnmonthly.objects.all()
   emp_id = emp_id.values('emp_id').filter(p_id=id)[0]['emp_id']
   currdate= date.today()
   cdae = request.POST['cdae']
   bbt = request.POST['bbt']
   ubvl = request.POST['ubvl']
   ancc = request.POST['ancc']
   er=request.POST['er']
   ev = request.POST['ev']
   esac=request.POST['esac']
   value=request.POST['remarks']
   cursor.execute("update dscnmonthly set Cleaning_DSCN_associated_eqpt = %s where p_id = %s",[cdae,id]) 
   cursor.execute("update dscnmonthly set Antenna_n_Cable_check = %s where p_id = %s",[ancc,id]) 
   cursor.execute("update dscnmonthly set Battery_backup_time_of_UPS1nUPS2 = %s where p_id = %s",[bbt,id]) 
   cursor.execute("update dscnmonthly set UPS_battery_voltage_on_load = %s where p_id = %s",[ubvl,id]) 
   cursor.execute("update dscnmonthly set Earth_resistance = %s where p_id = %s",[er,id]) 
   cursor.execute("update dscnmonthly set EorN_voltage = %s where p_id = %s",[ev,id]) 
   cursor.execute("update dscnmonthly set eqpt_status_after_check = %s where p_id = %s",[esac,id]) 
   cursor.execute("update dscnmonthly set unit_incharge_approval = %s where p_id = %s",[None,id]) 
   cursor.execute("update dscnmonthly set status = %s where p_id = %s",["COMPLETED",id]) 
   
   remarks = "Parameters submitted to the supervisor after rectification"
   val = (emp_id,id,remarks,value,currdate,currtime)
   sql = "INSERT INTO dscnmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
   cursor.execute(sql,val)
   cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['31'])
   cursor.execute("update dgmreports set r_count = r_count - 1 where r_id = %s",['30'])
     
   dscn_m = models.Dscnmonthly.objects.all()
   dscn_m = dscn_m.values('p_id','date','emp_id','time','status','cleaning_dscn_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check','remarks')
   dscn_m = dscn_m.filter(emp_id=emp_id)  
   dscnm = dscn_m.order_by('-p_id')   
   dscn_m = dscn_m.filter(date=currdate)     
   dscnmlogs = models.Dscnmlogs.objects.all()
   dscnmlogs = dscnmlogs.filter(date=date.today()).order_by('-log_id')    
   supdetails = models.Supervisor.objects.all()
   supdetails = supdetails.values('name','contact','email').filter(dept='C')
   f = 1
   return render(request,'engineer/dscn/dscnmonrep.html',{'dscn_m':dscn_m,'id':emp_id,'f':f,'supdetails':supdetails,'dscnmlogs':dscnmlogs,'dscnm':dscnm}) 
             
def repsubdmderrors(request,p_id,id):
 if request.session.has_key('uid'): 
   uid=request.session['uid'] 
   if int(uid) == int(id) :
    cursor = connection.cursor() 
    dscnm = models.Dscnmonthly.objects.all()
    dscnm = dscnm.values('p_id','date','time','status','cleaning_dscn_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check')
    dscnm = dscnm.filter(p_id=p_id)
    return render(request,'engineer/dscn/dscnmfinalrep.html',{'dscnm':dscnm,'p_id':p_id,'id':id}) 
   else :
    return routebackdatisd(request, uid)  
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
    sql = "INSERT INTO dscnmlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
    cursor.execute(sql,val)
    cursor.execute("update dscnmonthly set status = %s where p_id = %s",["COMPLETED WITH ERRORS",p_id])
    cursor.execute("update dscnmonthly set unit_incharge_approval = %s where p_id = %s",[None,p_id])
    cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['32'])
    cursor.execute("update dgmreports set r_count = r_count - 1 where r_id = %s",['30'])
  
    if request.session.has_key('uid'):
        cursor = connection.cursor() 
        currdate = date.today()
        dscn_m = models.Dscnmonthly.objects.all()
        dscn_m = dscn_m.values('p_id','date','time','status','cleaning_dscn_associated_eqpt','battery_backup_time_of_ups1nups2','ups_battery_voltage_on_load','antenna_n_cable_check','earth_resistance','eorn_voltage','eqpt_status_after_check','remarks')
        dscn_m = dscn_m.filter(emp_id=id)  
        dscnm = dscn_m.order_by('-p_id')   
        dscn_m = dscn_m.filter(date=currdate)     
        dscnmlogs = models.Dscnmlogs.objects.all()
        dscnmlogs = dscnmlogs.filter(date=date.today()).order_by('-log_id')    
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='C')
        return render(request,'engineer/dscn/dscnmonrep.html',{'supdetails':supdetails,'dscn_m':dscn_m,'id':id,'f':f,'dscnm':dscnm,'dscnmlogs':dscnmlogs}) 
    else : 
        return render(request,'login/login.html')

def homedm(request, id, p_id) :
 if request.session.has_key('uid'):
   uid=request.session['uid'] 
   if int(uid) == int(id):
     cursor = connection.cursor() 
     currdate = date.today()
     dscn_m = models.Dscnmonthly.objects.all().filter(emp_id=id)
     dscnm = dscn_m.order_by('-p_id')
     dscn_m = dscn_m.filter(p_id=p_id)     
     status = dscn_m.values('status')[0]['status']
     f=0 
     if status == "COMPLETED WITH ERRORS" or status == "PENDING" :
         f = 1 
     if dscn_m :
        dscnmlogs = models.Dscnmlogs.objects.all().filter(p_id=p_id).order_by('-log_id')
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='C')
        return render(request,'engineer/dscn/dscnmonthly.html',{'supdetails':supdetails,'dscn_m':dscn_m,'id':id,'dscnm':dscnm,'dscnmlogs':dscnmlogs,'f':f}) 
     else :
        messages.add_message(request,30, 'You cannot make changes to pending report!')
        return routebackdatisd(request, id)
   else :
       return routebackdatisd(request, uid)
 else : 
   return render(request,'login/login.html')


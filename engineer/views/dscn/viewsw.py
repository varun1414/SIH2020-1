from django.shortcuts import render
from django.db import connection
from datetime import date,datetime
# Create your views here.
from login import models as models
from django.contrib import messages

def dscnweeklylogs(request, id) :
     if request.session.has_key('uid'):
          dscn_w = models.Dscnweekly.objects.all()
          dscn_w =  dscn_w.values('dscnweekly_id','date','time','air_conditioning_check','cleaning_dscn_associated_eqpt','ups1_ups2_battery_backup','ups_battery_voltage_on_load','antenna_n_cable_check','remarks','unit_incharge_approval')
          dscn_w =  dscn_w.filter(emp_id=id)
          f=1
          return render(request,'engineer/dscn/dscnweeklyrep.html',{'dscn_w':dscn_w ,'id':id,'f':f}) 
     else : 
          return render(request,'login/login.html')

def dscnw(request, id) :
     if request.session.has_key('uid'):
          dscn_w = models.Dscnweekly.objects.all()
          dscn_w =  dscn_w.values('dscnweekly_id','date','time','air_conditioning_check','cleaning_dscn_associated_eqpt','ups1_ups2_battery_backup','ups_battery_voltage_on_load','antenna_n_cable_check','remarks','unit_incharge_approval')
          dscn_w =  dscn_w.filter(emp_id=id)
          f=0
          return render(request,'engineer/dscn/dscnweeklyrep.html',{'dscn_w':dscn_w ,'id':id,'f':f}) 
     else : 
          return render(request,'login/login.html')

def dscnwrep(request, id) :
     return render(request,'engineer/dscn/dscnwrepsub.html',{'id':id}) 
    
def editdscnweekly(request, dscnweekly_id) :
     cursor = connection.cursor() 
     dscnw = models.Dscnweekly.objects.all()
     dscnw =  dscnw.values('dscnweekly_id','date','emp_id','time','air_conditioning_check','cleaning_dscn_associated_eqpt','ups1_ups2_battery_backup','ups_battery_voltage_on_load','antenna_n_cable_check','remarks','unit_incharge_approval')
     dscnw = dsccnw.filter(dscnweekly_id=dscnweekly_id)
     dscnw_id = dscnw.values('dscnweekly_id').filter(dscnweekly_id=dscnweekly_id)[0]['dscnweekly_id']
     return render(request,'engineer/dscn/editdscnwrepsub.html',{'dscnw':dscnw,'id':dscnw_id})

def dscnwrepsub(request, id) :
    a_id = models.Engineer.objects.all()
    a_id = a_id.values('a_id').filter(emp_id=id)[0]['a_id'] 
    currtime = datetime.now().strftime("%H:%M:%S")
    emp_id = models.Dscnweekly.objects.all()
    emp_id = emp_id.values('emp_id').filter(emp_id=id)[0]['emp_id']
    currdate= date.today()
    cursor = connection.cursor() 
    acc=request.POST['acc']
    cdae=request.POST['cdae']
    uubb=request.POST['uubb']
    ubvl=request.POST['ubvl']
    ancc=request.POST['ancc']
    remarks=request.POST['remarks']
    f=1
    sql = "INSERT INTO dscnweekly (date,time,a_id,emp_id,f_id,Air_conditioning_check,Cleaning_DSCN_associated_eqpt,UPS1_UPS2_battery_backup,UPS_battery_voltage_on_load,Antenna_n_Cable_check,REMARKS,Unit_incharge_approval) VALUES (%s, %s,%s,%s,%s, %s,%s, %s, %s, %s,%s,%s)"
    val = (currdate,currtime,a_id,id,'3',acc,cdae,uubb,ubvl,ancc,remarks,"YES")
    cursor.execute(sql, val)
    dscn_w = models.Dscnweekly.objects.all()
    dscn_w =  dscn_w.values('dscnweekly_id','date','time','air_conditioning_check','cleaning_dscn_associated_eqpt','ups1_ups2_battery_backup','ups_battery_voltage_on_load','antenna_n_cable_check','remarks','unit_incharge_approval')
    return render(request,'engineer/dscn/dscnweeklyrep.html',{'dscn_w':dscn_w ,'id':id,'f':f}) 
     
def updscnweekly(request, id) :
    currdate= date.today()
    currtime = datetime.now().strftime("%H:%M:%S")
    emp_id = models.Dscnweekly.objects.all()
    emp_id = emp_id.values('emp_id').filter(dscnweekly_id=id)[0]['emp_id']
    cursor = connection.cursor() 
    acc=request.POST['acc']
    cdae=request.POST['cdae']
    uubb=request.POST['uubb']
    ubvl=request.POST['ubvl']
    ancc=request.POST['ancc']
    remarks=request.POST['remarks']
    cursor.execute("update dscnweekly set Air_conditioning_check = %s where dscnweekly_id = %s",[acc,id]) 
    cursor.execute("update dscnweekly set Cleaning_DSCN_associated_eqpt = %s where dscnweekly_id = %s",[cdae,id]) 
    cursor.execute("update dscnweekly set UPS1_UPS2_battery_backup = %s where dscnweekly_id = %s",[uubb,id]) 
    cursor.execute("update dscnweekly set UPS_battery_voltage_on_load = %s where dscnweekly_id = %s",[ubvl,id]) 
    cursor.execute("update dscnweekly set Antenna_n_Cable_check = %s where dscnweekly_id = %s",[ancc,id]) 
    cursor.execute("update dscnweekly set REMARKS = %s where dscnweekly_id = %s",[remarks,id]) 
    f=0
    dscn_w = models.Dscnweekly.objects.all()
    dscn_w =  dscn_w.values('dscnweekly_id','date','time','air_conditioning_check','cleaning_dscn_associated_eqpt','ups1_ups2_battery_backup','ups_battery_voltage_on_load','antenna_n_cable_check','remarks','unit_incharge_approval')
    return render(request,'engineer/dscn/dscnweeklyrep.html',{'dscn_w':dscn_w ,'id':emp_id,'f':f}) 
        
    
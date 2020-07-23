from django.shortcuts import render,redirect
from django.db import connection
from datetime import date,datetime,timedelta
from login import models as models
from django.core.mail import send_mail
from django.contrib import messages
from login import views 
from operator import itemgetter
from engineer.views.datis.viewsd import routebackdatisd

# Create your views here.
  
def homedsd(request, id, p_id) :
 if request.session.has_key('uid'):
   uid=request.session['uid'] 
   if int(uid) == int(id):
     cursor = connection.cursor() 
     currdate = date.today()
     dscn_d = models.Dscndaily.objects.all().filter(emp_id=id)
     dscnd = dscn_d.order_by('-p_id')
     dscn_d = dscn_d.filter(p_id=p_id)     
     status = dscn_d.values('status')[0]['status']
     f=0 
     if status == "COMPLETED WITH ERRORS" or status == "PENDING" :
         f = 1 
     if dscn_d :
        dscndlogs = models.Dscndlogs.objects.all().filter(p_id=p_id).order_by('-log_id')
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='C')
        return render(request,'engineer/dscn/dscndailyrep.html',{'supdetails':supdetails,'dscn_d':dscn_d,'id':id,'dscnd':dscnd,'dscndlogs':dscndlogs,'f':f}) 
     else :
        messages.add_message(request,30, 'You cannot make changes to pending report!')
        return routebackdatisd(request, id)
   else :
       return routebackdatisd(request, uid)
 else : 
   return render(request,'login/login.html')


def dscndailyrec(request, id) :
  if request.session.has_key('uid'):
    uid=request.session['uid'] 
    if int(uid) == int(id):
     cursor = connection.cursor() 
     dscn_d = models.Dscndaily.objects.all()
     dscn_d = dscn_d.values('p_id','date','time','status','sat_led','odu_led','io_led','alarm_led','power_led','v35_led','ip_voltage','op_voltage','battery_voltage','coro_function','unit_incharge_approval','approval_date','approval_time')
     dscn_d = dscn_d.filter(emp_id=id).order_by('-p_id')     
     return render(request,'engineer/dscn/dscndrecords.html',{'dscn_d':dscn_d,'id':id})
    else :
     return routebackdatisd(request, uid)
  else :
     return render(request,'login/login.html')
   
    
def dscnd(request, id) :
  if request.session.has_key('uid'):
    uid=request.session['uid'] 
    if int(uid) == int(id):
     currdate= date.today()
     cursor = connection.cursor() 
     dscn_d = models.Dscndaily.objects.all()
     dscn_d = dscn_d.values('p_id','date','time','status','sat_led','odu_led','io_led','alarm_led','power_led','v35_led','ip_voltage','op_voltage','battery_voltage','coro_function','remarks')
     dscn_d = dscn_d.filter(emp_id=id)  
     dscnd = dscn_d.order_by('-p_id')   
     dscn_d = dscn_d.filter(date=currdate)     
     dscndlogs = models.Dscndlogs.objects.all()
     dscndlogs = dscndlogs.filter(date=date.today()).order_by('-log_id')    
     supdetails = models.Supervisor.objects.all()
     supdetails = supdetails.values('name','contact','email').filter(dept='C')
     if dscn_d :
        return render(request,'engineer/dscn/dscndailyrep.html',{'supdetails':supdetails,'dscn_d':dscn_d,'id':id,'dscnd':dscnd,'dscndlogs':dscndlogs})
     else :
        messages.add_message(request,30, 'You cannot make changes to pending report!')
        return routebackdatisd(request, uid)
    else :
     return routebackdatisd(request, uid)
  else :
     return render(request,'login/login.html')
   

def dscndrep(request, id):
 cursor = connection.cursor() 
 if request.session.has_key('uid') : 
   temp = cursor.execute("select date from dscndaily where date = %s",[date.today()])    
   uid=request.session['uid'] 
   if int(uid) == int(id) and temp == 0:
     supdetails = models.Supervisor.objects.all()
     supdetails = supdetails.values('name','contact','email').filter(dept='C')
     dscn_d = models.Dscndaily.objects.all()
     dscn_d = dscn_d.values('p_id','date','time','sat_led','odu_led','io_led','alarm_led','power_led','v35_led','ip_voltage','op_voltage','battery_voltage','coro_function','remarks')
     dscn_d = dscn_d.filter(emp_id=id).order_by('-p_id') 
     return render(request,'engineer/dscn/dscnrepsub.html',{'id':id,'dscn_d':dscn_d,'supdetails':supdetails}) 
   else :
      messages.add_message(request,30, 'Unauthorized Access')
      return routebackdatisd(request, uid)  
 else : 
     return render(request,'login/login.html')
 
def dscndrepsub(request,id):
  if request.session.has_key('uid'):
     uid=request.session['uid'] 
     cursor = connection.cursor()
     currdate= date.today()
     currtime = datetime.now().strftime("%H:%M:%S")
     #a_id = models.Engineer.objects.all()
     #a_id = a_id.values('a_id').filter(emp_id=id)[0]['a_id']
     sled = request.POST['sled']
     oled = request.POST['oled']
     ioled=request.POST['ioled']
     aled = request.POST['aled']
     pwled = request.POST['pwled']
     v35led = request.POST['v35led']
     iv = request.POST['iv']
     ov = request.POST['ov']
     bv=request.POST['bv']
     cof = request.POST['cof']
     status = ""
     sql = "INSERT INTO dscndaily (date,time,status,a_id,emp_id,SAT_LED,ODU_LED,IO_LED,Alarm_LED,Power_LED,V35_LED,IP_Voltage,OP_voltage,Battery_Voltage,CorO_function) VALUES (%s,%s,%s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
     val = (currdate,currtime,status,"1",id,sled,oled,ioled,aled,pwled,v35led,iv,ov,bv,cof)
     cursor.execute(sql, val)
     
     p_id = models.Dscndaily.objects.all()
     p_id = p_id.values('p_id')
     p_id = p_id.order_by('-p_id')
     p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
    
   
     f=2
     if sled != 'STEADY ON' :
         f=3
         remarks = "SAT LED not steady on"
         val = (id,p_id,remarks,sled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     
     if ioled != 'STEADY ON' :
         f=3
         remarks = "I/O LED not steady on"
         val = (id,p_id,remarks,ioled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     
     if oled != 'STEADY ON' :
         f=3
         remarks = "ODU LED not steady on"
         val = (id,p_id,remarks,oled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     if pwled != 'STEADY ON' :
         f=3
         remarks = "Power LED not steady on"
         val = (id,p_id,remarks,pwled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
        
     if v35led != 'RX/TX BLINKING' :
         f=3
         remarks = "Rx/Tx -not Blinking"
         val = (id,p_id,remarks,v35led,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
         
     if aled != 'OFF' :
         f=3
         remarks = "Alarm LED was turned ON"
         val = (id,p_id,remarks,aled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     
     if int(iv) < 220 or int(iv) > 240 :
         f=3
         remarks = "UPS I/P Voltage exceeding normal voltage"
         val = (id,p_id,remarks,iv,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     if int(ov) < 220 or int(ov) > 240 :
         f=3
         remarks = "UPS O/P Voltage exceeding normal voltage"
         val = (id,p_id,remarks,ov,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     if int(bv) < 180 or int(bv) > 250 :
         f=3
         remarks = "UPS Battery Voltage exceeding normal voltage"
         val = (id,p_id,remarks,bv,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
      
     if  cof != 'OK' :
         f=3
         remarks = "C/O Function not OK"
         val = (id,p_id,remarks,cof,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s,%s ,%s, %s , %s,%s)"
         cursor.execute(sql,val)
    
     if f == 2 :
          status = "COMPLETED"
          remarks = "Parameters normal at the first submit!"
          value = "All parameters NORMAL"
          val = (id,p_id,remarks,value,currdate,currtime)
          sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
          cursor.execute(sql,val)
          cursor.execute("update dscndaily set unit_incharge_approval = %s where p_id = %s",[None,p_id])
          cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['5'])
     else :
          status = "PENDING"    
          cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['4'])
    
     cursor.execute("update dscndaily set status = %s where p_id = %s",[status,p_id])
     dscn_d = models.Dscndaily.objects.all()
     dscn_d = dscn_d.values('p_id','date','time','status','sat_led','odu_led','io_led','alarm_led','power_led','v35_led','ip_voltage','op_voltage','battery_voltage','coro_function','remarks')
     dscn_d = dscn_d.filter(emp_id=id)  
     dscnd = dscn_d.order_by('-p_id')   
     dscn_d = dscn_d.filter(date=currdate)     
     dscndlogs = models.Dscndlogs.objects.all()
     dscndlogs = dscndlogs.filter(date=date.today()).order_by('-log_id')    
     supdetails = models.Supervisor.objects.all()
     supdetails = supdetails.values('name','contact','email').filter(dept='C')
     return render(request,'engineer/dscn/dscndailyrep.html',{'supdetails':supdetails,'dscn_d':dscn_d,'id':id,'dscnd':dscnd,'dscndlogs':dscndlogs})
  else :
    return render(request,'login/login.html')  

def editdscndaily(request,p_id):
  if request.session.has_key('uid'):
   uid=request.session['uid'] 
   temp = models.Dscndaily.objects.all().values('status').order_by('-date').filter(date=date.today())[0]['status']
   emp_id = models.Dscndaily.objects.all().values('emp_id').filter(p_id=p_id)[0]['emp_id']
   uid=request.session['uid'] 
   if int(uid) == int(emp_id) and temp == "PENDING" :
     emp_id = models.Dscndaily.objects.all()
     emp_id = emp_id.values('emp_id').filter(p_id=p_id)[0]['emp_id']
     dscnd = models.Dscndaily.objects.all()
     dscnd = dscnd.values('p_id','date','time','status','emp_id','sat_led','odu_led','io_led','alarm_led','power_led','v35_led','ip_voltage','op_voltage','battery_voltage','coro_function','remarks','unit_incharge_approval','remarks')
     dscn_d = dscnd.filter(emp_id=emp_id).order_by('-p_id')     
     dscnd = dscnd.filter(p_id=p_id)
     dscndlogs = models.Dscndlogs.objects.all()
     dscndlogs = dscndlogs.filter(date=date.today()).order_by('-log_id')    
     supdetails = models.Supervisor.objects.all()
     supdetails = supdetails.values('name','contact','email').filter(dept='C')
     return render(request,'engineer/dscn/editdscnrepsub.html',{'supdetails':supdetails,'dscnd':dscnd,'id':p_id,'dscn_d':dscn_d,'dscndlogs':dscndlogs}) 
   else :
     return routebackdatisd(request, uid)  
  else : 
     return render(request,'login/login.html')

def updscndaily(request, id) :
 if request.session.has_key('uid'): 
   uid=request.session['uid'] 
   emp_id = models.Dscndaily.objects.all()
   emp_id = emp_id.values('emp_id').filter(p_id=id)[0]['emp_id']
   if int(uid) == int(emp_id) :
     currtime = datetime.now().strftime("%H:%M:%S")
     currdate= date.today()
     cursor = connection.cursor() 
     p_id = models.Dscndaily.objects.all()
     p_id = p_id.values('p_id')
     p_id = p_id.order_by('-p_id')
     p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
     currtime = datetime.now().strftime("%H:%M:%S")
     emp_id = models.Dscndaily.objects.all()
     emp_id = emp_id.values('emp_id').filter(p_id=id)[0]['emp_id']
     currdate= date.today()
     sled = request.POST['sled']
     oled = request.POST['oled']
     ioled=request.POST['ioled']
     aled = request.POST['aled']
     pwled = request.POST['pwled']
     v35led = request.POST['v35led']
     iv = request.POST['iv']
     ov = request.POST['ov']
     bv=request.POST['bv']
     cof = request.POST['cof']
     rmarks = request.POST['remarks']
     f=2
     if sled != 'STEADY ON' :
         f=3
         cursor.execute("update dscndaily set SAT_LED = %s where p_id = %s",[sled,id])
         remarks = "SAT LED not steady on(update)"
         val = (emp_id,p_id,remarks,sled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s, %s ,%s, %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set SAT_LED = %s where p_id = %s",[sled,id])
              
     if oled != 'STEADY ON' :
         f=3
         cursor.execute("update dscndaily set ODU_LED = %s where p_id = %s",[oled,id])
         remarks = "ODU LED not steady on(update)"
         val = (emp_id,p_id,remarks,oled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set ODU_LED = %s where p_id = %s",[oled,id])
          
     if ioled != 'STEADY ON' :
         f=3
         cursor.execute("update dscndaily set IO_LED = %s where p_id = %s",[ioled,id])
         remarks = "IO LED not steady on(update)"
         val = (emp_id,p_id,remarks,ioled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set IO_LED = %s where p_id = %s",[ioled,id])
    
     if pwled != 'STEADY ON' :
         f=3
         cursor.execute("update dscndaily set Power_LED = %s where p_id = %s",[pwled,id])
         remarks = "Power LED not steady on(update)"
         val = (emp_id,p_id,remarks,pwled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set Power_LED = %s where p_id = %s",[pwled,id])
            
     if v35led != 'RX/TX BLINKING' :
         f=3
         cursor.execute("update dscndaily set V35_LED = %s where p_id = %s",[v35led,id])
         remarks = "Rx/Tx -not Blinking(update)"
         val = (emp_id,p_id,remarks,v35led,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s, %s ,%s, %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set V35_LED = %s where p_id = %s",[v35led,id])
            
     if aled != 'OFF' :
         f=3
         cursor.execute("update dscndaily set Alarm_LED = %s where p_id = %s",[aled,id])
         remarks = "Alarm LED was turned ON(update)"
         val = (emp_id,p_id,remarks,aled,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s, %s ,%s, %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set Alarm_LED = %s where p_id = %s",[aled,id])
          
     if int(iv) < 220 or int(iv) > 240 :
         f=3
         cursor.execute("update dscndaily set IP_Voltage = %s where p_id = %s",[iv,id])
         remarks = "UPS I/P Voltage exceeding normal voltage(update)"
         val = (emp_id,p_id,remarks,iv,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set IP_Voltage = %s where p_id = %s",[iv,id])
        
     if int(ov) < 220 or int(ov) > 240 :
         f=3
         cursor.execute("update dscndaily set OP_voltage = %s where p_id = %s",[ov,id])
         remarks = "UPS O/P Voltage exceeding normal voltage(update)"
         val = (emp_id,p_id,remarks,ov,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set OP_voltage = %s where p_id = %s",[ov,id])
     
     if int(bv) < 180 or int(bv) > 250 :
         f=3
         cursor.execute("update dscndaily set Battery_voltage = %s where p_id = %s",[bv,id])
         remarks = "UPS Battery Voltage exceeding normal voltage(update)"
         val = (emp_id,p_id,remarks,bv,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set Battery_voltage = %s where p_id = %s",[bv,id])
         
     if  cof != 'OK' :
         f=3
         cursor.execute("update dscndaily set CorO_Function = %s where p_id = %s",[cof,id])
         remarks = "C/O Function not OK(update)"
         val = (emp_id,p_id,remarks,cof,currdate,currtime)
         sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
         cursor.execute(sql,val)
     else :
         cursor.execute("update dscndaily set CorO_Function = %s where p_id = %s",[cof,id])
          
     if ioled == 'STEADY ON' and pwled == 'STEADY ON' and oled == 'STEADY ON' and v35led == 'RX/TX BLINKING' and aled == 'OFF' and sled == 'STEADY ON' and cof == 'OK' and (int(bv) > 179 and int(bv) < 251) and (int(ov) > 219 and int(ov) < 241) and (int(iv) > 219 and int(iv) < 241) :
          status = "COMPLETED"
          f=1
          value = "All parameters NORMAL"
          val = (emp_id,p_id,value,rmarks,currdate,currtime)
          sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
          cursor.execute(sql,val)
          cursor.execute("update dscndaily set status = %s where p_id = %s",[status,id])
          cursor.execute("update dscndaily set unit_incharge_approval = %s where p_id = %s",[None,id])
          cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['5'])
          cursor.execute("update dgmreports set r_count = r_count - 1 where r_id = %s",['4'])
  
     else :
          val = (emp_id,p_id,"Procedure Followed",rmarks,currdate,currtime)
          sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
          cursor.execute(sql,val)  
      
     
     dscn_d = models.Dscndaily.objects.all()
     dscn_d = dscn_d.values('p_id','date','time','status','sat_led','odu_led','io_led','alarm_led','power_led','v35_led','ip_voltage','op_voltage','battery_voltage','coro_function','remarks')
     dscnd = dscn_d
     dscnd = dscnd.filter(emp_id=emp_id).order_by('-p_id')
     dscn_d = dscn_d.filter(date=currdate)
     dscndlogs = models.Dscndlogs.objects.all()
     dscndlogs = dscndlogs.filter(date=date.today()).order_by('-log_id')    
     supdetails = models.Supervisor.objects.all()
     supdetails = supdetails.values('name','contact','email').filter(dept='C')
    
     return render(request,'engineer/dscn/dscndailyrep.html',{'dscn_d':dscn_d,'id':emp_id,'dscndlogs':dscndlogs,'supdetails':supdetails,'dscnd':dscnd})
      
def repsubdsderrors(request,p_id,id) :
 if request.session.has_key('uid'): 
   uid=request.session['uid'] 
   if int(uid) == int(id) :
    cursor = connection.cursor() 
    dscnd = models.Dscndaily.objects.all()
    dscnd = dscnd.values('p_id','date','time','status','sat_led','odu_led','io_led','alarm_led','power_led','v35_led','ip_voltage','op_voltage','battery_voltage','coro_function')
    dscnd = dscnd.filter(p_id=p_id)
    return render(request,'engineer/dscn/dscnfinalrep.html',{'dscnd':dscnd,'p_id':p_id,'id':id}) 
   else :
    return routebackdatisd(request, uid)  
 else : 
    return render(request,'login/login.html')

def finalddrepsub(request,p_id,id) :
    f=1
    cursor = connection.cursor()
    currdate= date.today()
    currtime = datetime.now().strftime("%H:%M:%S")
    value = request.POST['remarks']
    remarks = "Final submit with errors"
    val = (id,p_id,remarks,value,currdate,currtime)
    sql = "INSERT INTO dscndlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
    cursor.execute(sql,val)
    cursor.execute("update dscndaily set status = %s where p_id = %s",["COMPLETED WITH ERRORS",p_id])
    cursor.execute("update dscndaily set unit_incharge_approval = %s where p_id = %s",[None,p_id])
    cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['6'])
    cursor.execute("update dgmreports set r_count = r_count - 1 where r_id = %s",['4'])
  
    if request.session.has_key('uid'):
        cursor = connection.cursor() 
        currdate = date.today()
        dscn_d = models.Dscndaily.objects.all()
        dscn_d = dscn_d.values('p_id','date','time','status','sat_led','odu_led','io_led','alarm_led','power_led','v35_led','ip_voltage','op_voltage','battery_voltage','coro_function','remarks')
        dscn_d = dscn_d.filter(emp_id=id)
        dscnd = dscn_d.order_by('-p_id')
        dscn_d = dscn_d.filter(date=currdate)     
        dscndlogs = models.Dscndlogs.objects.all()
        dscndlogs = dscndlogs.filter(date=date.today()).order_by('-log_id')    
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='C')
        return render(request,'engineer/dscn/dscndailyrep.html',{'supdetails':supdetails,'dscn_d':dscn_d,'id':id,'f':f,'dscnd':dscnd,'dscndlogs':dscndlogs}) 
    else : 
        return render(request,'login/login.html')
    
        
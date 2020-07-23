from django.shortcuts import render
from django.db import connection
from datetime import date,datetime,timedelta
from engineer.views.cdvor.viewsd import routebackcdvord
from login import models as models
from django.contrib import messages


def cdvormrep(request, id) :
    cursor = connection.cursor() 
    if request.session.has_key('uid'):
        temp = cursor.execute("select date from cdvormonthly where date = %s",[date.today()])    
        uid=request.session['uid'] 
        if int(uid) == int(id) and temp == 0:
            cdvor_m = models.Cdvormonthly.objects.all()
            cdvor_m = cdvor_m.values('p_id','date','time','measured_bearing_1','bearing_deviation_1','measured_bearing_2','bearing_deviation_2','measured_bearing_3','bearing_deviation_3','measured_bearing_4','bearing_deviation_4','measured_bearing_5','bearing_deviation_5','error_spread','remarks')
            cdvor_m = cdvor_m.filter(emp_id=id).order_by('-p_id')
            supdetails = models.Supervisor.objects.all()
            supdetails = supdetails.values('name','contact','email').filter(dept='N')
            return render(request,'engineer/cdvor/cdvormrepsub.html',{'cdvor_m':cdvor_m,'id':id,'supdetails':supdetails}) 
        else: 
            return routebackcdvord(request, uid)
    else: 
        return render(request,'login/login.html')

def cdvormrepsubm(request, id): 
    if request.session.has_key('uid'):
        a_id = models.Engineer.objects.all()
        a_id = a_id.values('a_id').filter(emp_id=id)[0]['a_id'] 
        currtime = datetime.now().strftime("%H:%M:%S")
        emp_id = models.Engineer.objects.all()
        if request.session['uid'] == id:
            emp_id = emp_id.values('emp_id').filter(emp_id=id)[0]['emp_id']
        currdate= date.today()
        cursor = connection.cursor() 
        
        measured_bearing = []
        bearing_deviation = []

        measured_bearing.insert(0,float(request.POST['Measured bearing 1'])) 
        bearing_deviation.insert(0,abs(measured_bearing[0] - 0)) 
        measured_bearing.insert(1,float(request.POST['Measured bearing 2'])) 
        bearing_deviation.insert(1,abs(measured_bearing[1] - 7.5)) 
        measured_bearing.insert(2,float(request.POST['Measured bearing 3'])) 
        bearing_deviation.insert(2,abs(measured_bearing[2] - 15)) 
        measured_bearing.insert(3,float(request.POST['Measured bearing 4'])) 
        bearing_deviation.insert(3,abs(measured_bearing[3] - 22.5))
        measured_bearing.insert(4,float(request.POST['Measured bearing 5'])) 
        bearing_deviation.insert(4,abs(measured_bearing[4] - 30)) 
 
        error_spread = sum(bearing_deviation) / 5

        sql = "INSERT INTO cdvormonthly (date,time,a_id,f_id,emp_id,status,measured_bearing_1,bearing_deviation_1, measured_bearing_2, bearing_deviation_2, measured_bearing_3, bearing_deviation_3, measured_bearing_4, bearing_deviation_4, measured_bearing_5, bearing_deviation_5, error_spread ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (currdate,currtime,a_id,'1',id,"",measured_bearing[0], bearing_deviation[0], measured_bearing[1], bearing_deviation[1], measured_bearing[2], bearing_deviation[2], measured_bearing[3], bearing_deviation[3], measured_bearing[4], bearing_deviation[4], error_spread)
        cursor.execute(sql, val)
        p_id = models.Cdvormonthly.objects.all()
        p_id = p_id.values('p_id')
        p_id = p_id.order_by('-p_id')
        p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
        print(p_id)
        f=2         # f=2, everything is okay
                    # f=3, not all values are in range
        for i in range(0,len(bearing_deviation)):
            if bearing_deviation[i] >= 1:
                f = 3
                print('index: ',i)
                remarks = "Measured bearing " + str(i+1) + " is deviating for more than 1"
                val = (id, p_id, remarks,measured_bearing[i], currdate, currtime) 
                sql  = "INSERT INTO cdvormlogs (emp_id,p_id, remarks, value, date, time) values (%s ,%s,%s,%s , %s,%s)"
                cursor.execute(sql, val)           

        if error_spread >= 0.5:
            f=3
            remarks = "Error spread found is greator than 0.5"
            val = (id,p_id,remarks,error_spread,currdate,currtime)
            sql = "INSERT INTO cdvormlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
            cursor.execute(sql,val)
        
        if f == 2:
            statusm = "COMPLETED"
            remarks = "Parameters normal at the first submit!"
            value = "All parameters NORMAL"
            val = (id,p_id,remarks,value,currdate,currtime)
            sql = "INSERT INTO cdvormlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
            cursor.execute(sql,val)
            cursor.execute("update cdvormonthly set unit_incharge_approval = %s where p_id = %s",[None,p_id])
            cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['25'])
  
        else:
            statusm = "PENDING"
            cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['24'])
      
        print(statusm)    
        cursor.execute("update cdvormonthly set status = %s where p_id = %s",[statusm,p_id])
        cdvor_m = models.Cdvormonthly.objects.all()
        cdvor_m = cdvor_m.values('p_id','date','time','status','measured_bearing_1','bearing_deviation_1','measured_bearing_2','bearing_deviation_2','measured_bearing_3','bearing_deviation_3','measured_bearing_3','bearing_deviation_3','measured_bearing_4','bearing_deviation_4','measured_bearing_5','bearing_deviation_5','error_spread','remarks')
        cdvorm = cdvor_m.filter(emp_id=id).order_by('-p_id')
        cdvor_m = cdvor_m.filter(date=currdate)
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='N')
        cdvormlogs = models.Cdvormlogs.objects.all()
        cdvormlogs = cdvormlogs.filter(date=date.today()).order_by('-log_id')    
        
        return render(request,'engineer/cdvor/cdvormonthlyrep.html',{'cdvormlogs':cdvormlogs,'cdvor_m':cdvor_m,'id':id,'cdvorm':cdvorm,'supdetails':supdetails})      
    else : 
        return render(request,'login/login.html')

def editcdvormonthly(request, p_id) :
    if request.session.has_key('uid'):
        temp = models.Cdvormonthly.objects.all().values('status').order_by('-date').filter(date=date.today())[0]['status']
        uid=request.session['uid'] 
        if temp == "PENDING" and 'uid' in request.session:
            cursor = connection.cursor() 
            emp_id = int(request.session['uid'])
            cdvorm = models.Cdvormonthly.objects.all()
            cdvorm = cdvorm.values('p_id','date','time','status','emp_id','measured_bearing_1','bearing_deviation_1','measured_bearing_2','bearing_deviation_2','measured_bearing_3','bearing_deviation_3','measured_bearing_4','bearing_deviation_4','measured_bearing_5','bearing_deviation_5','error_spread','remarks')
            cdvor_m = cdvorm.filter(emp_id=emp_id).order_by('-p_id')
            cdvorm = cdvorm.filter(p_id=p_id)
            cdvor_id = cdvorm.values('p_id').filter(p_id=p_id)[0]['p_id']
            supdetails = models.Supervisor.objects.all()
            supdetails = supdetails.values('name','contact','email').filter(dept='N')
            cdvormlogs = models.Cdvormlogs.objects.all()
            cdvormlogs = cdvormlogs.filter(date=date.today()).order_by('-log_id')    
            return render(request,'engineer/cdvor/editcdvormrepsub.html',{'cdvormlogs':cdvormlogs,'cdvorm':cdvorm,'id':cdvor_id,'cdvor_m':cdvor_m,'supdetails':supdetails})
        else: 
            return routebackcdvord(request, uid)
    else: 
        return render(request,'login/login.html')

def upcdvormonthly(request, id) :
    if request.session.has_key('uid'):
        p_id = models.Cdvormonthly.objects.all()
        p_id = p_id.values('p_id')
        p_id = p_id.order_by('-p_id')
        p_id = p_id.values('p_id').filter(a_id=1)[0]['p_id']
        currdate= date.today()
        currtime = datetime.now().strftime("%H:%M:%S")
        cursor = connection.cursor() 
        emp_id = int(request.session['uid'])
        remarks=request.POST['remarks']
        
        measured_bearing = []
        bearing_deviation = []

        measured_bearing.insert(0,float(request.POST['Measured bearing 1'])) 
        bearing_deviation.insert(0,abs(measured_bearing[0] - 0)) 
        measured_bearing.insert(1,float(request.POST['Measured bearing 2'])) 
        bearing_deviation.insert(1,abs(measured_bearing[1] - 7.5)) 
        measured_bearing.insert(2,float(request.POST['Measured bearing 3'])) 
        bearing_deviation.insert(2,abs(measured_bearing[2] - 15)) 
        measured_bearing.insert(3,float(request.POST['Measured bearing 4'])) 
        bearing_deviation.insert(3,abs(measured_bearing[3] - 22.5))
        measured_bearing.insert(4,float(request.POST['Measured bearing 5'])) 
        bearing_deviation.insert(4,abs(measured_bearing[4] - 30)) 

        error_spread = sum(bearing_deviation) / 5


        f=2   #intially set flag condition for all normal
    
    
        # Failure cases

        for i in range(0,len(bearing_deviation)):
            if bearing_deviation[i] >= 1:
                f = 3   # if not normal
                remarks1 = "Measured bearing " + str(i+1) + " is deviating for more than 1(update)"
                val = (emp_id, p_id, remarks1,measured_bearing[i], currdate, currtime) 
                sql  = "INSERT INTO cdvormlogs (emp_id,p_id, remarks, value, date, time) values (%s ,%s,%s,%s , %s,%s)"
                cursor.execute(sql, val)           
            cursor.execute("update cdvormonthly set measured_bearing_"+ str(i+1) +" = %s where p_id = %s",[measured_bearing[i],id])
            cursor.execute("update cdvormonthly set bearing_deviation_"+ str(i+1) +" = %s where p_id = %s",[bearing_deviation[i],id])
                

        if error_spread >= 0.5:
            f=3
            cursor.execute("update cdvormonthly set error_spread = %s where p_id = %s",[error_spread, id])
            remarks1 = "Error spread found is >= 0.5(update)"
            val = (emp_id,p_id,remarks1,error_spread,currdate,currtime)
            sql = "INSERT INTO cdvormlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
            cursor.execute(sql,val)
        else:
            cursor.execute("update cdvormonthly set error_spread = %s where p_id = %s",[error_spread, id])

        if error_spread < 0.5 and 0 not in (list(map(lambda x: x < 1,bearing_deviation))):
            cursor.execute("update cdvormonthly set status = %s where p_id = %s",["COMPLETED",id])
            val = (emp_id,p_id,"All parameters NORMAL",remarks,currdate,currtime)
            sql = "INSERT INTO cdvormlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
            cursor.execute(sql,val)
            cursor.execute("update cdvormonthly set unit_incharge_approval = %s where p_id = %s",[None,id])
            cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['25'])
            cursor.execute("update dgmreports set r_count = r_count - 1 where r_id = %s",['24'])
  
        else: 
            val = (emp_id,p_id,"Procedure Followed",remarks,currdate,currtime)
            sql = "INSERT INTO cdvormlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s,%s , %s,%s)"
            cursor.execute(sql,val)
        
        cdvor_m = models.Cdvormonthly.objects.all()
        cdvor_m = cdvor_m.values('p_id','date','time','status','measured_bearing_1','bearing_deviation_1','measured_bearing_2','bearing_deviation_2','measured_bearing_3','bearing_deviation_3','measured_bearing_4','bearing_deviation_4','measured_bearing_5','bearing_deviation_5','error_spread','remarks')
        cdvorm = cdvor_m.filter(emp_id=emp_id).order_by('-p_id')
        cdvor_m = cdvor_m.filter(date=currdate)
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='N')
        cdvormlogs = models.Cdvormlogs.objects.all()
        cdvormlogs = cdvormlogs.filter(date=date.today()).order_by('-log_id')    
        return render(request,'engineer/cdvor/cdvormonthlyrep.html',{'cdvormlogs':cdvormlogs,'cdvor_m':cdvor_m,'id':emp_id,'cdvorm':cdvorm,'supdetails':supdetails})      
    else:
        return render(request,'login/login.html')

def repsubmerrors(request,p_id,id):
    if request.session.has_key('uid'):
        uid=request.session['uid'] 
        if int(uid) == int(id):
            cursor = connection.cursor() 
            cdvorm = models.Cdvormonthly.objects.all()
            cdvorm = cdvorm.values('p_id','date','time','status','emp_id','measured_bearing_1','bearing_deviation_1','measured_bearing_2','bearing_deviation_2','measured_bearing_3','bearing_deviation_3','measured_bearing_4','bearing_deviation_4','measured_bearing_5','bearing_deviation_5','error_spread','remarks')
            cdvorm = cdvorm.filter(p_id=p_id)
            return render(request,'engineer/cdvor/cdvormfinalrep.html',{'cdvorm':cdvorm,'p_id':p_id,'id':id})
        else : 
            return routebackcdvord(request, uid)
    else: 
        return render(request,'login/login.html')

def finalmrepsub(request,p_id,id):
    f=1
    print(f)
    cursor = connection.cursor()
    currdate= date.today()
    currtime = datetime.now().strftime("%H:%M:%S")
    value = request.POST['remarks']
    remarks = "Final submit with errors"
    val = (id,p_id,remarks,value,currdate,currtime)
    sql = "INSERT INTO cdvormlogs (emp_id,p_id,remarks,value,date,time) values (%s ,%s,%s, %s , %s,%s)"
    cursor.execute(sql,val)
    cursor.execute("update cdvormonthly set status = %s where p_id = %s",["COMPLETED WITH ERRORS",p_id])
    cursor.execute("update cdvormonthly set unit_incharge_approval = %s where p_id = %s",[None,p_id])
    cursor.execute("update dgmreports set r_count = r_count + 1 where r_id = %s",['26'])
    cursor.execute("update dgmreports set r_count = r_count - 1 where r_id = %s",['24'])
  
   
    #code for notification to supervisor will come over here 
    if request.session.has_key('uid'):
        cursor = connection.cursor() 
        currdate = date.today()
        cdvor_m = models.Cdvormonthly.objects.all()
        cdvor_m = cdvor_m.values('p_id','date','time','status','measured_bearing_1','bearing_deviation_1','measured_bearing_2','bearing_deviation_2','measured_bearing_3','bearing_deviation_3','measured_bearing_4','bearing_deviation_4','measured_bearing_5','bearing_deviation_5','error_spread','remarks')
        cdvorm = cdvor_m.filter(emp_id=id).order_by('-p_id')
        cdvor_m = cdvor_m.filter(date=currdate)
        supdetails = models.Supervisor.objects.all()
        supdetails = supdetails.values('name','contact','email').filter(dept='N')
        cdvormlogs = models.Cdvormlogs.objects.all()
        cdvormlogs = cdvormlogs.filter(date=date.today()).order_by('-log_id')    
    
        return render(request,'engineer/cdvor/cdvormonthlyrep.html',{'cdvormlogs':cdvormlogs,'cdvor_m':cdvor_m,'id':id,'f':f,'cdvorm':cdvorm,'supdetails':supdetails})      
    else : 
        return render(request,'login/login.html')

def cdvorm(request, id) :
    if request.session.has_key('uid'):
        uid=request.session['uid'] 
        if int(uid) == int(id):
            cdvor_m = models.Cdvormonthly.objects.all()
            cdvor_m = cdvor_m.values('p_id','date','time','status','measured_bearing_1','bearing_deviation_1','measured_bearing_2','bearing_deviation_2','measured_bearing_3','bearing_deviation_3','measured_bearing_4','bearing_deviation_4','measured_bearing_5','bearing_deviation_5','error_spread','remarks')
            cdvor_m = cdvor_m.filter(emp_id=id)
            cdvorm = cdvor_m.order_by('-p_id')
            cdvor_m = cdvor_m.filter(date=date.today())
            supdetails = models.Supervisor.objects.all()
            supdetails = supdetails.values('name','contact','email').filter(dept='N')
            cdvormlogs = models.Cdvormlogs.objects.all()
            cdvormlogs = cdvormlogs.filter(date=date.today()).order_by('-log_id')    
            if cdvor_m :
                return render(request,'engineer/cdvor/cdvormonthlyrep.html',{'cdvormlogs':cdvormlogs,'supdetails':supdetails,'cdvor_m':cdvor_m,'id':id,'cdvorm':cdvorm}) 
            else:
                messages.add_message(request,30, 'You cannot make changes to pending report!')
                return routebackcdvord(request, id)
        else: 
            return routebackcdvord(request, uid)
    else:
        return render(request,'login/login.html')

def cdvormonthlyrec(request, id):
    if request.session.has_key('uid'):
        uid=request.session['uid'] 
        if int(uid) == int(id):
            cursor = connection.cursor() 
            cdvor_m = models.Cdvormonthly.objects.all()
            cdvor_m = cdvor_m.values('p_id','date','time','status','measured_bearing_1','bearing_deviation_1','measured_bearing_2','bearing_deviation_2','measured_bearing_3','bearing_deviation_3','measured_bearing_4','bearing_deviation_4','measured_bearing_5','bearing_deviation_5','error_spread','unit_incharge_approval','approval_date','approval_time')
            cdvor_m = cdvor_m.filter(emp_id=id).order_by('-p_id')
            return render(request,'engineer/cdvor/cdvormrecords.html',{'cdvor_m':cdvor_m,'id':id}) 
        else: 
            return routebackcdvord(request, id)
    else: 
        return render(request,'login/login.html')

def homem(request, id, p_id) :
    if request.session.has_key('uid'):
        uid=request.session['uid'] 
        if int(uid) == int(id):
            cdvor_m = models.Cdvormonthly.objects.all().filter(emp_id=id)
            cdvorm = cdvor_m.order_by('-p_id')
            cdvor_m = cdvor_m.filter(p_id=p_id)
            statusm = cdvor_m.values('status')[0]['status']
            f = 0 
            if statusm == "COMPLETED WITH ERRORS" or statusm == "PENDING":
                f = 1
            supdetails = models.Supervisor.objects.all().values('name','contact','email').filter(dept='N')
            cdvormlogs = models.Cdvormlogs.objects.all().filter(p_id=p_id).order_by('-log_id') 
            if cdvor_m :
                return render(request,'engineer/cdvor/cdvormonthlyrep.html',{'cdvormlogs':cdvormlogs,'supdetails':supdetails,'cdvor_m':cdvor_m,'id':id,'cdvorm':cdvorm,'f':f}) 
            else:
                return routebackcdvord(request, id)
        else: 
            return routebackcdvord(request, uid)
    else: 
        return render(request,'login/login.html')

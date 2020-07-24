from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from login.models import Engineer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from datetime import date,datetime,timedelta
from django.db import connection
from cryptography.fernet import Fernet as frt
from supervisor.views import main
from login.sup.homeviewSup import run_sup as run_sup
from login.eng.homeviewEng import dhomeview as dhomeview
from login.eng.homeviewEng import dhomeviewn as dhomeviewn
from login.eng.homeviewEng import dhomeviews as dhomeviews
from login.eng.logEng import logEng as logEng
from login.eng.logEng import logEngN as logEngN
from login.eng.logEng import logEngS as logEngS
from head.views import dispMap as dispMap
from dgm.views import homev as homev
from django.http import HttpResponse
from . import models
from django.db import connection
from head.views import headv as headv
# Create your views here.
def login(request):
    if request.session.has_key('uid') and request.session.get('type')=='e':
         id = int(request.session['uid'])
         dept = models.Engineer.objects.all().values('dept').filter(emp_id = id)[0]['dept']
         if dept == 'C':
            return logEng(request,request.session.get('uid'))
         elif dept == 'N':
            return logEngN(request, request.session.get('uid'))
         elif dept == 'S':
            return logEngS(request, request.session.get('uid'))
   

    if request.session.has_key('uid') and request.session.get('type')=='s':
        return run_sup(request,request.session.get('uid'))
    
    if request.session.has_key('uid') and request.session.get('type')=='d':
        return homev(request,request.session.get('uid'))
    else:
         return render(request,'login/login.html')

def validate(request):
    uid=request.POST.get('id',False)
    passw=request.POST.get('passw',False)
    flag=1
    temp=uid
    id = uid
    b=temp[0]+""+temp[1]
    if b=='41' :
        x=models.Engineer.objects.all()
        for i in x:  
            if (uid == str(i.emp_id)) & (check_password(passw,i.password)) :
                flag=0
                dept = models.Engineer.objects.all().values('dept').filter(emp_id=uid)[0]['dept']
                if dept == "C" :
                    request.session['type']='e'
                    return dhomeview(request,id)
                elif dept == "N" :  
                    request.session['type']='e'
                    return dhomeviewn(request,id)
                
                elif dept =="S" :
                    request.session['type']='e'
                    return dhomeviews(request,id)
    elif b=='21' :
        request.session['key']=frt.generate_key().decode('utf-8')
        x=models.Dgm.objects.all()
        for i in x:
            if (uid == str(i.dgm_id)) & (check_password(passw,i.password)) :
                flag=0
                request.session['type']='d'
                return homev(request,id)
    
               # y=models.Airport.objects.filter(a_id=i.a_id).values()
               # print(y[0])
               # return render(request,'./dgm/dgm.html',{'name':y[0]})
    elif b=='11' :
        request.session['key']=frt.generate_key().decode('utf-8')
        # x=models.Dgm.objects.all()
        x=models.Head.objects.all()
        for i in x:
            if (uid == str(i.head_id)) & (check_password(passw,i.password)) :
                flag=0
                request.session['type']='h'
                airInfo=models.Airport.objects.all().values()
                return dispMap(request,airInfo)
    elif b=='31' :
        request.session['key']=frt.generate_key().decode('utf-8')
        x=models.Supervisor.objects.all()
        for i in x:
            print(check_password(passw,i.password))
            if (uid == str(i.supervisor_id)) & (check_password(passw,i.password)) :
                flag=0
                supInfo=models.Supervisor.objects.filter(supervisor_id=uid).values()
                request.session['dept']=supInfo[0]['dept']
                return run_sup(request,uid)
    if flag==1 :
        print("wrong")
        return render(request,'login/login.html',{'flag':flag})

            




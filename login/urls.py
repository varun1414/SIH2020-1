from django.contrib import admin
from django.urls import path,include
from . import views
from engineer import views as eviews
from django.contrib import admin
from django.urls import path,include
from . import views
from engineer.views.datis import viewsd as datviewsd
from engineer.views.datis import viewsw as datviewsw
from engineer.views.dscn import viewsd as dscnviewsd
from engineer.views.dscn import viewsm as dscnviewsm
from engineer.views.dscn import viewsw as dscnviewsw
from engineer.views.cdvor import viewsd as cdvorviewsd
from engineer.views.cdvor import viewsw as cdvorviewsw
from engineer.views.cdvor import viewsm as cdvorviewsm
from engineer.views.scctv import viewsd as scctvviewsd
from engineer.views.scctv import viewsw as scctvviewsw
from engineer.views.scctv import viewsm as scctvviewsm
from supervisor.views.main import verify as verify
from dgm import views as viewsdgm
from django.urls import include, re_path
#from django.views.generic import TemplateView

urlpatterns = [
    path('',views.login),
    path('validate/',views.validate),
    path('schoice/',include('supervisor.urls')),
    path('dgm/',include('dgm.urls')),
    path('head/',include('head.urls')),
    path('',views.login),
    path('validate/',views.validate),
    path('dhomeview/',views.dhomeview),
    path('dhomeviews/<int:id>',views.dhomeview),
    re_path(r'^calendar/',viewsdgm.calendar, name='calendar'),
    re_path(r'^calendarn/',viewsdgm.calendarn, name='calendarn'),
    re_path(r'^calendars/',viewsdgm.calendars, name='calendars'),
    
    

    #vhf 
    #daily
    #path('vhfdaily/<int:id>',vhfviewsd.vhfd),
    #path('vhfdailyrep/<int:id>',vhfviewsd.vhfdrep),
    #path('vhfrepsub/<int:id>',vhfviewsd.vhfdrepsub), 
    #path('vhfdailylogs/<int:id>',vhfviewsd.vhfdlogs), 
    #path('editvhfd/<int:vhfdaily_id>',vhfviewsd.editvhfdaily), 
    #path('upvhfrepsub/<int:id>',vhfviewsd.upvhfdaily),
    #path('routebackvd/<int:id>/',vhfviewsd.routebackvhfd),    
    #path('vhfdailyrec/<int:id>/',vhfviewsd.vhfdailyrec),    
    
    #monthly
    #path('vhfmonthly/<int:id>',vhfviewsm.vhfm),
    #path('vhfmonthlyrep/<int:id>',vhfviewsm.vhfmrep),
    #path('vhfmrepsub/<int:id>',vhfviewsm.vhfmrepsub),
    #path('vhfmlogs/<int:id>',vhfviewsm.vhfmlogs),
    #path('editvhfm/<int:vhfmonthly_id>',vhfviewsm.editvhfmonthly),
    #path('upvhfmrepsub/<int:id>',vhfviewsm.upvhfmonthly),
    
    #yearly
    #path('vhfyearly/<int:id>',vhfviewsy.vhfy),
    #path('vhfyearlyrep/<int:id>',vhfviewsy.vhfyrep),
    #path('vhfyrepsub/<int:id>',vhfviewsy.vhfyrepsub),
    #path('vhfylogs/<int:id>',vhfviewsy.vhfylogs),
    #path('editvhfy/<int:vhfyearly_id>',vhfviewsy.editvhfyearly),
    #path('upvhfyrepsub/<int:id>',vhfviewsy.upvhfyearly),
  
    #dscn #daily
    path('dscndaily/<int:id>',dscnviewsd.dscnd),
    path('dscndailyrep/<int:id>',dscnviewsd.dscndrep),
    path('dscnrepsub/<int:id>',dscnviewsd.dscndrepsub),
    path('editdscnd/<int:p_id>',dscnviewsd.editdscndaily),
    path('updscnrepsub/<int:id>',dscnviewsd.updscndaily),
    path('finalddrepsub/<int:p_id>/<int:id>',dscnviewsd.finalddrepsub),
    path('repsubdsderrors/<int:p_id>/<int:id>',dscnviewsd.repsubdsderrors),
    path('dscndailyrec/<int:id>',dscnviewsd.dscndailyrec),
    path('homedsd/<int:id>/<int:p_id>',dscnviewsd.homedsd),
    
    #weekly
    path('dscnweekly/<int:id>',dscnviewsw.dscnw),
    path('dscnweeklyrep/<int:id>',dscnviewsw.dscnwrep),
    path('dscnwrepsub/<int:id>',dscnviewsw.dscnwrepsub),
    path('editdscnw/<int:dscnweekly_id>',dscnviewsw.editdscnweekly),
    path('updscnwrepsub/<int:id>',dscnviewsw.updscnweekly),
    path('dscnweeklylogs/<int:id>',dscnviewsw.dscnweeklylogs),
    
    #monthly
    path('dscnmonthly/<int:id>',dscnviewsm.dscnm),
    path('dscnmonthlyrep/<int:id>',dscnviewsm.dscnmrep),
    path('dscnmrepsub/<int:id>',dscnviewsm.dscnmrepsub),
    path('editdscnm/<int:p_id>',dscnviewsm.editdscnmonthly),
    path('updscnmrepsub/<int:id>',dscnviewsm.updscnmonthly),
    path('dscnmonthlyrec/<int:id>',dscnviewsm.dscnmonthlyrec),
    path('repsubdmderrors/<int:p_id>/<int:id>',dscnviewsm.repsubdmderrors),
    path('finalmrepsub/<int:p_id>/<int:id>',dscnviewsm.finalmrepsub),
    path('homedm/<int:id>/<int:p_id>',dscnviewsm.homedm),
    
    #datis
   #daily 
    path('datisdaily/<int:id>',datviewsd.datisd),
    path('datisdailyrep/<int:id>',datviewsd.datisdrep),
    path('datisrepsub/<int:id>',datviewsd.datisdrepsubm),
    path('editdatisd/<int:p_id>',datviewsd.editdatisdaily),
    path('updatisrepsub/<int:id>',datviewsd.updatisdaily),
    path('routebackdd/<int:id>/',datviewsd.routebackdatisd),
    path('logout/<int:id>',datviewsd.logoutd),
    path('datisdailyrec/<int:id>',datviewsd.datisdailyrec),
    path('repsuberrors/<int:p_id>/<int:id>',datviewsd.repsuberrors),
    path('finalrepsub/<int:p_id>/<int:id>',datviewsd.finalrepsub),
    path('sent/',datviewsd.sent),
    #added new route
    path('homed/<int:id>/<int:p_id>',datviewsd.homed),
    
    #weekly
    path('datisweekly/<int:id>',datviewsw.datisw),
    path('datisweeklyrep/<int:id>',datviewsw.datiswrep),
    path('datisweeklyrec/<int:id>',datviewsw.datisweeklyrec),
    path('datiswrepsub/<int:id>',datviewsw.datiswrepsubw),
    path('editdatisw/<int:p_id>',datviewsw.editdatisweekly),
    path('updatiswrepsub/<int:id>',datviewsw.updatisweekly),
    path('repsubwerrors/<int:p_id>/<int:id>',datviewsw.repsubwerrors),
    path('finalwrepsub/<int:p_id>/<int:id>',datviewsw.finalwrepsub),
    path('homew/<int:id>/<int:p_id>',datviewsw.homew),
   
   #cdvor
   #daily
    path('cdvordailyrep/<int:id>',cdvorviewsd.cdvordrep),
    path('cdvorrepsub/<int:id>',cdvorviewsd.cdvordrepsubm),
    path('cdvordaily/<int:id>', cdvorviewsd.cdvord),
    path('routebackcd/<int:id>/',cdvorviewsd.routebackcdvord),
    path('cdvordailyrec/<int:id>',cdvorviewsd.cdvordailyrec),
    path('editcdvord/<int:p_id>',cdvorviewsd.editcdvordaily),
    path('upcdvorrepsub/<int:id>',cdvorviewsd.upcdvordaily),
    path('repsubcderrors/<int:p_id>/<int:id>',cdvorviewsd.repsuberrors),
    path('finalcdrepsub/<int:p_id>/<int:id>',cdvorviewsd.finalrepsub),
    path('homecd/<int:id>/<int:p_id>',cdvorviewsd.homecd),
    
    #weekly
    path('cdvorweeklyrep/<int:id>',cdvorviewsw.cdvorwrep),
    path('cdvorwrepsub/<int:id>',cdvorviewsw.cdvorwrepsubw),
    path('editcdvorw/<int:p_id>',cdvorviewsw.editcdvorweekly),
    path('cdvorweekly/<int:id>',cdvorviewsw.cdvorw),
    path('repsubcwerrors/<int:p_id>/<int:id>',cdvorviewsw.repsubwerrors),
    path('upcdvorwrepsub/<int:id>',cdvorviewsw.upcdvorweekly),
    path('cdvorweeklyrec/<int:id>',cdvorviewsw.cdvorweeklyrec),
    path('homecw/<int:id>/<int:p_id>',cdvorviewsw.homew),
    path('finalcwrepsub/<int:p_id>/<int:id>',cdvorviewsw.finalwrepsub),

    #monthly
    path('cdvormonthlyrep/<int:id>',cdvorviewsm.cdvormrep),
    path('cdvormrepsub/<int:id>',cdvorviewsm.cdvormrepsubm),
    path('editcdvorm/<int:p_id>',cdvorviewsm.editcdvormonthly),
    path('upcdvormrepsub/<int:id>',cdvorviewsm.upcdvormonthly),
    path('repsubcmerrors/<int:p_id>/<int:id>',cdvorviewsm.repsubmerrors),
    path('finalcmrepsub/<int:p_id>/<int:id>',cdvorviewsm.finalmrepsub),
    path('cdvormonthly/<int:id>',cdvorviewsm.cdvorm),
    path('cdvormonthlyrec/<int:id>',cdvorviewsm.cdvormonthlyrec),
    path('homecm/<int:id>/<int:p_id>',cdvorviewsm.homem),

    #sccttv
    #daily
    path('scctvdaily/<int:id>',scctvviewsd.scctvd),
    path('scctvdailyrep/<int:id>',scctvviewsd.scctvdrep),
    path('scctvrepsub/<int:id>',scctvviewsd.scctvdrepsubm),
    path('editscctvd/<int:p_id>',scctvviewsd.editscctvdaily),
    path('upscctvrepsub/<int:id>',scctvviewsd.upscctvdaily),
    path('routebackss/<int:id>/',scctvviewsd.routebackscctvd),
    path('logout/<int:id>',scctvviewsd.logoutd),
    path('scctvdailyrec/<int:id>',scctvviewsd.scctvdailyrec),
    path('repsubscctverrors/<int:p_id>/<int:id>',scctvviewsd.repsuberrors),
    path('finalscctvrepsub/<int:p_id>/<int:id>',scctvviewsd.finalrepsub),
    path('sent/',scctvviewsd.sent),
    #added new route
    path('scctvhomed/<int:id>/<int:p_id>',scctvviewsd.homed),
    
    #weekly
    path('scctvweekly/<int:id>',scctvviewsw.scctvw),
    path('scctvweeklyrep/<int:id>',scctvviewsw.scctvwrep),
    path('scctvweeklyrec/<int:id>',scctvviewsw.scctvweeklyrec),
    path('scctvwrepsub/<int:id>',scctvviewsw.scctvwrepsubw),
    path('editscctvw/<int:p_id>',scctvviewsw.editscctvweekly),
    path('upscctvwrepsub/<int:id>',scctvviewsw.upscctvweekly),
    path('repsubscctvwerrors/<int:p_id>/<int:id>',scctvviewsw.repsubwerrors),
    path('finalscctvwrepsub/<int:p_id>/<int:id>',scctvviewsw.finalwrepsub),
    path('scctvhomew/<int:id>/<int:p_id>',scctvviewsw.homew),
    
    #monthly
    path('scctvmonthly/<int:id>',scctvviewsm.scctvm),
    path('scctvmonthlyrep/<int:id>',scctvviewsm.scctvmrep),
    path('finalsmrepsub/<int:p_id>/<int:id>',scctvviewsm.finalmrepsub),
    path('scctvmonthlyrec/<int:id>',scctvviewsm.scctvmrec),
    path('scctvmrepsub/<int:id>',scctvviewsm.scctvmrepsub),
    path('repscctvmsuberrors/<int:p_id>/<int:id>',scctvviewsm.repsuberrors),
    path('editscctvm/<int:p_id>',scctvviewsm.editscctvmonthly),
    path('upscctvmrepsub/<int:id>',scctvviewsm.upscctvmonthly),
    path('scctvhomem/<int:id>/<int:p_id>',scctvviewsm.homem),
    path('verify/<str:names>/<str:id>/',verify,name='verify'),


    
    
   

    # path('engineer/',include('supervisor.urls'))
    # path('employee/',views.employee)
    # path('officer/',views.officer)
    # path('install/', views.install),
    #  path('dummy/', views.dummy),
    #  path('test/', views.test)
]

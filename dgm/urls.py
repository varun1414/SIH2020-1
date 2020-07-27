from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path
from . import views

app_name='dgm'
urlpatterns = [
    # path('communication/',views.communication,name='communication'),
    # path('',views.main.choice,name='choice'),
    path('navigation/', views.navigation,name='navigation'),
    # path('surveillance/', views.navigation,name='sur')
    path('<str:id>/<str:name>', views.details),
    path('formsentn/', views.searchn,name='formsentn'),
    path('formsentc/', views.searchc,name='formsentc'),
    path('formsents/', views.searchs,name='formsents'),
    path('communication/',views.communication),
    path('surv/',views.surv),
    path('nav/',views.nav),
    path('calendar/',views.calendar),
    path('calendarn/',views.calendarn),
    path('calendars/',views.calendars),
    path('cdvordailylist/',views.cdvordaily,name='cdvordailylist'),
    path('cdvormonthlylist/',views.cdvormonthly,name='cdvormonthlylist'),
    path('cdvorweeklylist/',views.cdvorweekly,name='cdvorweeklylist'),
    path('scctvdailylist/',views.scctvdaily,name='scctvdailylist'),
    path('scctvmonthlylist/',views.scctvmonthly,name='scctvmonthlylist'),
    path('scctvweeklylist/',views.scctvweekly,name='scctvweeklylist'),
    path('dscndailylist/',views.dscndaily,name='dscndailylist'),
    path('dscnmonthlylist/',views.dscnmonthly,name='dscnmonthlylist'),
    path('datisdailylist/',views.datisdaily,name='datisdailylist'),
    
    path('datisweeklylist/',views.datisweekly,name='datisweeklylist'),
]
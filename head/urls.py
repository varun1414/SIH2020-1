from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path
from . import views

app_name='head'
urlpatterns = [
    # path('communication/',views.communication,name='communication'),
    # path('',views.main.choice,name='choice'),
    path('headv/', views.headv,name='headv'),
    # path('surveillance/', views.navigation,name='sur')
    # path('<str:id>/<str:name>', views.details,name='details'),
    # path('formsentn/', views.searchn,name='formsentn'),
    # path('formsentc/', views.searchc,name='formsentc'),
    # path('formsents/', views.searchs,name='formsents'),
    # path('communication/',views.communication),
    # path('surv/',views.surv),
    # path('nav/',views.nav),
    # path('calendar/',views.calendar),
    # path('calendarn/',views.calendarn),
    # path('calendars/',views.calendars),

]
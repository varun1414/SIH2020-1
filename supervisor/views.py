from django.shortcuts import render
from login import models as mod
# Create your views here.
def test(request):
    print("here")

    x=mod.Supervisor.objects.all()
    for i in x:
        print(i.emp_id)
    return render(request,'supervisor/supervisor.html')

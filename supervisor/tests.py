from django.test import TestCase

# Create your tests here.
dmemonthly=[entry for entry in models.Dmemonthly.objects.all().values()]
    for i in datisweekly:
        i['token']=main.encode(request,str(i['p_id']))
        if i['s_verify']==None:
           i['flag']=0
        else:
           i['flag']=1
    
    return render(request,'supervisor/list_details.html',{'context':dmemonthly,'name':'Dmemonthly'})
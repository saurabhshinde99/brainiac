from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
import datetime as dt
from .models import *

# Create your views here.
def home(request):
    return render(request,'index.html')

@login_required
def contact(request):
    return HttpResponse('contact')
    
@login_required
def user_details(request):
    return render(request,'user-details.html')

@login_required
@csrf_exempt
def user_details_api(request):
    if request.method == 'GET':
        return HttpResponse("Bad Request")
    try:
        c=Contact.objects.all().order_by('-date')
        data={}
        sr_no=1
        for i in range(len(c)):
            data[i]={"sr_no":sr_no,"date":dt.datetime.strptime(str(c[i].date).split(' ')[0], "%Y-%m-%d").strftime('%d-%m-%Y'), "name":c[i].name,"phone":c[i].phone,"email":c[i].email,"msg":c[i].msg}
            sr_no+=1
        print(data)
    except Exception as e:
        data = {}
        data["status"] = 400
        data["msg"]=str(e)
    data = json.dumps(data, indent=2, default=str)
    return HttpResponse(data)


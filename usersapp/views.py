from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .forms import userform

from .models import User
# Create your views here.

def home(request):
    if request.method == 'POST':
        form=userform(request.POST)
        if form.is_valid:
            form.save()
            data={"user_id":form.cleaned_data['user_id'],
                  "real_name":form.cleaned_data['real_name'],
                  "tz":form.cleaned_data['tz']}
            return JsonResponse({"ok":True,"members":data})
    form=userform()
    return render(request,'home.html',{'form':form})

def user_list(request):
    users=User.objects.all()
    print(type(users))
    data=[{"user_id":user.user_id,"real_name":user.real_name,"tz":user.tz,"activity_periods":[{"start_time":u.start_time,"end_time":u.end_time} for u in user.activity_set.all()]} for user in users ]
    return JsonResponse({"ok":True,"members":data})

def user_detail(request,user_id):
    user=User.objects.get(user_id=user_id)
    data={
        "user_id":user.user_id,
        "real_name":user.real_name,
        "tz":user.tz
    }
    return JsonResponse({"ok":True,"members":data})

def delete_user(request,user_id):
    user=User.objects.get(user_id=user_id)
    user.delete()
    return redirect('userlist')
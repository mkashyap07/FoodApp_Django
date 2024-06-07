from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
# from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('users:success')
    return render(request,'users/register.html',{'form':form})

def success(request):
    return render(request,'users/logout.html')

# def login(request):
#     return render(request,'users/login.html')
# def logout(request):
#     return render(request,'users/logout.html')
def profile(request):
    profile_instances=Profile.objects.all()
    context={
        'profile_instances':profile_instances
    }
    return render(request,'users/profile.html',context)
    
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            return redirect('home')
        else:
            error="username or password is incorrect"
            return render(request,'login.html',{'error':error})

    else:
        return render(request,'login.html')


def register(request):
    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created succesfully')
            return redirect('register')
    else:
        form = UserCreationForm()
        return render(request,'register.html',{'form':form})

def logout(request):
    auth.logout(request)
    return redirect('login')

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
from todo import models
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.

def register(request):
 if request.method=='POST':
    name=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    if not authenticate(request,username=name,password=password):
     
     user_ob=User.objects.create_user(username=name,email=email,password=password)
     user_ob.save()
     return redirect('login')
    else:
      return HttpResponse('user already exist')
 else:
    return render(request,'register.html')
def login_f(request):
  if request.method=='POST':
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect('todo')
    else:
      messages.info(request,'user not found')
      return render(request,'login.html')
  else:
    return render(request,'login.html')
@login_required(login_url='login/')
def todo(request):
  if request.method=='POST':
    task=request.POST['task']
    dat=request.POST['date']
    print(dat)
    dt=datetime.strptime(dat,'%Y-%m-%dT%H:%M')
    print(request.user.username)
    ob=models.todo.objects.create(username=request.user,task=task,date=dt)
    ob=models.todo.objects.filter(username=request.user).order_by('timestamp').reverse

    return redirect('todo')

    
  else:
    ob=models.todo.objects.filter(username=request.user).order_by('timestamp').reverse
    print(models.todo.timestamp)
    return render(request,'todo.html',{'tasks':ob})
@login_required(login_url='login/')
def edit(request,id):
   
   if request.method=='POST':
    task=request.POST['task']
    ob=models.todo.objects.get(id=id)
    ob.task=task
    ob.save()
    ob=models.todo.objects.filter(username=request.user).order_by('timestamp').reverse
    return render(request,'todo.html',{'tasks':ob})
   else:
       ob=models.todo.objects.filter(username=request.user).order_by('timestamp').reverse
       print(models.todo.timestamp)
       return render(request,'edit.html',{'tasks':ob})
@login_required(login_url='login/')
def signout(request):
  logout(request)
  return redirect('login/')
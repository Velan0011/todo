from django.shortcuts import render
from django.http import HttpResponse
from .models import verify,mydb
from django.contrib import messages
# Create your views here.
def home(request):
       return render(request,'verify.html')
def verif(request):
        username=request.GET['username']
        password=request.GET['password']
        if verify.objects.filter(user_name=username,password=password).exists():
             return render(request,'home.html')
        else:
              messages.info(request,"username or password is incorrect")
              messages.info(request,"not correct",extra_tags="no")
              return render(request,"verify.html")

def home2(request):
    name1=request.GET['name1']
    name2=request.GET['name2']
    name1=name1.replace(" ","")
    name2=name2.replace(" ","")
    flames="flames"
    f={"f":"friendship","l":"love","a":"affection","m":"marriage life","e":"enemy","s":"sister like relationship"}
    for i in name1:
        if i in name2:
            name3=name1.replace(i,"",1)
            name4=name2.replace(i,"",1)
            name=name3+name4
    n=len(name)
    while(len(flames)>1):
        r=n%len(flames)-1
        if r==-1:
            flames=flames.replace(flames[-1],"",1)
        elif r==0:
            flames=flames.replace(flames[0],"",1)
        else:
            flames=flames[r+1:]+flames[:r]
    return HttpResponse(name1+" and "+name2+" are in "+f[flames])
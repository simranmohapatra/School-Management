from django.shortcuts import render,redirect
from home.models import A
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.


@login_required(login_url='/register')
def home(request):
    if request.method=='POST':
        d=request.POST
        a=d.get("name")
        b=d.get("phno")
        c=d.get("pin")
        e=d.get("address")

        A.objects.create(name=a,phno=b,pin=c,address=e)

    z=A.objects.all()
    context={'sim':z} #context use to send data from backend to frontend

    return render(request,"index.html",context)


def delete(request,id):
    # A.objects.filter(id=id).delete()
    c=A.objects.get(id=id)
    c.delete()
    return redirect("/")

def update(request,id):
    q=A.objects.get(id=id)
    if request.method=='POST':  #post use to send data from frontend to backend
        d=request.POST 
        a=d.get("name")
        b=d.get("phno")
        c=d.get("pin")
        e=d.get("address")
        q.name=a
        q.phno=b
        q.pin=c
        q.address=e
        q.save()
        return redirect("/")
    return render(request,"U.html",context={'upp':q})


def login_Page(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        username_1=User.objects.filter(username=username)

        if not username_1.exists():
            messages.info(request,"INVALID USERNAME")
            return redirect('/login')
        
        user=authenticate(username=username,password=password)
        if user is None:
             messages.error(request,'Invalid Username or Password')
             return redirect('/login')
        else:
            login(request,user)
            messages.success(request,"You are Successfully Logged In!")
            return redirect("/")
        
    return render(request,"login.html")


def logout_Page(request):
    logout(request)
    return redirect('/login')

def register(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request,"username is already exists")
            return redirect("/register")
        
        user=User.objects.create(first_name=first_name,last_name=last_name,username=username)
        user.set_password(password)
        user.save()
        messages.info(request,"account created")
        return redirect("/login")

    return render(request, "register.html")
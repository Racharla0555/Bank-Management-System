from django.shortcuts import render,redirect
from myBank.models import form
from django.contrib import messages
from random import randint


# Create your views here.
def home(request):
    return render(request,'home.html')

from .models import *
from  django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
def createacc(request):
    if request.method=="POST":
        name=request.POST['name']
        number=request.POST['number']
        email=request.POST['email']
        type=request.POST['type']
        balance=request.POST['balance']
        password1=request.POST['password1']
        password=request.POST['password']
        if password!=password1 :
            messages.error(request,"Passwords not matches")
        elif User.objects.filter(username=name):
            messages.error(request,"Username already exists...!")
        elif User.objects.filter(email=email):
            messages.error(request,"Email already taken...!")
        elif type=="Savings" and int(balance)<3000 :
            messages.error(request,"Deposit minimum balance")
        elif type=="Current" and int(balance)<1000 :
            messages.error(request,"Deposit minimum balance")
        else:
            User.objects.create_user(username=name,email=email,password=password1)
            user=User.objects.get(username=name)
            Account(user=user,number=number,type=type,balance=balance).save()      
            return redirect('/login')
    return render(request,'createacc.html')
from django.contrib.auth.decorators import login_required
@login_required()
def options(request):
    return render(request,'options.html')

def login1(request):
    if request.method=='POST':
        email=request.POST['email']
        pin=request.POST['pin']
        username=User.objects.get(email=email).username
        user=authenticate(username=username,password=pin)
        if user is not None:
            login(request,user)
            return redirect('/options')
    return render(request,'login.html')

def accdeatils (request):
    return render(request,"accdetail.html")

def signout (request):
    logout(request)
    return redirect(home)

def contactus(request):
    return render(request,'contactus.html')

def resetpin(request):
    return render(request,"resetpin.html")

def modifyacc(request):
    return render(request,"modifyacc.html")

def transaction(request):
    return render(request,"transaction.html")


""""
def accNumber(request):
    a=randint(100000,999999)
    print(a)
    """
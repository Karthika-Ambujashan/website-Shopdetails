from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def registration(request):
    return render(request,'registration.html',)   
def getDetails(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        data=Registerdb(username=username,password=password,email=email,phone=phone)
        data.save()
        return redirect('registration')
def login(request):
    return render(request,'login.html',)   
def getValue(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Registerdb.objects.filter(username=username,password=password).exists():
            return HttpResponse("Successfully logged in")
        else:
            return render(request,'login.html',{'msg':'Invalid user credentials'})
    else:
        return redirect('login')

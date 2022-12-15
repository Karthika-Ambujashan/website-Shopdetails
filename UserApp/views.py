from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from ShopApp.models import *

# Create your views here.
def index(request):
    data=Shopdb.objects.all()
    return render(request,'index.html',{'data':data})

def view(request,sid):
    data=Shopdb.objects.filter(id=sid)
    return render(request,'views.html',{'data':data})

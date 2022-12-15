from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def shopdetails(request):
    return render(request,'shopdetails.html',)   
def getData(request):
    if request.method == "POST":
        shopname=request.POST.get('shopname')
        shoplocation=request.POST.get('shoplocation')
        shopcontactno=request.POST.get('shopcontactno')
        simage=request.FILES['shop_image']
        data=Shopdb(shopname=shopname,shoplocation=shoplocation,shopcontactno=shopcontactno,shop_image=simage)
        data.save()
        return redirect('shopdetails')
def viewshopdetails(request):
    data=Shopdb.objects.all()
    return render(request,'viewshopdetails.html',{'data':data})
def delete(request,sid):
    Shopdb.objects.filter(id=sid).delete()
    return redirect('viewshopdetails')
def edit(request,sid):
    data=Shopdb.objects.filter(id=sid)
    return render(request,'edit.html',{'data':data})
def update(request,sid):
    if request.method == "POST":
        shopame=request.POST.get('shopname')
        shoplocation=request.POST.get('shoplocation')
        shopcontactno=request.POST.get('shopcontactno')
        try:
            img_c = request.FILES['shop_image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Shopdb.objects.get(id=sid).shop_image
        Shopdb.objects.filter(id=sid).update(shopname=shopame,shoplocation=shoplocation,shopcontactno=shopcontactno,shop_image=file)
        return redirect('viewshopdetails')             

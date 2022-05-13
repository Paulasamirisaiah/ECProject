from django.shortcuts import render
from .models import category,product

def home(request):
    allcategory = category.objects.all()
    allproducts = product.objects.all().order_by("-id")
    return render(request,'pages/home.html',{"allproducts":allproducts,"allcategory":allcategory})

def Category(request,categoryid):
    allcategory = category.objects.all()
    allproducts = product.objects.all().filter(catagory_id=categoryid).order_by("-id")
    return render(request,'pages/category.html',{"allproducts":allproducts,"allcategory":allcategory})

def Product(request,productid):
    allcategory = category.objects.all()
    myproduct = product.objects.get(id=productid)
    allproducts = product.objects.all().filter(id=productid).order_by("-id")    
    return render(request,'pages/product.html',{"allcategory":allcategory,"myproduct":myproduct,"allproducts":allproducts})


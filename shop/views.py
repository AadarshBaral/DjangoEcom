
from math import prod
from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from shop.models import Product
from shop.models import Contact

# Create your views here.
def index(request):

    products = Product.objects.all()
    productCategories = Product.objects.values('category','id')
    categories = {item['category'] for item in productCategories}
    # print(categories)
    allProducts = []
    for category in categories:
        products= Product.objects.filter(category = category)[:4]
        allProducts.append(products)
    # print(allProducts)
    
    context = {'allProducts' : list(allProducts)}
    return render(request,'shop/index.html',context)
def about(request):
        return render(request,'shop/about.html')

def contact(request):

    if request.method == "POST":
        name = request.POST.get('name','')
        phone = request.POST.get('phone','')
        email = request.POST.get('email','')
        need = request.POST.get('need','')
        message = request.POST.get('message','')
        contact  = Contact(name = name,email= email,phone = phone, message = message,need = need)
        contact.save()
        # Sending the Email
        # return redirect('/shop')
    return render(request,'shop/contact.html')



def tracker(request):
    return HttpResponse("TrPageacker ")
def search(request):
    return HttpResponse("Search Page")


def productview(request,myid):
    #Fetch the product using the id
    product= Product.objects.filter(id = myid)
    context = {'prod' : product[0]}
    return render(request,'shop/prodview.html',context)

def cart(request):
    return render(request,'shop/cart.html')

def checkout(request):
    return HttpResponse("checkout Page")
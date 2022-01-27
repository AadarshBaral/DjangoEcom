from math import prod
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product

# Create your views here.
def index(request):

    products = Product.objects.all()
    productCategories = Product.objects.values('category','id')
    categories = {item['category'] for item in productCategories}
    print(categories)
    allProducts = []
    for category in categories:
        products= Product.objects.filter(category = category)[:4]
        allProducts.append(products)
    print(allProducts)

    # cat= []
    # dic = {}
    # for i in products:
    #     # print(i, i.category)
    #     if i.category in categories:
        
    #         print(i)
    #         # dic[i.category] = [i]
    #         # dic.update({i.category:[i]})
        
            

    # print(dic)
    # print(cat_to_value)
    
    context = {'allProducts' : list(allProducts)}
    return render(request,'shop/index.html',context)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return HttpResponse("Contact Page")
def tracker(request):
    return HttpResponse("TrPageacker ")
def search(request):
    return HttpResponse("Search Page")
def prodView(request):
    return HttpResponse("Product View Page")
def checkout(request):
    return HttpResponse("checkout Page")
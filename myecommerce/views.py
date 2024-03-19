from django.shortcuts import render

def index(request):
    context={}
    return render(request, "ecommerce/index.html", context)

def store(request):
    context={}
    return render(request, "ecommerce/store.html", context)

def cart(request):
    context= {}
    return render(request, "ecommerce/cart.html", context)

def checkout(request):
    context= {}
    return render(request, "ecommerce/checkout.html", context)

# Create your views here.

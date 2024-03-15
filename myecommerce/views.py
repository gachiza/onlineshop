from django.shortcuts import render



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

from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, "ecommerce/main.html")

def store(request):
    return render(request, "ecommerce/store.html")

def cart(request):
    return render(request, "ecommerce/cart.html")

def checkout(request):
    return render(request, "ecommerce/checkout.html")

# Create your views here.

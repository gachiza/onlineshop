from django.shortcuts import render, HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import *
# Create your views here.




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
def login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                return HttpResponse('logged in')
    else:
        form = UserLogin()
        context = {
            "form": form
        }
    return render(request, "ecommerce/login.html",context)
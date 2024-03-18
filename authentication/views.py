from django.shortcuts import render, HttpResponse
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
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
    return render(request, "auth/login.html",context)
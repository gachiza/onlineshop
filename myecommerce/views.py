from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import json


def item_list(request):
    items = Item.objects.all()
    query = request.GET.get('q')
    if query:
        items = items.filter(name__icontains=query)
    return render(request, 'your_template.html', {'items': items})


def home(request):
     return render(request, 'ecommerce/home.html')

def store(request):
     products= Product.objects.all()
     context = {'products':products}
     return render(request, 'ecommerce/store.html', context)

def cart(request):
     
     if request.user.is_authenticated:
          customer=request.user.customer
          order, created = Order.objects.get_or_create(customer=customer,complete=False)
          items= order.orderitem_set.all()
     else:
        items= []
        order= {'get_cart_total':0, 'get_cart_items':0}


     context = {'items':items, 'order':order}
     return render(request, 'ecommerce/cart.html', context)

def checkout(request):
        if request.user.is_authenticated:
            customer=request.user.customer
            order, created = Order.objects.get_or_create(customer=customer,complete=False)
            items= order.orderitem_set.all()
        else:
            items= []
            order= {'get_cart_total':0, 'get_cart_items':0}

        context = {'items':items, 'order':order}
        return render(request, 'ecommerce/checkout.html', context)

def signup(request):
     form = UserCreationForm()
     if request.method=='POST':
          user=form.save()
          username= form.cleaned_data.get('username')
          raw_password = form.cleaned_data.get('password1')
          user = authenticate(username=username, password= raw_password)
          login(request,user)
          return store(request)
     
     context={"form":form}
     return render(request, 'ecommerce/signup.html')




def login(request):
     if request.method == 'POST':

          username = request.POST.get('username')
          user = authenticate(username=username, password=request.POST.get('password'))
          login(request,user)
     return render(request, 'ecommerce/login.html')

def updateItem(request):
     data = json.loads(request.body)
     productId = data['productId']
     action = data['action']
     print('Action:', action)
     print('ProductId:', productId)

     customer= request.user.customer
     product= Product.objects.get(id=productId)
     order, created = Order.objects.get_or_create(customer=customer, complete= False)
     OrderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

     if action == 'add':
          OrderItem.quantity  = (OrderItem.quantity + 1)
     elif action == 'remove':
          OrderItem.quantity = (OrderItem.quantity - 1)
     OrderItem.save()

     if OrderItem <= 0:
          OrderItem.delete()

     return JsonResponse('Item was added', safe=False)


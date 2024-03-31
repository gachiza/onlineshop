from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import JsonResponse
import json
from .forms import CustomerForm
from .forms import GroupForm
from .forms import SearchForm
from .models import Product
from django.http import HttpResponse
from .models import TermsAndConditions



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
          auth_login(request,user)
          return store(request)
     
     context={"form":form}
     return render(request, 'ecommerce/signup.html')




def login(request):
     if request.method == 'POST':

          username = request.POST.get('username')
          user = authenticate(username=username, password=request.POST.get('password'))
          if user:
               auth_login(request,user)
               return redirect("home")
     return render(request, 'ecommerce/login.html')

def log_out(request):
     logout(request)
     return redirect('home')

def updateItem(request):
     data = json.loads(request.body)
     productId = data['productId']
     action = data['action']
     print('Action:', action)
     print('ProductId:', productId)

     customer= request.user.customer
     product= Product.objects.get(id=productId)
     order, created = Order.objects.get_or_create(customer=customer, complete= False)
     Orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)

     if action == 'add':
          Orderitem.quantity  = (Orderitem.quantity + 1)
     elif action == 'remove':
          Orderitem.quantity = (Orderitem.quantity - 1)
     Orderitem.save()

     if Orderitem.quantity <= 0:
          Orderitem.delete()

     return JsonResponse('Item was added', safe=False)
def upload_file(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data
            form.save()
            # Redirect or render success page
    else:
        form = MyForm()
    return render(request, 'upload.html', {'form': form})

def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect or show success message
    else:
        form = GroupForm()
    return render(request, 'create_group.html', {'form': form})

def SearchForm(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Perform the search operation, for example:
            results = Product.objects.filter(title__icontains=query)
            return render(request, 'search_results.html', {'results': results})
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})
def product_search(request):
    query = request.GET.get('q')
    if query:
        # Perform search on Product objects (assuming 'name' and 'description' fields)
        search_results = Product.objects.filter(name__icontains=query) | Product.objects.filter(description__icontains=query)
    else:
        search_results = None
    return render(request, 'product_search_results.html', {'search_results': search_results, 'query': query})
def email_view(request):
    # Your view logic here
    return HttpResponse("This is the view for abdulssekyanzi@gmail.com")
def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Perform the search operation, for example:
            results = item_list.objects.filter(title__icontains=query)
            return render(request, 'search_results.html', {'results': results})
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})
def terms_and_conditions(request):
    terms = TermsAndConditions.objects.first()  # Assuming you have only one terms and conditions entry
    return render(request, 'terms_and_conditions.html', {'terms': terms})



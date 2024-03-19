from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Shopping


def index (request):
    return render(request,'shopping/index.html')

def shopping (request):
    myshopping=Shopping.objects.all().values()
    template=loader.get_template('shopping.html')
    context = {
    'myshopping': myshopping,
  }
    return render(request, 'shopping.html', context)  

def details(request, id):
  myshopping = Shopping.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myshopping': myshopping,
  }
  return render(request, 'details.html', {'myshopping': myshopping})

def main(request):
  template = loader.get_template('main.html')
  return render(request, 'main.html')

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return render(request,'testing')
    
# Create your views here.

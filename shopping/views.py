from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Shopping


def index (request):
    return render(request,'shopping/index.html')

def shopping (request):
    myshopping=Shopping.objects.all().values()
    template=loader.get_template('myfirst.html')
    context = {
    'myshopping': myshopping,
  }
    return HttpResponse(template.render(context, request))
# Create your views here.

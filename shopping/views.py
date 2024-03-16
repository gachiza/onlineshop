from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index (request):
    return render(request,'shopping/index.html')

def shopping (request):
    template=loader.get_template('myfirst.html')
    return HttpResponse(template.render())
# Create your views here.

from django.urls import path
from shopping.views import index
from shopping import views

app_name='shopping'
urlpatterns=[
    path("shopping/",views.index)
]

from django.urls import path 
from . import views 

urlpatterns=[
    path("", views.store, name="store"),
    path("cart/", views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path("login/", views.login, name="login"),
    path("sign-up/", views.login, name="sign-up"), #change these i put them just to fix errors
    path("register/", views.login, name="register"),# change these i put them to fix errors
]
from django.urls import path 
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
    path('home/', views.home, name= "home"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name= "signup"),
    path('update_item/', views.updateItem, name="update_-item"),
    path('items/', views.item_list, name='item_list'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
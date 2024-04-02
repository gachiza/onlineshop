from django.urls import path 
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from .views import product_search
from .views import search_view
from .views import terms_and_conditions

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
    path('home/', views.home, name= "home"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name= "signup"),
    path('update_item/', views.updateItem, name="updateItem"),
    path('items/', views.item_list, name='item_list'),
    path('logout/', views.log_out, name='logout'),
    path('abdulssekyanzi@gmail.com/', views.email_view, name='email_view'),
    path('search/',views.product_search, name='product_search'),
    path('search/', views.search_view, name='search'),
    path('terms-and-conditions/', terms_and_conditions, name='terms_and_conditions'),
    path('bug-report/', views.bug_report, name='bug_report'),
    path('bug-report/success/', views.bug_report_success, name='bug_report_success'),

    


    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
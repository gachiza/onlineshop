from django.test import SimpleTestCase
from django.urls import reverse, resolve
from myecommerce.views import store, home, cart,checkout, login, signup, updateItem, item_list



class TestUrls(SimpleTestCase):

    def test_store_is_resolved(self):
        url= reverse('store')
        self.assertEquals(resolve(url).func, store)
        

    
    def test_home_is_resolved(self):
        url= reverse('home')
        self.assertEquals(resolve(url).func, home)
        

    def test_cart_is_resolved(self):
        url= reverse('cart')
        self.assertEquals(resolve(url).func, cart)
    

    def test_checkout_is_resolved(self):
        url= reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)
        

    def test_login_is_resolved(self):
        url= reverse('login')
        self.assertEquals(resolve(url).func, login)
        

    def test_signup_is_resolved(self):
        url= reverse('signup')
        self.assertEquals(resolve(url).func, signup)
        

    def test_updateItem_is_resolved(self):
        url= reverse('updateItem')
        self.assertEquals(resolve(url).func, updateItem)
        

    def test_item_list_is_resolved(self):
        url= reverse('item_list')
        self.assertEquals(resolve(url).func, item_list)
        
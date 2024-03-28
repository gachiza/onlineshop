from django.test import TestCase, Client
from django.urls import reverse
from myecommerce.models import Item, Customer, Product, Order, OrderItem, DeliveryAddress
from 



class Testviews(TestCase):

    def test_customer_list_GET(self):
        client = Client()

        response = client.get(reverse('list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUse()
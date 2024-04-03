from django.db import models
from django.contrib.auth.models import User
# models.

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)


class Customer(models.Model): 
    user= models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email= models.CharField(max_length=200)
    image = models.ImageField(upload_to='customer_images', null=True, blank=True)
    home_adress=models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Product(models.Model):
    name= models.CharField(max_length=200)
    price= models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=True)
    image= models.ImageField(null=True, blank= True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered= models.DateTimeField(auto_now_add=True)
    complete= models.BooleanField(default=False)
    transaction_id= models.CharField(max_length=100,null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total= sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems= self.orderitem_set.all()
        total= sum([item.quantity for item in orderitems])
        return total 


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order= models.ForeignKey(Order, on_delete= models.SET_NULL,null=True)
    quantity= models.IntegerField(default=0, null=True, blank=True)
    date_added= models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total= self.product.price * self.quantity
        return total


class DeliveryAddress(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.SET_NULL, null= True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    adress= models.CharField(max_length=200,null=False)
    city= models.CharField(max_length=200,null=False)
    building = models.CharField(max_length=200,null=True)
    date_added= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.address

class MyForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Group(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='group_images/', null=True, blank=True)
    
class TermsAndConditions(models.Model):
    content = models.TextField()

    def __str__(self):
        return "Terms and Conditions"
class BugReport(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    reported_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

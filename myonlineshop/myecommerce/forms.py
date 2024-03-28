from django.contrib.auth.models import User
from django import forms
from .models import Customer

class UserLogin(): 
    class Meta:
        model = User
        fields = ['username', 'password']
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'image']
from django.contrib.auth.models import User
from django import forms
from .models import Customer
from .models import Group

class UserLogin(): 
    class Meta:
        model = User
        fields = ['username', 'password']
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'image']
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'image']
class SearchForm(forms.Form):
    query = forms.CharField(label='Search')

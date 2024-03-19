from django.contrib import admin
from .models import Shopping

# Register your models here.

class ShoppingAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  
admin.site.register(Shopping, ShoppingAdmin)
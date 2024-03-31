from django.contrib import admin
from .models import *
from .models import TermsAndConditions

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(DeliveryAddress)
admin.site.register(MyForm)
admin.site.register(Group)
admin.site.register(TermsAndConditions)

# Register your models here.

from django.contrib import admin

from . models import Customer, Order, Category, Product

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Product)
from django.contrib import admin
from .models import Customers, Products, Sales

@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    pass

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    pass

@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    pass

from django.shortcuts import render
from mydjangoapp.models import Customers, Products, Sales

def index_page(request):
    customers = Customers.objects.all()
    products = Products.objects.all()
    sales = Sales.objects.all()

    context = {
        'customers': customers,
        'products': products,
        'sales': sales,
    }

    return render(request, 'index.html', context)
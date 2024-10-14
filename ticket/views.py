from django.shortcuts import render
from django.http import HttpResponse
from ticket.models import Product

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'ticket/index.html', context )
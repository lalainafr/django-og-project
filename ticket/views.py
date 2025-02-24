from django.shortcuts import render, redirect
from ticket.models import Product
from .form import ProductForm

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'ticket/index.html', context )

def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'ticket/product-details.html', context )

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        # reuqest.FILES quand il y a un fochoer pou image dans le formulaire

        if form.is_valid():
            form.save()
            return redirect('ticket')
        else:
            return redirect('cart_summary')

    else:
        form = ProductForm()
        context = {'form': form}
        return render(request, 'ticket/create_product.html', context)

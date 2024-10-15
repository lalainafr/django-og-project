from django.shortcuts import render, get_object_or_404 # if it doesn't exist return 404 error
from .cart import Cart # the created session
from ticket.models import Product
from django.http import JsonResponse  # send to json data 



def cart_summary(request):
    context = {}
    return render(request, 'cart/cart-summary.html', context)

def cart_add(request):
    # Get the cart
    cart = Cart(request)
    # test for POST
    # if the action is 'post' as specified on the AJAX
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id')) # product id passed in the AJAX
        
        # lookup product in the DB
        product = get_object_or_404(Product, id=product_id)
        
        # save to session
        cart.add(product=product) # 'add' methode to be implemented in cart.py
        
        # return response
        response = JsonResponse({'Product  Name: ' : product.name})
        return response
        

def cart_delete(request):
    pass

def cart_update(request):
    pass
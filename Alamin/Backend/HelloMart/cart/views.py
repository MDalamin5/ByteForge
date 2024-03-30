from django.shortcuts import render
from store.models import Product
from . models import Cart, CartItem

# Create your views here.

def cart_id(request):
    cart = request.session.session_key
    print(cart)

def cart(request):
    return render(request, 'cart/cart.html')

def add_to_cart(request, product_id):
    product = Product.objects.get(id = product_id)
    print(product)
    cart_id = request.session.session_key
    # print(cart)
    cart = Cart.objects.create(
        cart_id = cart_id
    )
    cart.save()
    cart_item = CartItem.objects.create(
        product = product,
        cart = cart,
        quantity = 1,
    )
    cart_item.save()
    
    
    return render(request, 'cart/cart.html')

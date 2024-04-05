from django.shortcuts import render, redirect
from store.models import Product
from . models import Cart, CartItem

# Create your views here.

def sessionID(request):
    session_id = request.session.session_key
    return session_id

def cart(request):
    session_id = request.session.session_key # bring session id from browser
    cartid = Cart.objects.get(cart_id = session_id) # cart model k bar kora anlm
    # print('hellollllllll',cartid)
    cart_id = Cart.objects.filter(cart_id = session_id).exists()
    cart_items = None
    if cart_id:
        cart_items = CartItem.objects.filter(cart = cartid)
        print(cart_items)
    return render(request, 'cart/cart.html', {'cart_items' : cart_items})






def add_to_cart(request, product_id):
    product = Product.objects.get(id = product_id)
    # print(product)
    session_id = request.session.session_key
    cart_id = Cart.objects.filter(cart_id = session_id).exists()

    if cart_id:
        cart_item = CartItem.objects.filter(product=product).exists()
        if cart_item:
            item = CartItem.objects.get(product=product)
            item.quantity += 1
            item.save()
        else:
            cart_id = Cart.objects.get(cart_id = session_id)
            item = CartItem.objects.create(
            product = product,
            cart = cart_id,
            quantity = 1,
            )
            item.save()
    else:
        cart = Cart.objects.create(
            cart_id = session_id
        )
        cart.save()
        cart_id = Cart.objects.get(cart_id = session_id)
        item = CartItem.objects.create(
        product = product,
        cart = cart_id,
        quantity = 1,
        )
        item.save()
    
    
    
    return redirect('cart')


def remove_cart(request, product_id):
    print('helllllllllo',product_id)
    product = Product.objects.get(id = product_id)
    session_id = request.session.session_key
    cartid = Cart.objects.get(cart_id = session_id)
    cart_item = CartItem.objects.get(cart = cartid, product= product)
    print(cart_item)
    
    return redirect('cart')
    






from django.shortcuts import render, redirect
from store.models import Product
from . models import Cart, CartItem
from django.db.models import Q

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def get_create_session(request):
    if not request.session.session_key:
        request.session.create()
        
    return request.session.session_key


def cart(request):
    cart_items = None
    tax = 0
    total = 0
    grand_total = 0
    
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user = request.user)
        for item in cart_items:
            total += item.product.price * item.quantity
        tax = (total*2)/100
    else:
        session_id = get_create_session(request) # session id nea aslm
        cartid = Cart.objects.get(cart_id = session_id)
        cart_id = Cart.objects.filter(cart_id = session_id).exists() # ai session ala kono cart is exists or not in database
        
        if cart_id:
            # cart_items = CartItem.objects.filter(cart__cart_id = session_id) # if you this line do not use 9 & 13 no line its work in single line
            cart_items = CartItem.objects.filter(cart = cartid)
            for item in cart_items:
                total += item.product.price * item.quantity
        tax = (total*2)/100
        
    grand_total = total + tax
    
    
    
    
    return render(request, 'cart/cart.html', {'cart_items' : cart_items, 'tax' : tax, 'grand_total' : grand_total, 'total' : total})




def add_to_cart(request, product_id):
    product = Product.objects.get(id = product_id)
    session_id = get_create_session(request)
    
    if request.user.is_authenticated:
        cart_item = CartItem.objects.filter(product = product, user = request.user).exists()
        if cart_item:
            item = CartItem.objects.get(product = product)
            item.quantity += 1
            # item.product.stock -= 1
            
            item.save()
            # item.product.save()
        else:
            # cart_id = Cart.objects.get(cart_id = session_id)
            item = CartItem.objects.create(product = product, quantity = 1, user = request.user)
            item.save()
            
    else: # if the usr is not authenticated
        cart_id = Cart.objects.filter(cart_id = session_id).exists()
        if cart_id: # have a cart not increase or decrease the cart-item
            cart_item = CartItem.objects.filter(product = product).exists()
            if cart_item:
                item = CartItem.objects.get(product = product)
                item.quantity += 1
                # item.product.stock -= 1
                
                item.save()
                # item.product.save()
            else:
                cart_id = Cart.objects.get(cart_id = session_id)
                item = CartItem.objects.create(product = product, cart = cart_id, quantity = 1)
                item.save()
        else:
            cart = Cart.objects.create(cart_id = session_id)
            cart.save()
            
            cart_id = Cart.objects.get(cart_id = session_id)
            item = CartItem.objects.create(product = product, cart = cart_id, quantity = 1)
            item.save()
    
    
    return redirect('cart')



def remove_cart_item(request, product_id):
    print('the product ID is: ', product_id)
    product = Product.objects.get(id = product_id)
    # session_id = request.session.session_key
    # cartid = Cart.objects.get(cart_id = session_id)
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(product = product, user = request.user)
    else:
        session_id = request.session.session_key
        cartid = Cart.objects.get(cart_id = session_id)
        cart_item = CartItem.objects.get(product = product, cart_id = cartid)
    
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        
        product.stock += 1
        product.save()
    else:
        cart_item.delete()
    
    print(cart_item)
    
    
    return redirect('cart')


def remove_cart(request, product_id):
    product = Product.objects.get(id = product_id)
    # session_id = request.session.session_key
    # cartid = Cart.objects.get(cart_id = session_id)
    
    # cart_item = CartItem.objects.get(product = product, cart = cartid)
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(product = product, user = request.user)
    else:
        session_id = request.session.session_key
        cartid = Cart.objects.get(cart_id = session_id)
        cart_item = CartItem.objects.get(product = product, cart = cartid)
    cart_item.delete()
    
    return redirect('cart')



def checkout(request):
    print(request.POST)
    cart_items = None
    tax = 0
    total = 0
    grand_total = 0
    
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user = request.user)
        for item in cart_items:
            total += item.product.price * item.quantity
        tax = (total*2)/100
    else:
        session_id = get_create_session(request) # session id nea aslm
        cartid = Cart.objects.get(cart_id = session_id)
        cart_id = Cart.objects.filter(cart_id = session_id).exists() # ai session ala kono cart is exists or not in database
        
        if cart_id:
            # cart_items = CartItem.objects.filter(cart__cart_id = session_id) # if you this line do not use 9 & 13 no line its work in single line
            cart_items = CartItem.objects.filter(cart = cartid)
            for item in cart_items:
                total += item.product.price * item.quantity
        tax = (total*2)/100
        
    grand_total = total + tax
    
    
    
    
    return render(request, 'cart/place-order.html', {'cart_items' : cart_items, 'tax' : tax, 'grand_total' : grand_total, 'total' : total})
    
    
    
    


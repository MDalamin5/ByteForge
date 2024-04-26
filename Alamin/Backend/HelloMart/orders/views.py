from django.shortcuts import render, redirect
from cart.models import Cart, CartItem
from . forms import OrderForm

# Create your views here.


def get_create_session(request):
    if not request.session.session_key:
        request.session.create()
        
    return request.session.session_key


def orderComplete(request):
    return render(request, 'orders/order_complete.html')


def place_order(request):
    print(request.POST)
    cart_items = None
    tax = 0
    total = 0
    grand_total = 0
    
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user = request.user)
        if cart_items.count() < 1:
            return redirect('store')
        for item in cart_items:
            total += item.product.price * item.quantity
        tax = (total*2)/100
    """else:
        session_id = get_create_session(request) # session id nea aslm
        cartid = Cart.objects.get(cart_id = session_id)
        cart_id = Cart.objects.filter(cart_id = session_id).exists() # ai session ala kono cart is exists or not in database
        
        if cart_id:
            # cart_items = CartItem.objects.filter(cart__cart_id = session_id) # if you this line do not use 9 & 13 no line its work in single line
            cart_items = CartItem.objects.filter(cart = cartid)
            for item in cart_items:
                total += item.product.price * item.quantity
        tax = (total*2)/100"""
        
    grand_total = total + tax
    
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.order_total = grand_total
            form.instance.tax = tax
            form.instance.ip = request.META.get('REMOTE_ADDR')
            # form.instance.payment = 2
            saved_instance = form.save()  # Save the form data to the database
            form.instance.order_number = saved_instance.id
            
            form.save()   
            # print('form data printing', form)
    return render(request, 'orders/place-order.html', {'cart_items' : cart_items, 'tax' : tax, 'grand_total' : grand_total, 'total' : total})

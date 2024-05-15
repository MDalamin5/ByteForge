from django.shortcuts import render, redirect
from . forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from cart.models import Cart, CartItem
from orders.models import Order, OrderProduct
# Create your views here.

def get_create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data.get('first_name'))
            user = form.save()
            login(request, user)
            
            
            return redirect('cart')
            
    
    
    return render(request, 'accounts/register.html', {'form' : form})

def user_login(request):
    if request.method == "POST":
        # print(request.POST)
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = user_name, password = password)
        # print(user)
        # session_key = get_create_session(request)
        # cart = Cart.objects.get(cart_id = session_key)
        # is_cart_item_exists= CartItem.objects.filter(cart = cart).exists()
        # if is_cart_item_exists:
        #     cart_item = CartItem.objects.filter(cart = cart)
        #     for item in cart_item:
        #         item.user = user
        #         item.save()
        login(request, user)
        return redirect('profile')
    return render(request, 'accounts/signin.html')


def user_logout(request):
    logout(request)
    return redirect('login')

def profile(request):
    orders = Order.objects.order_by('-created_at').filter(user_id=request.user.id, is_ordered=True)
    orders_count = orders.count()
   
    context = {
        'orders_count': orders_count,
    }
    return render(request, 'accounts/dashboard.html',context)


def my_order(request):
    
    orders = Order.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
    context = {
        'orders': orders,
    }
    
    return render(request, 'accounts/my_order.html', context)

def edit_profile(request):
    return render(request, 'accounts/edit_profile.html')

def change_password(request):
    if request.method == "POST":
        cur_pass = request.POST.get('current_password')
        print(cur_pass)
        print(request.POST)
    return render(request, 'accounts/change_password.html')

def forgot_password(request):
    return render(request, 'accounts/forgot_password.html')

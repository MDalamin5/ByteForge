from django.shortcuts import render, redirect
from . forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('first_name'))
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
        print(user)
        login(request, user)
        return redirect('profile')
    return render(request, 'accounts/signin.html')


def user_logout(request):
    logout(request)
    return redirect('login')

def profile(request):
    return render(request, 'accounts/dashboard.html')



# this line is add from alamin branceh
# this is new line

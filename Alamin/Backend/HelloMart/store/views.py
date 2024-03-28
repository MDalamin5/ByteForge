from django.shortcuts import render
from . models import Product

# Create your views here.
def store(request):
    products = Product.objects.filter(is_available = True)
    
    # for item in products: # unit-test code
    #     print(item.product_name, item.price, item.is_available)
    
    return render(request, 'store/store.html', {'products' : products})

def productDetail(request):
    return render(request, 'store/product-detail.html')

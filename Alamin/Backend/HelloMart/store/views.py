from django.shortcuts import render, get_object_or_404
from . models import Product
from category.models import Category


# Create your views here.
def store(request, category_slug=None):
    category = None
    products = None
    categories = Category.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(is_available = True, category = category)
    else:
        products = Product.objects.filter(is_available = True)
    
    # print(categories)
    # for item in products: # unit-test code
    #     print(item.product_name, item.price, item.is_available)
    
    context = {'products' : products, 'categories' : categories}
    return render(request, 'store/store.html', context)

def productDetail(request):
    return render(request, 'store/product-detail.html')

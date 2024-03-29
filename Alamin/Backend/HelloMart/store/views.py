from django.shortcuts import render, get_object_or_404
from . models import Product
from category.models import Category
from django.core.paginator import Paginator

# Create your views here.
def store(request, category_slug=None):
    category = None
    products = None
    categories = Category.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(is_available = True, category = category)
        paginator = Paginator(products, 1)
        
    else:
        products = Product.objects.filter(is_available = True)
        paginator = Paginator(products, 2)
        paged_product = paginator.get_page(1)
        
        for i in paged_product:
            print(i)

    
    # paginator Section
    
    
    
    context = {'products' : products, 'categories' : categories}
    return render(request, 'store/store.html', context)

def productDetail(request):
    return render(request, 'store/product-detail.html')

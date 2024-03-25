from django.shortcuts import render

# Create your views here.
def store(request):
    return render(request, 'store/store.html')

def productDetail(request):
    return render(request, 'store/product-detail.html')

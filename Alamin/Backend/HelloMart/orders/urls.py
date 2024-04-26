from django.urls import path
from . import views

urlpatterns = [
    path('order_complete/', views.orderComplete, name='order_complete'),
    path('place_order/', views.place_order, name='place_order'),
]

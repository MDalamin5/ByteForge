from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('signin/', views.user_login),
    path('profile/', views.profile)
]

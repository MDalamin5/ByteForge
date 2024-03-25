from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('signin/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile')
]

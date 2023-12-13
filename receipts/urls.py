from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_hello, name='home'),
    path('login/', views.loginView, name='login'),
    path('register/', views.registerView, name='register'),
    path('logout/', views.logoutView, name='logout'),
    path('receipts/', views.getReceipts, name='all_receipts')
]
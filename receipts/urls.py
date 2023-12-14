from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_hello, name='home'),
    path('login/', views.loginView, name='login'),
    path('register/', views.registerView, name='register'),
    path('logout/', views.logoutView, name='logout'),
    path('receipts/', views.getReceipts, name='my_receipts'),
    path('receipt/<int:id>', views.getReceipt, name='receipt'),
    path('receipts/add', views.addReceipt, name='add_receipt'),
    path('receipt/<int:id>/update', views.updateReceipt, name='update_receipt'),
    path('receipt/<int:id>/delete', views.deleteReceipt, name='delete_receipt')
]
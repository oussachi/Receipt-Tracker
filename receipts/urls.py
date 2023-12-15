from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_hello, name='home'),                                         # Home page
    path('login/', views.loginView, name='login'),                                  # Login page
    path('register/', views.registerView, name='register'),                         # Registration page
    path('logout/', views.logoutView, name='logout'),                               # Logout Endpoint
    path('receipts/', views.getReceipts, name='my_receipts'),                       # User's receipts page
    path('receipt/<int:id>', views.getReceipt, name='receipt'),                     # User's speicific receipt page
    path('receipts/add', views.addReceipt, name='add_receipt'),                     # Add receipt page
    path('receipt/<int:id>/update', views.updateReceipt, name='update_receipt'),    # Update receipt page
    path('receipt/<int:id>/delete', views.deleteReceipt, name='delete_receipt')     # Delete receipt page
]
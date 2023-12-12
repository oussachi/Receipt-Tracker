from django.urls import path
from . import views

urlpatterns = [
    path('receipts/hello/', views.say_hello)
]
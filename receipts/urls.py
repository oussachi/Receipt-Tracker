from django.urls import path
from . import views

urlpatterns = [
    path('/', views.say_hello),
    path('login/', views.login),
    path('register/', views.register)
]
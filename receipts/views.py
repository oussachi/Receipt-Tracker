from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.

def say_hello(request):
    return HttpResponse('hello world')


# ----------------------- User views -------------------------- #

def login(request):
    return render(request, 'login.html')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form' : form}
    return render(request, 'register.html', context)

def logout(request):
    return
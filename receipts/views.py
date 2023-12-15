from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from .forms import CreateUserForm, ReceiptForm
from .models import Receipt, User

# Create your views here.

# A basic view for the home page
# prints the authenticated user name
def say_hello(request):
    context = {'user' : get_user(request)}
    return render(request, 'home.html', context)


# ----------------------- User views -------------------------- #

# The login view using Django built-in auth functions
# The login is done using the username and the password
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            return redirect('login')
    context = {}
    return render(request, 'login.html', context)

# The register view using a custom User form
# The request contains a username, email, password and password confirmation
def registerView(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    context = {'form' : form}
    return render(request, 'register.html', context)

# The logout view using Django built in logout function
# Simply, logs the user out
def logoutView(request):
    logout(request)
    return redirect('login')

# ------------------------ Receipt views -------------------------- #

# View that returns the athenticated user's receipts
# The user is retrieved using Django's get_user()
def getReceipts(request):
    username = get_user(request)
    receipts = Receipt.objects.filter(owner=username)
    context = {'receipts' : receipts}
    return render(request, 'all_receipts.html', context)

# View that returns one the athenticated user's receipts, specified by the id
# The user is retrieved using Django's get_user()
def getReceipt(request, id):
    username = get_user(request)
    receipt = Receipt.objects.filter(owner=username, pk=id).first()
    context = {'receipt': receipt}
    return render(request, 'receipt.html', context)

# View that adds a receipt and marks it to the authenticated user, using a custom Receipt form
# The user is retrieved using Django's get_user()
def addReceipt(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            username = get_user(request)
            receipt = form.save(commit=False)
            receipt.owner = username
            receipt.save()
            return redirect('my_receipts')
    
    form = ReceiptForm()
    context = {'form':form}
    return render(request, 'add_receipt.html', context)
            
# View that updates one of the authenticated user's receipts, specified by id, using a custom Receipt form
# The user is retrieved using Django's get_user()
def updateReceipt(request, id):
    username = get_user(request) 
    receipt = Receipt.objects.get(owner=username, pk=id)

    if request.method == 'POST':
        form = ReceiptForm(request.POST, instance=receipt)
        if form.is_valid():
            form.save()
            return redirect('my_receipts')
    form = ReceiptForm(instance=receipt)
    context = {'form' : form}
    return render(request, 'update_receipt.html', context)

# View that deletes one of the authenticated user's receipts, specified by id
def deleteReceipt(request, id):
    username = get_user(request)
    receipt = Receipt.objects.get(owner=username, pk=id)
    receipt.delete()
    return redirect('my_receipts')
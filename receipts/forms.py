from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Receipt

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields = ['store_name', 'date_of_purchase', 'item_list', 'total_amount']
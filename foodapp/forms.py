from django import forms
from .models import *

class Additemform(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name','item_description','item_price','item_image']

class Contactsform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','phone','desc']

class AdminForm(forms.Form):
    Admin = forms.CharField()
    Password = forms.CharField()
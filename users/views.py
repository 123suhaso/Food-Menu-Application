from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()  
            messages.success(request, f"Welcome {username}, your account has been created successfully! and you can now login")
            return redirect('foodapp:register')
    else:
        form = RegisterForm()  

    return render(request, 'users/register.html', {'form': form})



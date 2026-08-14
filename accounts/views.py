from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , logout
from django.shortcuts import render, redirect
from .forms import RegisterForm


def login_view(request):
    
    form = AuthenticationForm(request, data=request.POST or None)

    if form.is_valid():
        login(request, form.get_user())
        return redirect("home")

    return render(request, "accounts/login.html", {"form": form})

def register(request):

    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("home") 

    return render(request, "accounts/register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')

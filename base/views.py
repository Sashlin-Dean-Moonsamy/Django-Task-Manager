from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register_page(request):
    if request.POST:

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("base:dashboard")
    else:
        form = UserRegisterForm()
    return render(request, "registration/sign_up.html", {'form': form})

def home(request):
    return render(request, 'main_structure.html')

@login_required
def dashboard(request):
    return render(request, 'base/dashboard.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm

# Create your views here.


def user_register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    form = UserRegisterForm()
    return render(request, 'registration/user_register.html', {'form': form})


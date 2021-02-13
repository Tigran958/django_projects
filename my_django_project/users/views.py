from django.shortcuts import render, redirect
from .forms import UserRegistrForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def create_user(request):
    form = UserRegistrForm()

    if request.method == 'POST':
        form = UserRegistrForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.data.get('username')
            password = form.data.get("password1")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('home_page')

    return render(request, "users/create_user.html", {'form': form})

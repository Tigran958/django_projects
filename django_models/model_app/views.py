from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Message


# Create your views here.

def home(request):
	users = User.objects.all()

	return HttpResponse(F"{users[0]} and {users[1]}")

def message_view(request):
	messages = Message.objects.all()


	return HttpResponse(messages)

def home_view(request):

	messages = Message.objects.all()
	users = User.objects.all()

	context = {
				"users": users,
				"messages": messages,
				}

	return render(request, 'model_app/home.html', context)

def user_register(request):

	if request.method == "POST":
		form = UserCreationForm(request.POST)
		
		if form.is_valid():
			form.save()

			return redirect("home_view")


	form = UserCreationForm()

	content = {'form':form}

	return render(request, "model_app/register.html", content)
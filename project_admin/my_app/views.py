from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

dict_ = {
		"name": "Tigran",
		"last_name": "Danielyan"
		}


def home(request):
	content = {"name": dict_}
	return render(request, "my_app/welcome.html", content)
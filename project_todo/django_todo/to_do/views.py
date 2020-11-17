from django.shortcuts import render, redirect
from .models import NewTask
from .forms import TaskForm

# Create your views here.

def home(request):
	tasks = NewTask.objects.all()

	content = {"tasks": tasks}

	return render(request, 'to_do/home.html', content)

def task_update(request, pk):
	task = NewTask.objects.get(id=pk)


	if request.method == "POST":
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()

		return redirect("home")


	form = TaskForm(instance=task)

	content = {"form": form}
	return render(request, 'to_do/update.html', content)

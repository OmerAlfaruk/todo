from django.shortcuts import redirect, render
from .models import Task


# Create your views here.
def add_task(request):
    if request.method == "POST":
        task = request.POST["task"]
        Task.objects.create(task=task)

        # Here you would typically save the task to the database
        # For now, we will just render it back to the template
        return redirect("home")

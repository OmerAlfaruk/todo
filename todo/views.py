from django.shortcuts import get_object_or_404, redirect, render
from .models import Task


# Create your views here.
def add_task(request):
    if request.method == "POST":
        task = request.POST["task"]
        Task.objects.create(task=task)

        # Here you would typically save the task to the database
        # For now, we will just render it back to the template
        return redirect("home")


def mark_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()

    return redirect("home")


def mark_in_complete(request, task_id):

    task = get_object_or_404(Task, id=task_id)
    task.is_completed = False
    task.save()

    return redirect("home")


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()

    return redirect("home")


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.task = request.POST["task"]
        task.save()
        return redirect("home")
    return render(request, "edit_task.html", {"task": task})

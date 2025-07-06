from django.shortcuts import render

from todo.models import Task


def home(request):
    """
    Home view that renders the home page.
    """
    incompete_task = Task.objects.filter(is_completed=False).order_by("updated_at")
    completed_task = Task.objects.filter(is_completed=True)
    context = {
        "incomplet_tasks": incompete_task,
        "completed_tasks": completed_task,
        "tasks": incompete_task | completed_task,  # Combine both querysets
    }
    return render(request, "home.html", context)

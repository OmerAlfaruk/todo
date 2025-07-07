from django.urls import path
from . import views


urlpatterns = [
    path("add-task/", views.add_task, name="addTask"),
    path("mark-complete/<int:task_id>/", views.mark_complete, name="markComplete"),
    path(
        "mak-incomplete/<int:task_id>/", views.mark_in_complete, name="markIncomplete"
    ),
    path("edit-task/<int:task_id>/", views.edit_task, name="editTask"),
    # This is the URL to delete a task
    path("delete-tak/<int:task_id>/", views.delete_task, name="deleteTask"),
]

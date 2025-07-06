from django.urls import path
from . import views


urlpatterns = [
    path("add-task/", views.add_task, name="addTask"),
]

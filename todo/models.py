from django.db import models

# Create your models here.


class Task(models.Model):
    """
    Model representing a task in the to-do application.
    """

    task = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task

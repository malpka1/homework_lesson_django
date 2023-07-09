from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    objects = None
    title = models.CharField(max_length=128)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

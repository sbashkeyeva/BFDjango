from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone


class Todo(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(default=timezone.now())
    dueon = models.DateTimeField(default=timezone.now()+timedelta(days=2))
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.BooleanField(default=False)

    def __str__(self):
        return self.name

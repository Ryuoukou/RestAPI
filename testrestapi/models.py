from django.db import models
from markdown import markdown


# Create your models here.\

class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=00000)


    def __str__(self):
        return self.title


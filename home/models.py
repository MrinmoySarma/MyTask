from django.db import models
from django.utils import timezone


# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length = 250)
    note = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    mark = models.BooleanField(default = False)
    
    def __str__(self):
        return self.task
    

    
    
from django.db import models
from django.contrib.auth.models import User #attaching Task to User shows each user their own tasks only, not elses

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)

    def __str__ (self):
        return self.title

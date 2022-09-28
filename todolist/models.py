from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now=True, auto_now_add=False)
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)


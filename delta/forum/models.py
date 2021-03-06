from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Subforum(models.Model):
    category = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    description = models.TextField()

class Thread(models.Model):
    subforum = models.ForeignKey(Subforum, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

class Reply(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

class UserTitle(models.Model):
    COLORS = (
        ("primary", "Orange"), 
        ("secondary", "Grey"), 
        ("success", "Green"), 
        ("danger", "Pink"), 
        ("warning", "Red"), 
        ("info", "Blue"), 
        ("light", "White"), 
        ("dark", "Black")
    )

    color = models.CharField(max_length=10, choices=COLORS, default="secondary")
    title = models.CharField(max_length=20)
    users = models.ManyToManyField(to=User)
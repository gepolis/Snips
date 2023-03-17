from django.db import models
from Snippets.settings import choices
class Languages(models.Model):
    language = models.CharField(max_length=30)
    show = models.BooleanField(default=True)

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=30,choices=choices)
    code = models.TextField(max_length=500000)
    creation_date = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=True)
    author = models.IntegerField()

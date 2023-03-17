from django.db import models

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30)
    code = models.TextField(max_length=500000)
    creation_date = models.DateTimeField(auto_now=True)
    show = models.BooleanField(default=True)
    author = models.IntegerField()
class Languages(models.Model):
    language = models.CharField(max_length=30)
    show = models.BooleanField(default=True)

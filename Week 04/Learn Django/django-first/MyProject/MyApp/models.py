from django.db import models

# Create your models here.

class MovieInfo(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(max_length=100)
    summary = models.TextField(max_length=500)
    
from django.db import models

# Create your models here.
class Dj(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    best_known = models.CharField(max_length=100)
    description = models.TextField()

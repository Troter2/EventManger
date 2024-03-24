from django.db import models


# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ubication = models.CharField(max_length=200)
    creation_date = models.DateTimeField()
    photo = models.ImageField(upload_to='club/')

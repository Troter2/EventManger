from django.db import models

from Dj.models import Dj
from Club.models import Club


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    dj = models.ManyToManyField(Dj)

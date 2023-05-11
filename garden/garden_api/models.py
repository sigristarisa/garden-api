from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Plant(models.Model):
    plant_id = models.IntegerField()
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    seedlings_per_square = models.IntegerField()
    companions = ArrayField(models.CharField(max_length=80))
    enemies = ArrayField(models.CharField(max_length=80))
    created = models.DateTimeField(auto_now=False, auto_now_add=False)
    edited = models.DateTimeField(auto_now=True, auto_now_add=False)
    url = models.CharField(max_length=80)
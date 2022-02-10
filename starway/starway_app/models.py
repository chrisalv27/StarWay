from django.db import models

class User(models.model):
    name = models.CharField(max_length=20)
    birth = models.DateField(max_length=10)


class zodiac(models.model):
    name = models.CharField(max_length=10)
    signs = models.ManyToManyField('sign')

# Create your models here.

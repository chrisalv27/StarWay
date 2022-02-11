from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    birth = models.DateField(max_length=10)


class Zodiac(models.Model):
    name = models.CharField(max_length=10)
    matches = models.ManyToManyField('Zodiac', blank=True)
    element = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    planet = models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.name


# Create your models here.

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    birth = models.DateField(max_length=10)
    zodiac = models.ForeignKey('Zodiac', on_delete=models.PROTECT, null=True, blank=True)

class Zodiac(models.Model):
    name = models.CharField(max_length=25)
    matches = models.ManyToManyField('Zodiac', blank=True)
    element = models.CharField(max_length=10)
    description = models.CharField(max_length=550)
    planet = models.CharField(max_length=10,null=True)
    start_date = models.DateField(max_length=8, null=True)
    end_date = models.DateField(max_length=8, null=True)
    
    
    
    def __str__(self):
        return self.name


# Create your models here.

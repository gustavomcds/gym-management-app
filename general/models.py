from django.db import models

# Create your models here.
class Athlete(models.Model):

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=64)
    age = models.IntegerField()

class Coach(models.Model):

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=64)
    age = models.IntegerField()
from django.db import models

# Create your models here.
class Mood(models.Model):
    feeling = models.IntegerField()
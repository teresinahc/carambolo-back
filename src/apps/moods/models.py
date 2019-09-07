from django.db import models
import datetime

# Create your models here.
class Mood(models.Model):
    feeling = models.IntegerField(null=True,blank=True)
    thought = models.TextField(null=True,blank=True)
    racional_thought = models.TextField(null=True,blank=True)
    day = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now().date())
    updated_at = models.DateTimeField(auto_now=True, null=True,blank=True)
    #relationships
    # user = models.ForeignKey()
from django.db import models

#Create your models here.
class Data(models.Model):
    position=models.CharField(max_length=250)
    trackname=models.CharField(max_length=250)
    Artist=models.CharField(max_length=250)
    streams=models.BigIntegerField()
    date=models.DateField()
    country=models.CharField(max_length=250)
  

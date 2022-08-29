from datetime import date, datetime
from django.db import models
from datetime import date


# Create your models here.

class Familiar(models.Model):
    nombre= models.CharField(max_length=50)
    parentesco= models.CharField(max_length=50)
    dni= models.IntegerField()
    nacimiento= models.DateField(blank=True, null=True, default=date.today())
    
   
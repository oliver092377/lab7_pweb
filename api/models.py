from django.db import models

# Create your models here.
class Glass(models.Model):
    nombre = models.CharField(max_length=32)
    costo = models.IntegerField()
    id = models.IntegerField(primary_key=True)
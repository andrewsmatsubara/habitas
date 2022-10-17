from django.db import models

# Create your models here.

class Tree(models.Model):
    nome_popular = models.CharField(max_length=255)
    nome_cientifico = models.CharField(max_length=255)
    DAP = models.IntegerField()
    altura = models.IntegerField()
    data_da_coleta = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    laudo = models.URLField(max_length=255, blank=True)

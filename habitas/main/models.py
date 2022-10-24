from django.db import models

# Create your models here.

class Tree(models.Model):
    N_placa = models.FloatField(default=0)
    nome_popular = models.CharField(max_length=255)
    nome_cientifico = models.CharField(max_length=255)
    dap = models.IntegerField()
    altura = models.IntegerField()
    #data_da_coleta = models.DateField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    laudo = models.URLField(max_length=255, blank=True)

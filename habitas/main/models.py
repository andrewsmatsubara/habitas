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


class Post(models.Model):
    tree = models.ForeignKey(Tree,related_name="posts", on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_on", )
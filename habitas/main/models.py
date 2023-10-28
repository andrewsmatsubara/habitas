import math
from django.db import models

# Create your models here.
BETA0 = -0.906586
BETA1 = 1.60421
BETA2 = 0.37162


class Tree(models.Model):
    N_placa = models.FloatField(default=0)
    nome_popular = models.CharField(max_length=255)
    nome_cientifico = models.CharField(max_length=255)
    dap = models.IntegerField()
    altura = models.FloatField()
    # data_da_coleta = models.DateField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    laudo = models.URLField(max_length=255, blank=True)
    imagem = models.URLField(max_length=255, blank=True)

    @property
    def stored_co2(self) -> float:
        if self.dap <= 0 or self.altura <= 0:
            return 0

        return round(
            (
                math.exp(
                    BETA0 + BETA1 * math.log(self.dap) + BETA2 * math.log(self.altura)
                )
                / 1000
            ),
            4,
        )


class Post(models.Model):
    tree = models.ForeignKey(Tree, related_name="posts", on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_on",)

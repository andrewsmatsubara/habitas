import math
from django.db import models

# Create your models here.
BETA0 = -0.906586
BETA1 = 1.60421
BETA2 = 0.37162

PRECIPITATION = 1329  # Precipitação anual em São José dos Campos (L / m^2)
DIAMETER_RATIO = 4  # Razão média entre diâmetro da copa e diâmetro do tronco

RADIATION = 1661 # Radiação solar anual em São José dos Campos (kWh / m^2)
ENERGY_RATIO = 0.25 # Taxa de aproveitamento da energia das sombras


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
    plantado_por = models.CharField(max_length=100, default="DCTA")
    species = models.ForeignKey('Species', null=True, on_delete=models.SET_NULL)

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

    @property
    def stormwater_intercepted(self) -> float:
        if self.dap <= 0:
            return 0

        return math.pi * ((self.dap * DIAMETER_RATIO) / (2 * 100)) ** 2 * PRECIPITATION

    @property
    def conserved_energy(self) -> float:
        if self.dap <= 0:
            return 0

        return math.pi * ((self.dap * DIAMETER_RATIO) / (2 * 100)) ** 2 * RADIATION * ENERGY_RATIO

    @property
    def biodiversity(self) -> float:
        return self.species.bio_index if self.species is not None else 1


class Post(models.Model):
    tree = models.ForeignKey(Tree, related_name="posts", on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    specialized = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_on",)


class Species(models.Model):
    name = models.TextField()
    bio_index = models.FloatField()

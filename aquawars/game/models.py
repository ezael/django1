from django.db import models
from django.utils import timezone

# Create your models here.
class Classe(models.Model):
    nom = models.CharField(max_length=32)
    navigation = models.IntegerField()
    commerce = models.IntegerField()
    recherche = models.IntegerField()
    construction = models.IntegerField()
    aquaculture = models.IntegerField()
    combat = models.IntegerField()

    def __str__(self):
        return self.nom


class Serveur(models.Model):
    nom = models.CharField(max_length=16)
    lang = models.CharField(max_length=8)
    res_prod = models.FloatField()
    res_cap = models.FloatField()
    att_light = models.FloatField()
    att_medium = models.FloatField()
    att_heavy = models.FloatField()
    def_light = models.FloatField()
    def_medium = models.FloatField()
    def_heavy = models.FloatField()

    def __str__(self):
        return self.nom


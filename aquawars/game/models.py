from django.db import models
from django.utils import timezone

# Create your models here.
class Classe(models.Model):
    nom = models.CharField(max_length=32)
    navigation = models.IntegerField()
    commerce = models.IntegerField()
    recherche = models.IntegerField()
    construction = models.IntegerField()
    culture = models.IntegerField()
    combat = models.IntegerField()

    def __str__(self):
        return self.nom



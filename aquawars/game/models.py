from django.db import models
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.
class Classe(models.Model):
    nom = models.CharField(max_length=32)
    navigation = models.IntegerField(default=0)
    commerce = models.IntegerField(default=0)
    recherche = models.IntegerField(default=0)
    construction = models.IntegerField(default=0)
    aquaculture = models.IntegerField(default=0)
    combat = models.IntegerField(default=0)

    def __str__(self):
        return self.nom


class Serveur(models.Model):
    nom = models.CharField(max_length=16)
    lang = models.CharField(max_length=8)
    res_prod = models.FloatField(default=1)
    res_cap = models.FloatField(default=1)
    att_light = models.FloatField(default=1)
    att_medium = models.FloatField(default=1)
    att_heavy = models.FloatField(default=1)
    def_light = models.FloatField(default=1)
    def_medium = models.FloatField(default=1)
    def_heavy = models.FloatField(default=1)

    def __str__(self):
        return self.nom


class Station(models.Model):
    nom = models.CharField(max_length=32)
    joueur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    principale = models.IntegerField(default=1)
    coord_x = models.IntegerField(blank=True)
    coord_y = models.IntegerField(blank=True)
    coord_z = models.IntegerField(blank=True)
    res0 = models.IntegerField(default=10000)
    res1 = models.IntegerField(default=5000)
    res2 = models.IntegerField(default=0)
    res3 = models.IntegerField(default=0)
    res4 = models.IntegerField(default=0)
    res5 = models.IntegerField(default=0)
    res6 = models.IntegerField(default=0)
    res7 = models.IntegerField(default=0)
    cron_res0 = models.IntegerField(default=100)
    cron_res1 = models.IntegerField(default=50)
    cron_res2 = models.IntegerField(default=0)
    cron_res3 = models.IntegerField(default=0)
    cron_res4 = models.IntegerField(default=0)
    cron_res5 = models.IntegerField(default=0)
    cron_res6 = models.IntegerField(default=0)
    cron_res7 = models.IntegerField(default=0)
    cap_res0 = models.IntegerField(default=100000)
    cap_res1 = models.IntegerField(default=25000)
    cap_res2 = models.IntegerField(default=0)
    cap_res3 = models.IntegerField(default=0)
    cap_res4 = models.IntegerField(default=0)
    cap_res5 = models.IntegerField(default=0)
    cap_res6 = models.IntegerField(default=0)
    cap_res7= models.IntegerField(default=0)
    recherches_actu = models.IntegerField(default=0)
    recherches_max = models.IntegerField(default=1)
    flottes_actu = models.IntegerField(default=0)
    flottes_max = models.IntegerField(default=1)
    constructions_actu = models.IntegerField(default=0)
    constructions_max = models.IntegerField(default=1)
    navires_actu = models.IntegerField(default=0)
    navires_max = models.IntegerField(default=1)
    debris_actu = models.IntegerField(default=0)
    debris_max = models.IntegerField(default=1)

    def __str__(self):
        return self.nom


class TypeBatiment(models.Model):
    nom_admin = models.CharField(max_length=32)
    nom_web = models.CharField(max_length=256, blank=True)
    image = models.CharField(max_length=32, blank=True)
    description = models.TextField(blank=True)
    rech_mandatory = models.CharField(max_length=256, blank=True)
    cout_res0 = models.IntegerField(default=0)
    cout_res1 = models.IntegerField(default=0)
    cout_res2 = models.IntegerField(default=0)
    cout_res3 = models.IntegerField(default=0)
    cout_res4 = models.IntegerField(default=0)
    cout_res5 = models.IntegerField(default=0)
    cout_res6 = models.IntegerField(default=0)
    cout_res7 = models.IntegerField(default=0)
    timer = models.IntegerField(default=100)
    att_light = models.IntegerField(default=0)
    att_medium = models.IntegerField(default=0)
    att_heavy = models.IntegerField(default=0)
    def_light = models.IntegerField(default=0)
    def_medium = models.IntegerField(default=0)
    def_heavy = models.IntegerField(default=0)
    pv = models.IntegerField(default=100)
    gain_bat = models.IntegerField(default=0)
    gain_rech = models.IntegerField(default=0)
    gain_flot= models.IntegerField(default=0)

    def __str__(self):
        return self.nom_admin


class TypeNavire(models.Model):
    nom_admin = models.CharField(max_length=32)
    nom_web = models.CharField(max_length=256, blank=True)
    image = models.CharField(max_length=32, blank=True)
    description = models.TextField(blank=True)
    rech_mandatory = models.CharField(max_length=256, blank=True)
    bat_mandatory = models.CharField(max_length=256, blank=True)
    cout_res0 = models.IntegerField(default=0)
    cout_res1 = models.IntegerField(default=0)
    cout_res2 = models.IntegerField(default=0)
    cout_res3 = models.IntegerField(default=0)
    cout_res4 = models.IntegerField(default=0)
    cout_res5 = models.IntegerField(default=0)
    cout_res6 = models.IntegerField(default=0)
    cout_res7 = models.IntegerField(default=0)
    timer = models.IntegerField(default=100)
    att_light = models.IntegerField(default=0)
    att_medium = models.IntegerField(default=0)
    att_heavy = models.IntegerField(default=0)
    def_light = models.IntegerField(default=0)
    def_medium = models.IntegerField(default=0)
    def_heavy = models.IntegerField(default=0)
    pv = models.IntegerField(default=100)
    soute = models.IntegerField(default=0)
    vitesse = models.IntegerField(default=100)
    scanner = models.IntegerField(default=100)

    def __str__(self):
        return self.nom_admin


class TypeRecherche(models.Model):
    nom_admin = models.CharField(max_length=32)
    nom_web = models.CharField(max_length=256)
    image = models.CharField(max_length=32, blank=True)
    description = models.TextField(blank=True)
    timer = models.IntegerField(default=100)
    rech_mandatory = models.CharField(max_length=256, blank=True)
    bat_mandatory = models.CharField(max_length=256, blank=True)
    const_mandatory = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.nom_admin


class Player(models.Model):
    joueur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    serveur = models.ForeignKey(Serveur, on_delete=models.CASCADE, blank=True, null=True)
    date_creation = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.joueur.username

    def get_serveur(self):
        return self.serveur.nom



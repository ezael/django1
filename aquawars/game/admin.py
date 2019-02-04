from django.contrib import admin
from .models import *

# Register your models here.
class StationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nom',
        'joueur',
        'principale',
        'coord_x',
        'coord_y',
        'coord_z'
    )

    list_display_links = (
        'id',
        'nom'
    )

    search_fields = (
        'nom',
    )


class TypeBatimentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nom_admin'
    )

    list_display_links = (
        'id',
        'nom_admin'
    )


class TypeRechercheAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nom_admin'
    )

    list_display_links = (
        'id',
        'nom_admin'
    )


class TypeNavireAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nom_admin',
        'att_light',
        'att_medium',
        'att_heavy',
        'def_light',
        'def_medium',
        'def_heavy',
        'pv',
        'vitesse',
        'soute',
        'scanner'
    )

    list_display_links = (
        'id',
        'nom_admin'
    )


class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'joueur',
        'classe',
        'serveur',
        'date_creation'
    )

    list_display_links = (
        'id',
        'joueur'
    )


class ClasseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nom',
        'navigation',
        'commerce',
        'recherche',
        'construction',
        'aquaculture',
        'combat'
    )

    list_display_links = (
        'id',
        'nom'
    )


class StationConnueAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'joueur',
        'station'
    )

    list_display_links = (
        'id',
        'joueur',
        'station'
    )


admin.site.register(Classe, ClasseAdmin)
admin.site.register(Serveur)
admin.site.register(Station, StationAdmin)
admin.site.register(TypeBatiment, TypeBatimentAdmin)
admin.site.register(TypeNavire, TypeNavireAdmin)
admin.site.register(TypeRecherche, TypeRechercheAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(StationConnue, StationConnueAdmin)
admin.site.register(Flotte)

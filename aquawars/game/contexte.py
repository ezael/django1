from .models import *

def Contexte(request):
    # enregistrement de la page actuelle
    if 'page' in request.GET:
        page = request.GET['page']
    else:
        page = ""

    player = Player.objects.get(joueur=request.user.id)
    serveur = Serveur.objects.get(id=player.serveur.id)

    # on recupere la station principale du Player
    station_principale = Station.objects.get(
        joueur=request.user,
        principale=1
    )

    # on cherche s'il y a une session avec un ID de station
    # si OUI, on le prends
    # si NON, on met  la station principale
    id_station_actuelle = request.session.get('id_station_actuelle', station_principale.id)

    if id_station_actuelle != station_principale.id:
        station_actuelle = Station.objects.get(id=id_station_actuelle)
    else:
        station_actuelle = station_principale

    ctx = {
        "player": player,
        "serveur": serveur,
        "page": page,
        "station_principale": station_principale,
        "station_actuelle": station_actuelle
    }

    return ctx

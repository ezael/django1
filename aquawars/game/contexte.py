from .models import *
from .lib import *
from .lang.fr import fr
from .lang.en import en

def Contexte(request):
    global fr, en

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

    # on cherche les batiments de la station
    batiments = Batiment.objects.filter(
        station_id=station_actuelle
    )

    for item in batiments:
        item.nom = get_trad(serveur.lang, item.bat.nom_web)

    # on met la langue en fonction de celle du serveur
    if serveur.lang == "fr":
        trad = fr
    elif serveur.lang == "en":
        trad = en

    ctx = {
        "lang": serveur.lang,
        "trad": trad,
        "player": player,
        "serveur": serveur,
        "station_principale": station_principale,
        "station_actuelle": station_actuelle,
        "batiments": batiments,
        "bat_slot_dispo": station_actuelle.batiments_max - station_actuelle.batiments_actu,
        "bat_slot_max": station_actuelle.batiments_max,
    }

    return ctx

from .models import *

def get_trad(lang, txt):
    t = txt.split("#")

    trad = {}

    for item in t:
        x = item.split(".")

        trad[x[0]] = x[1]

    return trad[lang]


def new_bat(bat_id, station_id):
    station = Station.objects.get(id=station_id)
    type_batiment = TypeBatiment.objects.get(id=bat_id)

    new_bat = Batiment(
        bat=type_batiment,
        station=station,
        timer=type_batiment.timer,
        att_light=type_batiment.att_light,
        att_medium=type_batiment.att_medium,
        att_heavy=type_batiment.att_heavy,
        def_light=type_batiment.def_light,
        def_medium=type_batiment.def_medium,
        def_heavy=type_batiment.def_heavy,
        pv=type_batiment.pv,
        pv_max=type_batiment.pv
    );

    new_bat.save()

    return "new construct up, const_id:"+str(bat_id)+" | station_id:"+str(station_id)



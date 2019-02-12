from django.shortcuts import render, redirect
from .forms import *
from .models import *
from .contexte import *
from .lib import *
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect('accounts/login/')
    else:
        ctx = Contexte(request)
        ctx['page'] = "recap"

        return render(request, 'index.html', context=ctx)


def construction(request):
    if not request.user.is_authenticated:
        return redirect('accounts/login/')
    else:
        ctx = Contexte(request)
        ctx['page'] = "construction"

        # on regarde si on a lance une construction
        ctx['construction_up'] = ""

        if 'id' in request.GET:
            ctx['construction_up'] = new_bat(request.GET['id'], ctx['station_actuelle'].id)

            return redirect('/construction')

        bd = []

        station = ctx['station_actuelle']

        if ctx['bat_slot_dispo'] > 0:
            bat_dispos = TypeBatiment.objects.all()

            for bat_dispo in bat_dispos:
                bat_dispo.nom_web = get_trad(ctx['lang'], bat_dispo.nom_web)
                go = 1

                # on verifie mandatory rech
                if bat_dispo.rech_mandatory != "":
                    pass

                # on verifie mandatory bat
                if bat_dispo.bat_mandatory != "":
                    pass

                # on verifie les ressources
                if bat_dispo.cout_res0 > station.res0:
                    go = 0
                if bat_dispo.cout_res1 > station.res1:
                    go = 0
                if bat_dispo.cout_res2 > station.res2:
                    go = 0
                if bat_dispo.cout_res3 > station.res3:
                    go = 0
                if bat_dispo.cout_res4 > station.res4:
                    go = 0
                if bat_dispo.cout_res5 > station.res5:
                    go = 0
                if bat_dispo.cout_res6 > station.res6:
                    go = 0
                if bat_dispo.cout_res7 > station.res7:
                    go = 0

                if go == 1:
                    bd.append(bat_dispo)

        ctx['bat_dispos'] = bd

        return render(request, 'construction.html', context=ctx)


def recherche(request):
    if not request.user.is_authenticated:
        return redirect('accounts/login/')
    else:
        ctx = Contexte(request)
        ctx['page'] = "recherche"

        return render(request, 'recherche.html', context=ctx)


def navire(request):
    if not request.user.is_authenticated:
        return redirect('accounts/login/')
    else:
        ctx = Contexte(request)
        ctx['page'] = "navire"

        return render(request, 'navire.html', context=ctx)


def flotte(request):
    if not request.user.is_authenticated:
        return redirect('accounts/login/')
    else:
        ctx = Contexte(request)
        ctx['page'] = "flotte"

        return render(request, 'flotte.html', context=ctx)


def commerce(request):
    if not request.user.is_authenticated:
        return redirect('accounts/login/')
    else:
        ctx = Contexte(request)
        ctx['page'] = "commerce"

        return render(request, 'commerce.html', context=ctx)


def new_account(request):
    existe_deja = ""

    if request.method == 'GET':
        form = NewPlayerForm()
    else:
        data = request.POST

        new_identifiant = data['identifiant']
        new_password = data['password']
        new_classe = data['classe']
        new_serveur = data['serveur']

        form = NewPlayerForm(data)

        # on test le nickname pour voir si le joueur existe deja en BD
        if User.objects.filter(username=new_identifiant).exists():
            existe_deja = "This nickname already exist !"
        else:
            # on crée le nouveau joueur
            new_user = User.objects.create_user(new_identifiant, "", new_password)
            existe_deja = "user created id "+str(new_user.id)

            # on créé l'enregistrement dans la table Players
            new_player = Player(
                joueur=new_user,
                classe=Classe.objects.get(id=new_classe),
                serveur=Serveur.objects.get(id=new_serveur)
            )
            new_player.save()

            #on construit sa station principale


            return redirect('/accounts/login/?new='+str(new_user.id))

    ctx = {
        'form': form,
        'existe_deja': existe_deja
    }

    return render(request, 'new_account.html', context=ctx)

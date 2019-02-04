from django.shortcuts import render, redirect
from game.forms import *
from game.models import Classe, Player, Serveur
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect('accounts/login/')
    else:
        ctx = {}
        return render(request, 'index.html', context=ctx)


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

            return redirect('/accounts/login/?new='+str(new_user.id))

    ctx = {
        'form': form,
        'existe_deja': existe_deja
    }

    return render(request, 'new_account.html', context=ctx)

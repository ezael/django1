from django.shortcuts import render, redirect
from game.forms import *
from game.models import Classe
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect('accounts/login/')
    else:
        contexte = {
        }
        return render(request, 'index.html', context=contexte)


def new_account(request):
    existe_deja = ""

    if request.method == 'GET':
        form = NewPlayerForm()
    else:
        form = NewPlayerForm(request.POST)

        new_identifiant = request.POST['identifiant']
        new_password = request.POST['password']
        new_classe = request.POST['classe']

        u, created = User.objects.get_or_create(username=new_identifiant, password=new_password)
        if created:
            existe_deja = "user created"
        else:
            existe_deja = "This nickname already exist !"

    classes = Classe.objects.all()

    contexte = {
        'form': form,
        'existe_deja': existe_deja
    }

    return render(request, 'new_account.html', context=contexte)

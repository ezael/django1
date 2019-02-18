from django.forms import Form, CharField, PasswordInput, ModelChoiceField
from .models import Classe, Serveur

class NewPlayerForm(Form):
    e = Classe.objects.all()
    s = Serveur.objects.all()

    identifiant = CharField(max_length=16)
    password = CharField(widget=PasswordInput(), max_length=16)
    classe = ModelChoiceField(queryset=e)
    serveur = ModelChoiceField(queryset=s)

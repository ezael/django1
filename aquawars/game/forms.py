from django.forms import Form, CharField, PasswordInput, ModelChoiceField
from game.models import Classe

class NewPlayerForm(Form):
    e = Classe.objects.all()

    identifiant = CharField(max_length=16)
    password = CharField(widget=PasswordInput(), max_length=16)
    classe = ModelChoiceField(queryset=e)

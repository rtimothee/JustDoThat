from django import forms
from JustDoThat.apps.defi.models import Categorie

class Rechercheform(forms.Form):
    demande = forms.CharField(max_length=500, label="Recherche", required=False)
    difficulte = forms.ChoiceField(
        choices = ((u"", u"--"), (u"1", u"1"), (u"2", u"2"), (u"3", u"3"), (u"4", u"4"), (u"5", u"5")), required=False
    )
    categorie = forms.ModelChoiceField(queryset=Categorie.objects.all(), required=False)
    fin = forms.DateField(required=False)

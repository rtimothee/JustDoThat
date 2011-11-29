from django import forms

class Rechercheform(forms.Form):
    demande = forms.CharField(max_length=500, label="")
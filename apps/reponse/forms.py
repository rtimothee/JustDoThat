from django import forms
from django.forms import ModelForm, widgets
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User

from JustDoThat.apps.reponse.models import Reponse
from datetime import date


class ReponseForm(ModelForm):
    class Meta:
        model = Reponse
        exclude = ('slug','date_reponse','utilisateur','defi', 'notification')
        
    #surcharge du constructeur pour changer l'affichage de la date de naissance
    def __init__(self, *args, **kwargs):
        super(ReponseForm, self).__init__(*args, **kwargs)
        #set the list of years used in the form, we assume that users are at least 15 years old 
   


        
    
#    def save(self, commit=True):
#        user = super(RegisterForm, self).save(commit=False)
#        first_name, last_name = self.cleaned_data["fullname"].split()
#        user.first_name = first_name
#        user.last_name = last_name
#        user.email = self.cleaned_data["email"]
#        if commit:
#            user.save()
#        return user


from django import forms
from django.forms import ModelForm, widgets
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from JustDoThat.apps.utilisateur.models import Utilisateur
from JustDoThat.apps.utilisateur.models import MessagePrive
from datetime import date

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', )

class EditUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', )
    
    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['username'].widget.attrs['readonly'] = True
    
    def clean_username(self):
        return self.instance.username

class UtilisateurForm(ModelForm):
    class Meta:
        model = Utilisateur
        exclude = ('user', 'points',)
        
    #surcharge du constructeur pour changer l'affichage de la date de naissance
    def __init__(self, *args, **kwargs):
        super(UtilisateurForm, self).__init__(*args, **kwargs)
        #set the list of years used in the form, we assume that users are at least 15 years old
        this_year = date.today().year
        years = range(this_year-100, this_year-15)
        years.reverse()
        self.fields['dateNaissance'].widget = SelectDateWidget(years=years)


        
    
#    def save(self, commit=True):
#        user = super(RegisterForm, self).save(commit=False)
#        first_name, last_name = self.cleaned_data["fullname"].split()
#        user.first_name = first_name
#        user.last_name = last_name
#        user.email = self.cleaned_data["email"]
#        if commit:
#            user.save()
#        return user

class MessageForm(ModelForm):
    class Meta:
        model = MessagePrive
        exclude = ('dateMessage', 'lu', 'emeteur', 'destinataire',)
		
	def __init__(self,pseudo, *args, **kwargs):
		super(MessageForm, self).__init__(*args, **kwargs)
		self.fields['destinataire'] = CharField(max_length=45, null=False)

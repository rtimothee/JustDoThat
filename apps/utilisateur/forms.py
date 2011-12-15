from django import forms
from django.forms import ModelForm, widgets
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from JustDoThat.apps.utilisateur.models import Utilisateur
from JustDoThat.apps.utilisateur.models import MessagePrive
from datetime import date

class UserForm(UserCreationForm):
    
    #le champs email est obligatoire
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', )
        
    #surcharge du constructeur 
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        #affiche le help_text dans l'attribut title du champ
        self.fields['username'].widget.attrs['title'] = self.fields['username'].help_text
        #affiche le help_text dans l'attribut title du champ
        self.fields['password2'].widget.attrs['title'] = self.fields['password2'].help_text

class EditUserForm(UserCreationForm):
    
    #le champs email est obligatoire
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', )
    
    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        
        #affiche le help_text dans l'attribut title du champ
        self.fields['password2'].widget.attrs['title'] = self.fields['password2'].help_text
        #empeche l'edition du username
        if instance and instance.id:
            self.fields['username'].widget.attrs['readonly'] = True
            
    #renvoie la valeur de depart pour s'assurer que la valeur n'a pas ete change (securite)
    def clean_username(self):
        return self.instance.username

class UtilisateurForm(ModelForm):
    
    #personnalisation de certains champs
    GENDER_CHOICES = ((True, 'Male'), (False, 'Female'), )
    dateNaissance = forms.DateField(label='Date of birth')
    pays = forms.CharField(label='Country', max_length=45, required=True)
    sexeM = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, required=True)
    
    class Meta:
        model = Utilisateur
        exclude = ('user', 'points',)
        
    #surcharge du constructeur pour changer l'affichage de la date de naissance
    def __init__(self, *args, **kwargs):
        super(UtilisateurForm, self).__init__(*args, **kwargs)
        #reglage des annees a afficher, on estime que l'utilisateur a au moins 15 ans
        this_year = date.today().year
        years = range(this_year-100, this_year-15)
        years.reverse()
        self.fields['dateNaissance'].widget = SelectDateWidget(years=years)



class MessageForm(ModelForm):
    class Meta:
        model = MessagePrive
        exclude = ('dateMessage', 'lu', 'emeteur', 'destinataire',)
		
	def __init__(self,pseudo, *args, **kwargs):
		super(MessageForm, self).__init__(*args, **kwargs)

		self.fields['destinataire'] = CharField(max_length=45, null=False)

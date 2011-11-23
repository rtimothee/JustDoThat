# Create your views here.
from JustDoThat.apps.utilisateur.models import *
from JustDoThat.apps.defi.models import *
from JustDoThat.apps.main.forms import *
from django.contrib.auth.models import User

from datetime import *
from django.shortcuts import render_to_response

def recherche (request):
    if request.method == 'POST':
            form = Rechercheform(request.POST)
            if form.is_valid():
                requete = form.cleaned_data['demande']
                #requetes
                utilisateurs = User.objects.filter(username__contains=requete)
                defis = Defi.objects.filter(titre__contains=requete).filter(description__contains=requete) #AJOUTER LA VERIFICATION DU USER
                #rediriger vers la page de resultats
                return render_to_response('main/resultats.html', {'defis':defis, 'utilisateurs':utilisateurs})
    else:
        form = Rechercheform()
        
    return render_to_response('main/recherche.html', {'form':form})# Create your views here.

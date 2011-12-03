# Create your views here.
from JustDoThat.apps.utilisateur.models import *
from JustDoThat.apps.defi.models import *
from JustDoThat.apps.main.forms import *
from django.contrib.auth.models import User
from django.db.models import Q


from datetime import *
from django.shortcuts import render_to_response

def recherche (request):
    if request.method == 'GET':
            form = Rechercheform(request.GET)
            if form.is_valid():
                requete = form.cleaned_data['demande']
                #requetes
                utilisateurs = User.objects.filter(username__icontains=requete)
                defis = Defi.objects.filter(Q(titre__icontains=requete) | Q(description__icontains=requete) | Q(createur__in = utilisateurs))
                #rediriger vers la page de resultats
                return render_to_response('main/resultats.html', {'defis':defis, 'utilisateurs':utilisateurs})
    else:
        form = Rechercheform()
        
    return render_to_response('main/recherche.html', {'form':form}, context_instance=RequestContext(request))# Create your views here.


# Create your views here.
from JustDoThat.apps.utilisateur.models import *
from JustDoThat.apps.defi.models import *
from JustDoThat.apps.main.forms import *
from django.contrib.auth.models import User
from django.db.models import Q
from django.template import RequestContext
from datetime import datetime

from datetime import *
from django.shortcuts import render_to_response


def recherche (request):
    if request.method == 'GET':
            form = Rechercheform(request.GET)
            if form.is_valid():
                requete = form.cleaned_data['demande']
                #requetes
                utilisateurs = User.objects.filter(username__icontains=requete)
                myquery = {}
                if form.cleaned_data['difficulte']:
                    myquery['difficulte'] = form.cleaned_data['difficulte']
                    #defis = defis.filter(difficulte = form.cleaned_data['difficulte'])
                if form.cleaned_data['categorie']:
                    myquery['categorie'] = form.cleaned_data['categorie']
                    #defis = defis.filter(categorie__nom = form.cleaned_data['categorie'])
                if form.cleaned_data['fin']:
                    myquery['fin__lte'] = form.cleaned_data['fin']
                    myquery['fin__gte'] = datetime.now
                    #defis = defis.filter(fin = form.cleaned_data['fin'])
                defis = Defi.objects.filter(Q(titre__icontains=requete) | Q(description__icontains=requete) | Q(createur__in = utilisateurs)).filter(**myquery)
                #rediriger vers la page de resultats
                return render_to_response('main/recherche.html', {'defis':defis, 'utilisateurs':utilisateurs, 'form':form}, context_instance=RequestContext(request))
    else:
        form = Rechercheform()
        
    return render_to_response('main/recherche.html', {'form':form}, context_instance=RequestContext(request))# Create your views here.

def recherche_av (request):
    '''TO DO !! 
    Champs texte
    Difficulte
    categorie
    duree avant la fin
    '''
    return render_to_response('main/recherche.html', context_instance=RequestContext(request))# Create your views here.


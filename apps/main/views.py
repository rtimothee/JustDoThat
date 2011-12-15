# Create your views here.
from JustDoThat.apps.utilisateur.models import *
from JustDoThat.apps.defi.models import *
from JustDoThat.apps.main.forms import *
from django.contrib.auth.models import User
from django.db.models import Q
from django.template import RequestContext
from datetime import *
from operator import itemgetter, attrgetter
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def compfreq(elem1,elem2):
    if elem1[1]<elem2[1]:
        return -1
    if elem1[1]>elem2[1]:
        return 1
    return 0

def index (request):

	# les 8 meilleurs challengers avec le plus de points
	best_challengers = Utilisateur.objects.all().order_by("-points")
	best_challengers[0:8]
	
	# les 4 derniers challenges crees
	latest = Defi.objects.all().order_by("-id")
	latest[0:4]

	# les 4 challenges non finis ayant le plus de releves
	challenges = Defi.objects.all()
	releves = []
	best_challenges = []
	challenges_not_over = []
	for c in challenges:
		if c.timeleft != 'Challenge over' :
			challenges_not_over.append(c);
			releves.append(c.nbreleve)
	best_challenges = sorted(zip(challenges_not_over, releves))
	best_challenges.sort(lambda x,y: cmp(x[1],y[1]), reverse=True)



 
	best_challenges.sort(compfreq, reverse=True)
	best_challenges[0:4]

	return render_to_response('main/index.html', {'best_challengers': best_challengers, 'best_challenges':best_challenges, 'latest':latest}, context_instance=RequestContext(request))# Create your views here.

def recherche (request):
    if request.method == 'GET':
            form = Rechercheform(request.GET)
            if form.is_valid():
                requete = form.cleaned_data['demande']
        #---------------- requetes Utilisateur ------------------
                #requete
                utilisateurs = User.objects.filter(username__icontains=requete)
                
                #recuperation des conditions de tri
                triUser = request.GET.get('triUser')
                if triUser :
                    if triUser == 'Ncr' : utilisateurs = utilisateurs.order_by('username')
                    elif triUser == 'Ndecr' : utilisateurs = utilisateurs.order_by('-username')
                
                #Recuperation du numero de la page 
                utilisateursP = Paginator(utilisateurs, 12)
                try: pageU = int(request.GET.get('pageU', '1'))
                except ValueError : pageU = 1
                
                #pagination
                try: pageUser = utilisateursP.page(pageU)
                except PageNotAnInteger: pageUser = utilisateursP.page(1)
                except EmptyPage: pageUser = utilisateursP.page(utilisateursP.num_pages)

        #---------------- requetes Defi ------------------
                #requete
                myquery = {}
                if form.cleaned_data['difficulte']:
                    myquery['difficulte'] = form.cleaned_data['difficulte']
                if form.cleaned_data['categorie']:
                    myquery['categorie'] = form.cleaned_data['categorie']
                if form.cleaned_data['fin']:
                    myquery['fin__lte'] = form.cleaned_data['fin']
                    myquery['fin__gte'] = datetime.now
                defis = Defi.objects.filter(Q(titre__icontains=requete) | Q(description__icontains=requete) | Q(createur__in = utilisateurs)).filter(**myquery)
                
                #recuperation des conditions de tri
                triDefi = request.GET.get('triDefi')
                if triDefi :
                    if triDefi == 'Ncr' : defis = defis.order_by('titre')
                    elif triDefi == 'Ndecr' : defis = defis.order_by('-titre')
                    elif triDefi == 'Dcr' : defis = defis.order_by('fin')
                    elif triDefi == 'Ddecr' : defis = defis.order_by('-fin')
                    
                #Recuperation du numero de la page 
                defisP = Paginator(defis, 12)
                try: pageD = int(request.GET.get('pageD', '1'))
                except ValueError : pageD = 1
                
                #pagination
                try: pageDefis = defisP.page(pageD)
                except PageNotAnInteger: pageDefis = defisP.page(1)
                except EmptyPage: pageDefis = utilisateursP.page(defisP.num_pages)
               
                
                #rediriger vers la page de resultats
                return render_to_response('main/recherche.html', {'defis':pageDefis, 'utilisateurs':pageUser, 'form':form}, context_instance=RequestContext(request))
            
    else:
        form = Rechercheform()
        
    return render_to_response('main/recherche.html', {'form':form}, context_instance=RequestContext(request))# Create your views here.



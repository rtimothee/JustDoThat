# -*- coding: utf-8 -*-
# Create your views here.
from JustDoThat.apps.defi.models import *
from JustDoThat.apps.defi.forms import *
from JustDoThat.apps.reponse.models import *
from JustDoThat.apps.reponse.forms import *
from django.template.defaultfilters import slugify
from JustDoThat.apps.utilisateur.models import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.contrib.auth.views import login, logout
from django.shortcuts import render_to_response
from JustDoThat.apps.defi.tools import handle_uploaded_file
from datetime import date
from django.template import RequestContext
from compiler.pycodegen import EXCEPT
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def challenges_view(request):
	defis = Defi.objects.all()
	
	#tri
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
	return render_to_response('defi/challenges.html', {'defis':pageDefis}, context_instance=RequestContext(request))



'''def challenges_view(request):
	defis = Defi.objects.all()
			
	return render_to_response('defi/challenges.html', {'defis': defis}, context_instance=RequestContext(request))'''
	
def modif_challenge_view(request, int):
	if request.user.is_authenticated():
		try: defi = Defi.objects.get(id=int)
		except Defi.DoesNotExist:
			return HttpResponseRedirect("/")
		if request.method == 'POST':   
			defi_form = DefiForm(request.POST, instance = defi)  
			if defi_form.is_valid(): 
				defi_form.save()
				return HttpResponseRedirect('/challenges/list_challenges/') 

		else:
			if defi.createur == request.user :
				defi_form = DefiForm(instance = defi) 
			else :
				return HttpResponseRedirect('/') 
	else:
		return HttpResponseRedirect('/')
	# on renvoie le booleen pour specifier de modifer certains elements du formulaires
	modif = True
	return render_to_response('defi/create_challenge.html', {'defi_form': defi_form, 'modif': modif,'defi':int}, context_instance=RequestContext(request))
  


  
def delete_challenge_view(request, int, delete):
	# verification de connexion du user
	if request.user.is_authenticated():
		try: defi = Defi.objects.get(id=int)
		except Defi.DoesNotExist:
			return HttpResponseRedirect("/")
		if delete=='sup':
			if defi.createur == request.user :
				defi.delete()
				return HttpResponseRedirect('/challenges/list_challenges/') 
			else :
				return HttpResponseRedirect('/') 
	else:
		return HttpResponseRedirect('/') 

	return render_to_response('defi/delete_challenge.html', {'defi':int}, context_instance=RequestContext(request)) 

def create_challenge_view(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			#recuperation des informations du formulaire
			defi_form = DefiForm(request.POST, request.FILES)
			
			#si les infos sont valides
			if defi_form.is_valid() :
				  #fonction gerant l'upload de la photo du d�fi
						#creation du nouveau defi
						new_defi = Defi(**defi_form.cleaned_data)
						new_defi.slug = slugify(new_defi.titre)
						#creation du nouveau defi avec comme createur l'utilisateur connecte
						new_defi.createur = request.user
						new_defi.save()
						
						return HttpResponseRedirect("/challenges/list_challenges/")
		else:
			defi_form = DefiForm()
	else:
		return HttpResponseRedirect('/') 
        
	return render_to_response("defi/create_challenge.html", {'defi_form': defi_form,}, context_instance=RequestContext(request))
   
   
def create_reponse_view(request, int):
    #Fonction de creation de reponse
    #Cette fonction sera accessible par une lightbox
    if request.method == 'POST':
        #recuperation des informations du formulaire
        reponse_form = ReponseForm(request.POST, request.FILES)
        
        #si les infos sont valides
        if reponse_form.is_valid() :
             		#Creation d'un table relever correspondant au defi a l'utilisateur
					new_releve = Relever()
					new_releve.utilisateur = request.user
					new_releve.defi = Defi.objects.get(id = int)
                    #sauvegarde de cette table
					new_releve.save()
					new_reponse = Reponse(**reponse_form.cleaned_data)
					#creation du nouveau defi avec comme cr�ateur l'utilisateur connecte
					new_reponse.utilisateur_id = request.user.id
					new_reponse.defi_id = int
			        #sauvegarde de la reponse créée
					new_reponse.save()
					#redirection vers la page d'affichage du challenge correspondant
					return HttpResponseRedirect('/challenges/display_challenge/'+int+'/')
    else:
        reponse_form = ReponseForm()
        
    return render_to_response("defi/create_reponse.html", {'reponse_form': reponse_form,}, context_instance=RequestContext(request))   


def delete_reponse_view(request, int):
	reponse = Reponse.objects.get(id=int)
	reponse.delete()
	return HttpResponseRedirect('/challenges/display_challenge/'+int+'/')

def modif_reponse_view(request, int, intDefi):
	#la modification de la reponse se fait aussi dans une lightbox
    #elle dispose de integer das son URL
	reponse  = Reponse.objects.get(id=int)
	defi = reponse.defi
	if request.method == 'POST':   
		reponse_form = ReponseForm(request.POST, instance = reponse)  
		if reponse_form.is_valid(): 
			reponse_form.save()
			return HttpResponseRedirect('/challenges/display_challenge/'+intDefi+'/') 

	else:
        #on rempli le formlaire
		if reponse.utilisateur == request.user :
			reponse_form = ReponseForm(instance = reponse) 
		else :
			return HttpResponseRedirect('/challenges/display_challenge/'+intDefi+'/') 
	
	modif = True
	return render_to_response('defi/create_reponse.html', {'reponse_form': reponse_form, 'modif': modif,'reponse':int}, context_instance=RequestContext(request))

def display_challenge_view(request, int):
	try: defi = Defi.objects.get(id=int)
	except Defi.DoesNotExist:
		return HttpResponseRedirect("/")
	releves = Relever.objects.filter(defi = defi.id)
	users = []
	createur =0
	if defi.createur == request.user :
		createur=1
	# recuperation des users qui ont releve le defi
	for r in releves :
			user = User.objects.get(id = r.utilisateur.id)
			if user not in users:
				users.append(user)

	# on verifie si le defi est fini et on envoi un booleen pour restreindre l access aux users
	time_left = defi.fin - defi.debut

	if defi.fin > date.today() :
		end = 0
	else:
		end = 1

	# on recupere la categorie
	category = Categorie.objects.get(id=defi.categorie_id)

	# on specifie les niveaux de difficulte
	if defi.difficulte == 1:
		difficulte = 'Easy'
	if defi.difficulte == 2:
		difficulte = 'Normal'
	if defi.difficulte == 3:
		difficulte = 'Hard'
	if defi.difficulte == 4:
		difficulte = 'Very Hard'
		
	# reponses du defi
	reponses = Reponse.objects.filter(defi=defi.id)
	# defis de meme categorie
	listeD = Defi.objects.filter(categorie = defi.categorie).order_by('-fin')
	
	
	if request.method == 'POST':
        #autre formualaire de creation de reponse present ici pour le fonctionement de la lightbox
		Reponse_form = ReponseForm(request.POST, request.FILES)
		
		#si les infos sont valides
		if Reponse_form.is_valid():
			new_releve = Relever()
			new_releve.utilisateur = request.user
			new_releve.defi = Defi.objects.get(id = int)
			new_releve.save()
			new_reponse = Reponse(**Reponse_form.cleaned_data)
			new_reponse.utilisateur_id = request.user.id
			new_reponse.defi_id = int
			new_reponse.save()
			return HttpResponseRedirect("/challenges/display_challenge/"+int+"/")
	else:
		 Reponse_form = ReponseForm()
	

	return render_to_response("defi/display_challenge.html", {'Reponse_form': Reponse_form,'reponses': reponses,'defiList':listeD[0:4], 'defi': defi, 'difficulty': difficulte, 'category':category.nom, 'users':users, 'createur':createur,'end':end}, context_instance=RequestContext(request))


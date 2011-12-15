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
	defi  = Defi.objects.get(id=int)
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
	
	modif = True
	return render_to_response('defi/create_challenge.html', {'defi_form': defi_form, 'modif': modif,'defi':int}, context_instance=RequestContext(request))
  


  
def delete_challenge_view(request, int, delete):
	defi = Defi.objects.get(id=int)
	if delete=='sup':
		if defi.createur == request.user :
			defi.delete()
			return HttpResponseRedirect('/challenges/list_challenges/') 
		else :
			return HttpResponseRedirect('/') 

	return render_to_response('defi/delete_challenge.html', {'defi':int}, context_instance=RequestContext(request)) 

def create_challenge_view(request):
    if request.method == 'POST':
        #recup�ration des informations du formulaire
        defi_form = DefiForm(request.POST, request.FILES)
        
        #si les infos sont valides
        if defi_form.is_valid() :
              #fonction g�rant l'upload de la photo du d�fi
					handle_uploaded_file(request.FILES['photo'])
					#creation du nouveau d�fi
					new_defi = Defi(**defi_form.cleaned_data)
					new_defi.slug = slugify(new_defi.titre)
					#creation du nouveau d�fi avec comme cr�ateur l'utilisateur connect�
					new_defi.createur = request.user
					new_defi.save()
					
					return HttpResponseRedirect("/challenges/list_challenges/")
    else:
        defi_form = DefiForm()
        
    return render_to_response("defi/create_challenge.html", {'defi_form': defi_form,}, context_instance=RequestContext(request))
   
   
def create_reponse_view(request, int):
	if request.method == 'POST':
		
	
		Reponse_form = ReponseForm(request.POST, request.FILES)
		
		#si les infos sont valides
		if Reponse_form.is_valid():
			handle_uploaded_file(request.FILES['photo'])
			new_reponse = Reponse(**Reponse_form.cleaned_data)
		  #  new_reponse.slug = slugify(new_reponse.titre)
			new_reponse.utilisateur_id = request.user.id
			new_reponse.defi_id = int
			new_reponse.save()
			return HttpResponseRedirect("/challenges/display_challenge/1/")
	else:
		 Reponse_form = ReponseForm()
	
	return render_to_reponse("defi/create_reponse.html", {'Reponse_form': Reponse_form}, context_instance=RequestContext(request))

def delete_reponse_view(request, int):
	reponse = Reponse.objects.get(id=int)
	reponse.delete()
	return HttpResponseRedirect('/challenges/display_challenge/1/')

def modif_reponse_view(request, int):
	reponse  = Reponse.objects.get(id=int)
	if request.method == 'POST':   
		reponse_form = ReponseForm(request.POST, instance = reponse)  
		if reponse_form.is_valid(): 
			reponse_form.save()
			return HttpResponseRedirect('/challenges/display_challenge/1/') 

	else: 
		reponse_form = ReponseForm(instance = reponse) 
	
	modif = True
	return render_to_response('defi/create_reponse.html', {'reponse_form': reponse_form, 'modif': modif}, context_instance=RequestContext(request))


def display_challenge_view(request, int):
	defi = Defi.objects.get(id=int)
		
	releves = Relever.objects.filter(defi = defi.id)
	users = []
	createur =0
	if defi.createur == request.user :
		createur=1
	
	for r in releves :
		users.append(User.objects.get(id = r.utilisateur.id))
			
	
		
	time_left = defi.fin - defi.debut
		
	if defi.fin <= date.today() :
		End = False
	else:
		End = True
			
	
	category = Categorie.objects.get(id=defi.categorie_id)
		
	
	if defi.difficulte == 1:
		difficulte = 'Easy'
	if defi.difficulte == 2:
		difficulte = 'Normal'
	if defi.difficulte == 3:
		difficulte = 'Hard'
	if defi.difficulte == 4:
		difficulte = 'Very Hard'
		
		
	reponses = Reponse.objects.filter(defi=defi.id)
	
	if request.method == 'POST':
		
	
		Reponse_form = ReponseForm(request.POST, request.FILES)
		
		#si les infos sont valides
		if Reponse_form.is_valid():
			handle_uploaded_file(request.FILES['photo'])
			new_reponse = Reponse(**Reponse_form.cleaned_data)
		  #  new_reponse.slug = slugify(new_reponse.titre)
			new_reponse.utilisateur_id = request.user.id
			new_reponse.defi_id = int
			new_reponse.save()
			return HttpResponseRedirect("/challenges/display_challenge/1/")
	else:
		 Reponse_form = ReponseForm()
	 
	
		
	return render_to_response("defi/display_challenge.html", {'Reponse_form': Reponse_form,'reponses': reponses, 'defi': defi, 'difficulty': difficulte, 'category':category.nom, 'users':users, 'createur':createur}, context_instance=RequestContext(request))
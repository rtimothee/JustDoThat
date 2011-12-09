# -*- coding: utf-8 -*-
# Create your views here.
from JustDoThat.apps.defi.models import *
from JustDoThat.apps.defi.forms import *
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

def challenges_view(request):
	defis = Defi.objects.all()
			
	return render_to_response('defi/challenges.html', {'defis': defis}, context_instance=RequestContext(request))
	
def modif_challenge_view(request, int):
	defi  = Defi.objects.get(id=int)
	if request.method == 'POST':   
		defi_form = DefiForm(request.POST, instance = defi)  
		if defi_form.is_valid(): 
			defi_form.save()
			return HttpResponseRedirect('/challenges/list_challenges/') 

	else: 
		defi_form = DefiForm(instance = defi) 
	
	modif = True
	return render_to_response('defi/create_challenge.html', {'defi_form': defi_form, 'modif': modif}, context_instance=RequestContext(request))
  
def display_challenge_view(request, int):
		defi = Defi.objects.get(id=int)
		
		releves = Relever.objects.filter(defi = defi.id)
		users = []
		
		for r in releves :
			users.append(User.objects.get(id = r.utilisateur.id))
			
			
		# on récupère la durée restante du défi
		time_left = defi.fin - defi.debut
		
		# on vérifie si le défi est déjà terminé ou non
		if defi.fin <= date.today() :
			End = False
		else:
			End = True
			
		# on récupère le nom de la catégorie
		category = Categorie.objects.get(id=defi.categorie_id)
		
		# on définit les niveaux de difficulté
		if defi.difficulte == 1:
			difficulte = 'Easy'
		if defi.difficulte == 2:
			difficulte = 'Normal'
		if defi.difficulte == 3:
			difficulte = 'Hard'
		if defi.difficulte == 4:
			difficulte = 'Very Hard'

		return render_to_response('defi/display_challenge.html', {'defi': defi, 'difficulty': difficulte, 'category':category.nom, 'users':users}, context_instance=RequestContext(request))

  
def delete_challenge_view(request, int):
	defi = Defi.objects.get(id=int)
	defi.delete()
	return HttpResponseRedirect('/challenges/')

def create_challenge_view(request):
    if request.method == 'POST':
        #recupération des informations du formulaire
        defi_form = DefiForm(request.POST, request.FILES)
        
        #si les infos sont valides
        if defi_form.is_valid() :
              #fonction gèrant l'upload de la photo du défi
					handle_uploaded_file(request.FILES['photo'])
					#creation du nouveau défi
					new_defi = Defi(**defi_form.cleaned_data)
					new_defi.slug = slugify(new_defi.titre)
					#creation du nouveau défi avec comme créateur l'utilisateur connecté
					new_defi.createur = request.user.id
					new_defi.save()
					
					return HttpResponseRedirect("/challenges/list_challenges/")
    else:
        defi_form = DefiForm()
        
    return render_to_response("defi/create_challenge.html", {'defi_form': defi_form,}, context_instance=RequestContext(request))
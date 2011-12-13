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
		if defi.createur == request.user :
			defi_form = DefiForm(instance = defi) 
		else :
			return HttpResponseRedirect('/') 
	
	modif = True
	return render_to_response('defi/create_challenge.html', {'defi_form': defi_form, 'modif': modif,'defi':int}, context_instance=RequestContext(request))
  
def display_challenge_view(request, int):
		defi = Defi.objects.get(id=int)
		releves = Relever.objects.filter(defi = defi.id)
		createur =0
		users = []

		if defi.createur == request.user :
			createur=1

		for r in releves :
			users.append(User.objects.get(id = r.utilisateur.id))
			
			
		# on r�cup�re la dur�e restante du d�fi
		time_left = defi.fin - defi.debut
		
		# on v�rifie si le d�fi est d�j� termin� ou non
		if defi.fin <= date.today() :
			End = False
		else:
			End = True
			
		# on r�cup�re le nom de la cat�gorie
		category = Categorie.objects.get(id=defi.categorie_id)
		
		# on d�finit les niveaux de difficult�
		if defi.difficulte == 1:
			difficulte = 'Easy'
		if defi.difficulte == 2:
			difficulte = 'Normal'
		if defi.difficulte == 3:
			difficulte = 'Hard'
		if defi.difficulte == 4:
			difficulte = 'Very Hard'

		return render_to_response('defi/display_challenge.html', {'defi': defi, 'difficulty': difficulte, 'category':category.nom, 'users':users, 'createur':createur}, context_instance=RequestContext(request))

  
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
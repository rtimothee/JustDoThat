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

def challenges_view(request):
	defis = Defi.objects.all()
			
	return render_to_response('defi/challenges.html', {'defis': defis}, context_instance=RequestContext(request))
	
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
	modif = True
	return render_to_response('defi/create_challenge.html', {'defi_form': defi_form, 'modif': modif,'defi':int}, context_instance=RequestContext(request))
  


  
def delete_challenge_view(request, int, delete):
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
	else:
		return HttpResponseRedirect('/') 
        
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
			return HttpResponseRedirect("/challenges/display_challenge/"+int+"/")
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
			return HttpResponseRedirect('/challenges/display_challenge/'+int+'/') 

	else: 
		reponse_form = ReponseForm(instance = reponse) 
	
	modif = True
	return render_to_response('defi/create_reponse.html', {'reponse_form': reponse_form, 'modif': modif}, context_instance=RequestContext(request))


def display_challenge_view(request, int):
	try: defi = Defi.objects.get(id=int)
	except Defi.DoesNotExist:
		return HttpResponseRedirect("/")
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
			return HttpResponseRedirect("/challenges/display_challenge/"+int+"/")
	else:
		 Reponse_form = ReponseForm()
	 
	
		
	return render_to_response("defi/display_challenge.html", {'Reponse_form': Reponse_form,'reponses': reponses, 'defi': defi, 'difficulty': difficulte, 'category':category.nom, 'users':users, 'createur':createur}, context_instance=RequestContext(request))
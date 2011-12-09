# -*- coding: utf-8 -*-
# Create your views here.
from JustDoThat.apps.utilisateur.models import *
from JustDoThat.apps.defi.models import *
from JustDoThat.apps.reponse.models import *
from JustDoThat.apps.utilisateur.forms import *
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.contrib.auth.views import login, logout
from django.shortcuts import render_to_response
from JustDoThat.apps.utilisateur.tools import handle_uploaded_file
from django.db.models import Count



def login_view(request):

  if request.method == 'POST':
    user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
      if user.is_active:
        login(request, user)
        # success
        if request.POST['next']:
          return HttpResponseRedirect(request.POST['next'])
        else:
          return HttpResponseRedirect('/')
      else:
        # disabled account
        return render_to_response('utilisateur/login.html', {'next':'./', 'erreur' : 'compte désactivé.', 'user':request.user})
    
    else:
      # invalid login
      return render_to_response('utilisateur/login.html', {'next':'./', 'erreur' : 'Login ou mot de passe invalide.', 'user':request.user})

  else:
      return render_to_response('utilisateur/login.html', {'next':'./', 'user':request.user})
  
def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/')

def register_view(request):
    if request.method == 'POST':
        #recupération des informations du formulaire
        user_form = UserForm(request.POST)
        utilisateur_form = UtilisateurForm(request.POST, request.FILES)
        
        #si les infos sont valides
        if user_form.is_valid() and utilisateur_form.is_valid():
                #fonction gèrant l'upload de l'avatar
                handle_uploaded_file(request.FILES['avatar'])
                #creation du nouvel utilisateur
                new_user = Utilisateur(**utilisateur_form.cleaned_data)
                new_user.user = user_form.save()
                new_user.save()
                
                return HttpResponseRedirect("/")
    else:
        #creation des formulaires
        user_form = UserForm()
        utilisateur_form = UtilisateurForm()
        
    return render_to_response("utilisateur/register.html", {'user_form': user_form, 'utilisateur_form': utilisateur_form,})

def send_message_view(request, pseudo):
	if request.method == 'POST':
        #recupération des informations du formulaire
		message_form = MessageForm(request.POST)
        
        #si les infos sont valides
		if message_form.is_valid() :
					#creation du nouveau message
					new_message = MessagePrive(**message_form.cleaned_data)
					#creation du nouveau message avec comme créateur l'utilisateur connecté
					new_message.emeteur = request.user
					destinataire = User.objects.get(username = pseudo)
					new_message.save()
					
					return HttpResponseRedirect("/user/inbox/")
	else:
		message_form = MessageForm()
		message_form.destinataire = User.objects.get(username = pseudo)
        
	return render_to_response("utilisateur/send_message.html", {'message_form': message_form,})

def inbox_view(request):

	messages = MessagePrive.objects.filter(destinataire = request.user).order_by("-id")

	nb = MessagePrive.objects.filter(destinataire = request.user).count()
	users = []
	messages1 = User.objects.none()
	if nb > 1 :
		for m in messages :
			user = User.objects.get(id= m.emeteur.id)
			if user.username in users:
				if not messages1:
					messages1 = messages.exclude(emeteur=user.id)
				else:
					messages1 += messages.exclude(emeteur=user.id)
			else:
				users.append(user.username)
	return render_to_response("utilisateur/inbox.html", {'messages': messages1,})

def conversation_view(request, pseudo):
	if request.method == 'POST':
        #recupération des informations du formulaire
		message_form = MessageForm(request.POST)
        
        #si les infos sont valides
		if message_form.is_valid() :
					#creation du nouveau message
					new_message = MessagePrive(**message_form.cleaned_data)
					#creation du nouveau message avec comme créateur l'utilisateur connecté
					new_message.emeteur = request.user
					new_message.destinataire = User.objects.get(username = pseudo)
					new_message.save()
					
					return HttpResponseRedirect("/user/conversation/"+pseudo)
	else:
		message_form = MessageForm()
		message_form.destinataire = User.objects.get(username = pseudo)
		
		messages1 = MessagePrive.objects.filter(destinataire = request.user, emeteur=User.objects.get(username = pseudo)).order_by("id")
		messages2 = MessagePrive.objects.filter(emeteur = request.user, destinataire=User.objects.get(username = pseudo)).order_by("id")
		messages = messages1 | messages2
        
	return render_to_response("utilisateur/conversation.html", {'messages': messages, 'message_form': message_form,})

#----------------------- SUPPRESSION COMPTE --------------------
def delete_account (request, pseudo):
    user = User.objects.get(username=pseudo)
    if request.method == 'GET' :
        if request.GET['confirm'] == 'True':
            #MAJ des défis
            try : defi = Defi.objects.filter(createur=user).update(createur=User.objects.get(username='Anonymous'))
            except Defi.DoesNotExist : pass
            #suppression de l'utilisateur en Cascade
            user.delete()
            
            #redirection vers l'accueil
            return HttpResponseRedirect('/')
        
        
    return render_to_response('utilisateur/delete_account.html', {'user':user})
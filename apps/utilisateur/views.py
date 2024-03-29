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
from django.template import RequestContext
from compiler.pycodegen import EXCEPT
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#------------------------LOGIN---------------------------------------------------------------------
def login_view(request):

  if request.method == 'POST':
    user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
      if user.is_active:
        login(request, user)
        # success
        return HttpResponseRedirect(request.POST['next'])
      else:
        # disabled account
        return render_to_response('utilisateur/errorLog.html', {'erreur' : 'compte désactivé.', 'user':request.user, 'next':request.POST['next']},context_instance=RequestContext(request))
    
    else:
      # invalid login
      return render_to_response('utilisateur/errorLog.html', {'erreur' : 'Login ou mot de passe invalide.', 'user':request.user, 'next':request.POST['next']},context_instance=RequestContext(request))
  else:
      # return HttpResponseRedirect('/')
      return render_to_response('utilisateur/errorLog.html',context_instance=RequestContext(request))
  
def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/')

#-----------------------------------INSCRIPTION--------------------------------------------
def register_view(request):
    if request.method == 'POST':
        #recupération des informations du formulaire
        user_form = UserForm(request.POST)
        utilisateur_form = UtilisateurForm(request.POST, request.FILES)
        
        #si les infos sont valides
        if user_form.is_valid() and utilisateur_form.is_valid():
            #creation du nouvel utilisateur
            new_user = Utilisateur(**utilisateur_form.cleaned_data)
            new_user.points = 0
            new_user.user = user_form.save()
            new_user.save()
            
            return HttpResponseRedirect("/")
    else:
        #creation des formulaires
        user_form = UserForm()
        utilisateur_form = UtilisateurForm()
        
    return render_to_response("utilisateur/register.html", {'user_form': user_form, 'utilisateur_form': utilisateur_form,}, context_instance=RequestContext(request))

#------------------------ENVOI DE MESSAGE---------------------------------------------------------------------
def send_message_view(request, pseudo):
	if request.user.is_authenticated(): 
	 # On verifie si le user existe
		try: user = User.objects.get(username = pseudo)
		except User.DoesNotExist:
			return HttpResponseRedirect("/")
		if pseudo == user.username:
			if request.method == 'POST':
				#recuperation des informations du formulaire
				message_form = MessageForm(request.POST)
				
				#si les infos sont valides
				if message_form.is_valid() :
							#creation du nouveau message
							new_message = MessagePrive(**message_form.cleaned_data)
							#creation du nouveau message avec comme createur l utilisateur connecté
							new_message.emeteur = request.user
							new_message.destinataire = User.objects.get(username = pseudo)
							new_message.save()
							
							HttpResponseRedirect("/user/profile/"+pseudo+"/")
			else:
				message_form = MessageForm()
				message_form.destinataire = User.objects.get(username = pseudo)
		else:
			return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/")
        
	return render_to_response("utilisateur/send_message.html", {'message_form': message_form,}, context_instance=RequestContext(request))

#------------------------BOITE DE RECEPTION---------------------------------------------------------------------
def inbox_view(request):
	if request.user.is_authenticated(): 
		messages = MessagePrive.objects.filter(destinataire = request.user).order_by("-id")
		notif = 0
		
		# on recupere l\'ensemble des messages recus par un user
		nb = MessagePrive.objects.filter(destinataire = request.user).count()
		
		# si il y ny en a aucun il aura un message le lui disant
		if nb ==0:
			notif = 1
		
		# on recupere lensemble des users ayant envoye un message au courant ainsi que leur dernier message emis
		users = []
		last_messages = []
		if nb > 1 :
			for m in messages :
				user = User.objects.get(id= m.emeteur.id)
				if user not in users:
					last_messages.append(MessagePrive.objects.filter(emeteur = m.emeteur.id).order_by("-id")[0])
					users.append(user)
		else:
			last_messages = messages
			
		#Recuperation du numero de la page 
		messagesP = Paginator(last_messages, 10)
		try: pageM = int(request.GET.get('pageM', '1'))
		except ValueError : pageM = 1
					
		#pagination
		try: pageMessage = messagesP.page(pageM)
		except PageNotAnInteger: pageMessage = messagesP.page(1)
		except EmptyPage: pageMessage = messagesP.page(messagesP.num_pages)
	else:
		return HttpResponseRedirect('/')
	return render_to_response("utilisateur/inbox.html", {'last_messages': pageMessage, 'notif':notif,},context_instance=RequestContext(request))

#------------------------CONVERSATION---------------------------------------------------------------------
def conversation_view(request, pseudo):

	if request.user.is_authenticated(): 
	 # On verifie si le user existe
		try: user = User.objects.get(username = pseudo)
		except User.DoesNotExist:
			return HttpResponseRedirect("/")
		if pseudo == user.username:
			
			if request.method == 'POST':
				#recuperation des informations du formulaire
				message_form = MessageForm(request.POST)
				
				#si les infos sont valides
				if message_form.is_valid() :
							#creation du nouveau message
							new_message = MessagePrive(**message_form.cleaned_data)
							#creation du nouveau message avec comme createur l utilisateur connecté
							new_message.emeteur = request.user
							new_message.destinataire = User.objects.get(username = pseudo)
							new_message.save()
							
							return HttpResponseRedirect("/user/conversation/"+pseudo)
			else:
				message_form = MessageForm()
				message_form.destinataire = User.objects.get(username = pseudo)
				# on assemble les deux listes de messages
				messages1 = MessagePrive.objects.filter(destinataire = request.user, emeteur=User.objects.get(username = pseudo)).order_by("id")
				messages2 = MessagePrive.objects.filter(emeteur = request.user, destinataire=User.objects.get(username = pseudo)).order_by("id")
				messages = messages1 | messages2
				
				# on met a jour le statut lu du message
				for m in messages:
					if m.lu == 0 :
						if m.destinataire == request.user :
							m.lu=1
							m.save()
				
				#Recuperation du numero de la page 
				messagesP = Paginator(messages, 10)
				try: pageM = int(request.GET.get('pageM', '1'))
				except ValueError : pageM = 1
						
				#pagination
				try: pageMessage = messagesP.page(pageM)
				except PageNotAnInteger: pageMessage = messagesP.page(1)
				except EmptyPage: pageMessage = messagesP.page(messagesP.num_pages)
		else:
			return HttpResponseRedirect("/user/inbox/")
	else : 
		return HttpResponseRedirect("/")
	return render_to_response("utilisateur/conversation.html", {'messages': pageMessage, 'message_form': message_form,}, context_instance=RequestContext(request))

#----------------------- SUPPRESSION COMPTE --------------------
def delete_account (request):
    if request.user.is_authenticated(): 
        user = request.user
        if request.GET.get('confirm'):
            if request.GET['confirm'] == 'True':
                #MAJ des défis
                defi = Defi.objects.filter(createur=user)
                if defi.count() > 0 : defi.update(createur=User.objects.get(username='Anonymous'))
                #suppression de l utilisateur en Cascade
                user.delete()
            
                #redirection vers l'accueil
                return HttpResponseRedirect('/')
            else : return render_to_response('utilisateur/delete_account.html', {'user':user}, context_instance=RequestContext(request))
        else : return render_to_response('utilisateur/delete_account.html', {'user':user}, context_instance=RequestContext(request))
        
    else :
        return render_to_response('utilisateur/error.html', {'user':user, 'error':'Access denied'}, context_instance=RequestContext(request))

#-----------------------AFFICHAGE PROFIL------------------------------------
def display_profile(request, pseudo):
    
    # On recupere le user du profil a afficher
    try: user_to_display = User.objects.get(username=pseudo)
    except User.DoesNotExist:
        return render_to_response('utilisateur/profile.html', {'requested_user':pseudo, 'error':"Sorry, no profile was found for",},  context_instance=RequestContext(request))

    # On recupere les badges remportes par le user du profil
    tmp_gagner = Gagner.objects.filter(utilisateur=user_to_display)
    badges = []
    for g in tmp_gagner :
        badges.append(Badge.objects.get(id=g.badge.id))
        
    # On recupere les defis releves par le user du profil
    tmp_releves = Relever.objects.filter(utilisateur=user_to_display)
    defis_releves = []  
    for r in tmp_releves :
        defis_releves.append(Defi.objects.get(id=r.defi.id))
    
    # On recupere les defis crees par le user du profil
    defis_crees = Defi.objects.filter(createur=user_to_display)
    
    #On recupere les trophees du user
    trophees_or = Reponse.objects.filter(utilisateur = user_to_display, classement = 1).count()
    trophees_ar = Reponse.objects.filter(utilisateur = user_to_display, classement = 2).count()
    trophees_br = Reponse.objects.filter(utilisateur = user_to_display, classement = 3).count()
    
    #On compte le nombre de defi releve
    taken = Relever.objects.filter(utilisateur = user_to_display).count()

    return render_to_response('utilisateur/profile.html', {'badges':badges, 
                                                           'user_to_display':user_to_display, 
                                                           'defis_releves':defis_releves, 
                                                           'defis_crees':defis_crees, 
                                                           'trophee_or' : trophees_or,
                                                           'trophee_ar' : trophees_ar,
                                                           'trophee_br' : trophees_br,
                                                           'taken' : taken,
                                                           }, context_instance=RequestContext(request))

        
#-----------------------EDITION PROFIL------------------------------------
def edit_profile(request):
    
    # On check si l'utilisateur est authentifie
    if request.user.is_authenticated(): 
    
        if request.method == 'POST':
            #recuperation des informations du formulaire
            user_form = EditUserForm(request.POST, instance=request.user)
            utilisateur_form = UtilisateurForm(request.POST, request.FILES, instance=request.user.get_profile())
            
            #si les infos sont valides
            if user_form.is_valid() and utilisateur_form.is_valid():
                #on change les infos de l'utilisateur
                user_form.save()
                utilisateur_form.save()
                    
                return HttpResponseRedirect("/")
        else:
            #creation des formulaires
            user_form = EditUserForm(instance=request.user)
            utilisateur_form = UtilisateurForm(instance=request.user.get_profile())
            
        return render_to_response("utilisateur/edit_profile.html", {'user_form': user_form, 'utilisateur_form': utilisateur_form,}, context_instance=RequestContext(request))
    
    else:
        return render_to_response("utilisateur/edit_profile.html", {'error': "You must login to edit your profile",}, context_instance=RequestContext(request))


#--------------------------------LISTE DES USERS-------------------------------
def list_challengers(request):
    #requete            
    utilisateurs = User.objects.all()         
    #recuperation des conditions de tri
    triUser = request.GET.get('triUser')
    if triUser :
        if triUser == 'Ncr' : utilisateurs = utilisateurs.order_by('username')
        elif triUser == 'Ndecr' : utilisateurs = utilisateurs.order_by('-username')

    #Recuperation du numero de la page 
    utilisateursP = Paginator(utilisateurs, 24)
    try: pageU = int(request.GET.get('pageU', '1'))
    except ValueError : pageU = 1
     
    #pagination
    try: pageUser = utilisateursP.page(pageU)
    except PageNotAnInteger: pageUser = utilisateursP.page(1)
    except EmptyPage: pageUser = utilisateursP.page(utilisateursP.num_pages)

    return render_to_response('utilisateur/list_challengers.html', {'utilisateurs':pageUser}, context_instance=RequestContext(request))

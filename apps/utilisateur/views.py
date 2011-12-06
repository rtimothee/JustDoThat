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
from django.template import RequestContext
from compiler.pycodegen import EXCEPT

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
      #return HttpResponseRedirect('/')
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
        
    return render_to_response("utilisateur/register.html", {'user_form': user_form, 'utilisateur_form': utilisateur_form,}, context_instance=RequestContext(request))

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
        
        
    return render_to_response('utilisateur/delete_account.html', {'user':user}, context_instance=RequestContext(request))

#-----------------------AFFICHAGE PROFIL------------------------------------
def display_profile(request, pseudo):
    
    # On recupere le user du profil a afficher
    try: user_to_display = User.objects.get(username=pseudo)
    except User.DoesNotExist:
        return render_to_response('utilisateur/profile.html', {'requested_user':pseudo, 'error':"Sorry, no profile was found for",},  context_instance=RequestContext(request))

    # On recupere badges remportes par le user du profil
    tmp_gagner = Gagner.objects.filter(utilisateur=user_to_display)
    badges = []
    for g in tmp_gagner :
        badges.append(Badge.objects.get(id=g.badge.id))
        
    # On recupere les défis releves par le user du profil
    tmp_releves = Relever.objects.filter(utilisateur=user_to_display)
    defis_releves = []  
    for r in tmp_releves :
        defis_releves.append(Defi.objects.get(id=r.defi.id))
    
    # On recupere les défis crees par le user du profil
    defis_crees = Defi.objects.filter(createur=user_to_display)
    
    return render_to_response('utilisateur/profile.html', {'badges':badges, 'user_to_display':user_to_display, 'defis_releves':defis_releves, 'defis_crees':defis_crees}, context_instance=RequestContext(request))

        
#-----------------------EDITION PROFIL------------------------------------
def edit_profile(request):
    
    if request.user.is_authenticated(): 
    
        if request.method == 'POST':
            #recupération des informations du formulaire
            user_form = UserForm(request.POST, instance=request.user)
            utilisateur_form = UtilisateurForm(request.POST, request.FILES, instance=request.user.get_profile())
            
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
            user_form = UserForm(instance=request.user)
            utilisateur_form = UtilisateurForm(instance=request.user.get_profile())
            
        return render_to_response("utilisateur/edit_profile.html", {'user_form': user_form, 'utilisateur_form': utilisateur_form,}, context_instance=RequestContext(request))
    
    else:
        return render_to_response("utilisateur/edit_profile.html", {'error': "You must login to edit your profile",}, context_instance=RequestContext(request))
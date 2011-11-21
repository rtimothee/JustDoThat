# -*- coding: utf-8 -*-
# Create your views here.
from JustDoThat.apps.utilisateur.models import *
from JustDoThat.apps.defi.models import *
from JustDoThat.apps.reponse.models import *
from django.contrib.auth.models import *

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.contrib.auth.views import login, logout
from django.shortcuts import render_to_response

#------------------------ LOGIN / LOGOUT -------------------
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

#----------------------- SUPPRESSION COMPTE --------------------
''' NE MARCHE PAS CAR IL FAUT AJOUTER LES CONDITIONS DE PRESENCE EN BDD -> TODO '''
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
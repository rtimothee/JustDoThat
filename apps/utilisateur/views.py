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
            try : defi = Defi.objects.get(createur=user)
            except Defi.DoesNotExist : pass
            else :  
                defi.createur = User.objects.get(username='Anonymous')
                defi.save()
            #suppression des liens
            try : relever = Relever.objects.get(utilisateur=user)
            except Relever.DoesNotExist : pass
            else : relever.delete()
            
            #suppression commentaires
            try : com = Commentaire.Objects.get(utilisateur=user)
            except Commentaire.DoesNotExist : pass
            else : com.delete()
            #suppression reponse
            try : reponse = Reponse.objects.get(utilisateur=user)
            except Reponse.DoesNotExist : pass
            else :reponse.delete()

            #suppression Messages prives
            try : msg = MessagePrive.objects.get(emeteur=user)
            except MessagePrive.DoesNotExist : pass
            else : msg.delete()
            try : msg = MessagePrive.objects.get(destinataire=user)
            except MessagePrive.DoesNotExist : pass
            else : msg.delete()

            #suppression Badges
            try : badge = Gagner.Objects.get(utilisateur=user)
            except Gagner.DoesNotExist : pass
            else : badge.delete()
            
            #suppression Utilisateur
            utilisateur = Utilisateur.Objects.get(user=user)
            utilisateur.delete()
            user.delete()
        
        
    return render_to_response('utilisateur/delete_account.html', {'user':user})
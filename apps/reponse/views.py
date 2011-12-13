# Create your views here.
from JustDoThat.apps.utilisateur.models import *
from JustDoThat.apps.defi.models import *
from JustDoThat.apps.defi.forms import *
from JustDoThat.apps.reponse.models import *
from JustDoThat.apps.reponse.models import *
from JustDoThat.apps.reponse.forms import *
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.contrib.auth.views import login, logout
from django.shortcuts import render_to_response
from JustDoThat.apps.utilisateur.tools import handle_uploaded_file


def reponse_view(request, int):
    defi = Defi.objects.get(id=int)
        
    releves = Relever.objects.filter(defi = defi.id)
    users = []
        
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
            return HttpResponseRedirect("/")
    else:
         Reponse_form = ReponseForm()
     
    
        
    return render_to_response("reponse/reponse.html", {'Reponse_form': Reponse_form,'defi': defi, 'difficulty': difficulte, 'category':category.nom, 'users':users})

def notation_view(request, userNotation, note_user, rep):
    #recuperation du user et de la reponse
    model_user = User.objects.get(id = userNotation)
    model_reponse = Reponse.objects.get(id = rep)
    
    #recuperation du nombre de vote de l'utilisateur sur la reponse
    notationExist = Noter.objects.filter(utilisateur = model_user, reponse = model_reponse).count()
    #si il n'a pas encore vote
    if(notationExist == 0):
        #choix de la note
        if(note_user > 0):
            noteF = Noter(note = True, utilisateur = model_user, reponse = model_reponse)
        else:
            noteF = Noter(note = False, utilisateur = model_user, reponse = model_reponse)
        noteF.save()
        statut = 'done'  
    #Si il a deja vote 
    else :
        statut = 'already vote'
    #recuperation de la nouvelle note
    note = Noter.objects.filter(reponse = model_reponse, note = True).count() - Noter.objects.filter(reponse = model_reponse, note = False).count()
    return render_to_response("reponse/ajax.html", {'note': note,'statut': statut})

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
from datetime import date


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
    note = model_reponse.note
    return render_to_response("reponse/ajax.html", {'note': note,'statut': statut})

def compfreq(elem1,elem2):
    if elem1[1]<elem2[1]:
        return -1
    if elem1[1]>elem2[1]:
        return 1
    return 0


def update_users_view(request):
	# en cours de dev pas beau ne pas faire attention
	# challenges= Defi.objects.extra(where=['fini = 0'])
	# for c in challenges :
		# notes = []
		# if c.timeleft == 'Challenge over':
			# reponses = Reponse.objects.filter(defi=c)
			# for r in reponses :
				# notes.append(r.note)
			# reponses_notes = sorted(zip(reponses, notes))
			# reponses_notes.sort(lambda x,y: cmp(x[1],y[1]), reverse=True)
			# reponses_notes.sort(compfreq, reverse=True)
			# reponses_notes[0:2]
			# for reponses, notes in reponses_notes :
				# if reponses_notes[0]:
					# reponses.classement = 1
					# reponses.save()
					# user1 = Utilisateur.objects.get(user= reponses.utilisateur)
					# user1.points = 150
					# user1.save()
				# if reponses_notes[1]:
					# reponses.classement = 2
					# reponses.save()
					# user2 = Utilisateur.objects.get(user = reponses.utilisateur)
					# user2.points = 100
					# user2.save()
				# if reponses_notes[2]:
					# reponses.classement = 3
					# reponses.save()
					# user3 = Utilisateur.objects.get(user = reponses.utilisateur)
					# user3.points = 50
					# user3.save()
	# c.fini = 1
	# c.save()

	return render_to_response("reponse/test.html", {'challenges': challenges})

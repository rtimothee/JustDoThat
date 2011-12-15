# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import date


#-------------------------------DEFI--------------------------------    
class Defi(models.Model):
	slug = models.SlugField(max_length=100)
	titre = models.CharField(max_length=100, null=False)
	description = models.TextField(null=False)
	debut = models.DateField(null=False, default=date.today())
	fin = models.DateField(null=False)
	photo = models.ImageField(upload_to=settings.IMAGE_UPLOAD_PATH_CHALLENGE, null=False)
	liste = ((1,'Easy'), (2,'Normal'),(3,'Hard'), (4,'Very Hard'))    
	difficulte = models.IntegerField(null=False, max_length=1, choices=liste)
	categorie = models.ForeignKey('Categorie')
	createur = models.ForeignKey(User)
    
    
	def __unicode__(self):
		return "%s %s" % (self.titre, self.description)
		
	def time_left(self):

		if self.fin <= date.today() :
			tl = 'Challenge over'
		else:
			tl = self.fin - self.debut
			tl = (str(tl.days)+'d')
		
		return "%s" % (tl)
	timeleft = property(time_left)
	
	def nb_releve(self):
		nb = Relever.objects.filter(defi = self.id).count()
		
		return "%s" % (nb)
	nbreleve = property(nb_releve)


#----------------------------CATEGORIES------------------------------    
class Categorie(models.Model):
    slug = models.SlugField(max_length=100)
    nom = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    
    
    def __unicode__(self):
        return "%s" % (self.nom)
		

    

#------------------------------RELEVER--------------------------------    
class Relever(models.Model):
    defi = models.ForeignKey('Defi')
    utilisateur = models.ForeignKey(User)
    
    
    def __unicode__(self):
        return "%s %s" % (self.defi, self.utilisateur)
    
    
    
    
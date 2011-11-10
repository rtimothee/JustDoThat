from django.db import models
from JustDoThat.apps.utilisateur.models import Utilisateur


#-------------------------------DEFI--------------------------------    
class Defi(models.Model):
    slug = models.SlugField(max_length=100)
    titre = models.CharField(max_length=100)
    description = models.TextField()
    debut = models.DateField()
    fin = models.DateField()
    photo = models.URLField()
    difficulte = models.IntegerField()
    categorie = models.ForeignKey('Categorie')
    createur = models.ForeignKey(Utilisateur)
    
    
    def __unicode__(self):
        return "%s %s" % (self.titre, self.description)


#----------------------------CATEGORIES------------------------------    
class Categorie(models.Model):
    slug = models.SlugField(max_length=100)
    nom = models.CharField(max_length=100)
    description = models.TextField()
    
    
    def __unicode__(self):
        return "%s %s" % (self.nom, self.description)
    

#------------------------------RELEVER--------------------------------    
class Relever(models.Model):
    defi = models.ForeignKey('Defi')
    utilisateur = models.ForeignKey(Utilisateur)
    
    
    def __unicode__(self):
        return "%s %s" % (self.defi, self.utilisateur)
    
    
    
    
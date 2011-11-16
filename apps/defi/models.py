from django.db import models
from django.contrib.auth.models import User


#-------------------------------DEFI--------------------------------    
class Defi(models.Model):
    slug = models.SlugField(max_length=100)
    titre = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    debut = models.DateField(null=False)
    fin = models.DateField(null=False)
    photo = models.URLField(null=False)
    difficulte = models.IntegerField(null=False)
    categorie = models.ForeignKey('Categorie')
    createur = models.ForeignKey(User)
    
    
    def __unicode__(self):
        return "%s %s" % (self.titre, self.description)


#----------------------------CATEGORIES------------------------------    
class Categorie(models.Model):
    slug = models.SlugField(max_length=100)
    nom = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    
    
    def __unicode__(self):
        return "%s %s" % (self.nom, self.description)
    

#------------------------------RELEVER--------------------------------    
class Relever(models.Model):
    defi = models.ForeignKey('Defi')
    utilisateur = models.ForeignKey(User)
    
    
    def __unicode__(self):
        return "%s %s" % (self.defi, self.utilisateur)
    
    
    
    
from django.db import models
from JustDoThat.apps.utilisateur.models import Utilisateur
from JustDoThat.apps.defi.models import Defi

#-------------------------------REPONSE--------------------------------    
class Reponse(models.Model):
    slug = models.SlugField(max_length=100)
    message = models.TextField()
    date_reponse = models.DateField()
    photo = models.URLField()
    notification = models.BooleanField()
    defi = models.ForeignKey(Defi)
    utilisateur = models.ForeignKey(Utilisateur)
    
    def __unicode__(self):
        return "%s %s" % (self.message, self.date_reponse)
    

#-----------------------------COMMENTAIRE------------------------------    
class Commenaire(models.Model):
    message = models.TextField()
    date_commentaire = models.DateField()
    moderation = models.BooleanField()
    notification = models.BooleanField()
    reponse = models.ForeignKey('Reponse')
    utilisateur = models.ForeignKey(Utilisateur)
    
    def __unicode__(self):
        return "%s %s" % (self.message, self.reponse)
    
    
#-------------------------------NOTER---------------------------------    
class Noter(models.Model):
    note = models.BooleanField()
    reponse = models.ForeignKey('Reponse')
    utilisateur = models.ForeignKey(Utilisateur)
    
    def __unicode__(self):
        return "%s %s" % (self.note, self.reponse)
from django.db import models
from django.contrib.auth.models import User
from JustDoThat.apps.defi.models import Defi

#-------------------------------REPONSE--------------------------------    
class Reponse(models.Model):
    slug = models.SlugField(max_length=100,null=False)
    message = models.TextField()
    date_reponse = models.DateField(null=False)
    photo = models.URLField(null=False)
    notification = models.BooleanField(null=False)
    defi = models.ForeignKey(Defi)
    utilisateur = models.ForeignKey(User)
    
    def __unicode__(self):
        return "%s %s" % (self.message, self.date_reponse)
    

#-----------------------------COMMENTAIRE------------------------------    
class Commenaire(models.Model):
    message = models.TextField(null=False)
    date_commentaire = models.DateField(null=False)
    moderation = models.BooleanField(null=False)
    notification = models.BooleanField(null=False)
    reponse = models.ForeignKey('Reponse')
    utilisateur = models.ForeignKey(User)
    
    def __unicode__(self):
        return "%s %s" % (self.message, self.reponse)
    
    
#-------------------------------NOTER---------------------------------    
class Noter(models.Model):
    note = models.BooleanField(null=False)
    reponse = models.ForeignKey('Reponse')
    utilisateur = models.ForeignKey(User)
    
    def __unicode__(self):
        return "%s %s" % (self.note, self.reponse)
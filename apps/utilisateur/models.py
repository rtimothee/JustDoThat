from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

#-------------------------------UTILISATEUR--------------------------------    
class Utilisateur(models.Model):
    #User_Auth de Django
    user = models.ForeignKey(User, unique=True)
    
    #Ajout de nos champs perso
    avatar = models.ImageField(upload_to=settings.IMAGE_UPLOAD_PATH, null=False)
    points = models.IntegerField(null=True)
    dateNaissance = models.DateField(null=False)
    pays = models.CharField(max_length=45, null=False)
    sexeM = models.BooleanField(null=False)
    
    def __unicode__(self):
        return "%s %s" % (self.user.username, self.points)


#---------------------------MESSAGE PRIVE-----------------------------    
class MessagePrive(models.Model):
    message = models.TextField(max_length=45, null=False)
    dateMessage = models.DateField(null=False)
    lu = models.BooleanField(null=False)
    emeteur = models.ForeignKey(User, related_name='messagePrive_emeteur') 
    destinataire = models.ForeignKey(User, related_name='messagePrive_destinataire') 
    
    def __unicode__(self):
        return "%s %s" % (self.message, self.emeteur)


#------------------------------BADGE--------------------------------    
class Badge(models.Model):
    titre = models.CharField(max_length=45, null=False)
    description = models.TextField(max_length=45)
    photo = models.URLField(null=False)
    dateBadge = models.DateField(null=False)
    notification = models.BooleanField(null=False)
    
    def __unicode__(self):
        return "%s %s" % (self.titre, self.description)
    
    
#------------------------------GAGNER--------------------------------    
class Gagner(models.Model):
    badge = models.ForeignKey('Badge') 
    utilisateur = models.ForeignKey(User) 
    
    def __unicode__(self):
        return "%s %s" % (self.badge, self.utilisateur)

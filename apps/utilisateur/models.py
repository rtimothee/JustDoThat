from django.db import models

#-------------------------------UTILISATEUR--------------------------------    
class Utilisateur(models.Model):
    slug = models.SlugField(max_length=100)
    pseudo = models.CharField(max_length=45)
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    mail = models.EmailField()
    avatar = models.URLField()
    points = models.IntegerField()
    dateNaissance = models.DateField()
    pays = models.CharField(max_length=45)
    sexeM = models.BooleanField()
    
    def __unicode__(self):
        return "%s %s" % (self.pseudo, self.points)


#---------------------------MESSAGE PRIVE-----------------------------    
class MessagePrive(models.Model):
    message = models.TextField(max_length=45)
    dateMessage = models.DateField()
    lu = models.BooleanField()
    emeteur = models.ForeignKey('Utilisateur', related_name='messagePrive_emeteur') 
    destinataire = models.ForeignKey('Utilisateur', related_name='messagePrive_destinataire') 
    
    def __unicode__(self):
        return "%s %s" % (self.pseudo, self.points)


#------------------------------BADGE--------------------------------    
class Badge(models.Model):
    titre = models.CharField(max_length=45)
    description = models.TextField(max_length=45)
    photo = models.URLField()
    dateBadge = models.DateField()
    notification = models.BooleanField()
    
    def __unicode__(self):
        return "%s %s" % (self.pseudo, self.points)
    
    
#------------------------------GAGNER--------------------------------    
class Gagner(models.Model):
    badge = models.ForeignKey('Badge') 
    utilisateur = models.ForeignKey('Utilisateur') 
    
    def __unicode__(self):
        return "%s %s" % (self.pseudo, self.points)

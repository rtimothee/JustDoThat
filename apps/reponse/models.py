from django.db import models
from django.contrib.auth.models import User
from JustDoThat.apps.defi.models import Defi
from django.conf import settings
from datetime import date

#-------------------------------REPONSE--------------------------------    
class Reponse(models.Model):

	slug = models.SlugField(max_length=100,null=False)
	message = models.TextField()
	date_reponse = models.DateField(null=False, default=date.today())
	photo = models.ImageField(upload_to=settings.IMAGE_UPLOAD_PATH_REPONSE, default='reponse_pics/defaut.jpg', null=False)
	notification = models.BooleanField(default=True)
	defi = models.ForeignKey(Defi)
	utilisateur = models.ForeignKey(User)
	classement = models.IntegerField(null=False,default=4)


	def __unicode__(self):
		return "%s %s" % (self.message, self.date_reponse)

    
	def note_fonc(self):
		var = Noter.objects.filter(reponse = self, note = True).count() - Noter.objects.filter(reponse = self, note = False).count()
		return "%d" % (var)
	note = property(note_fonc)
    

#-----------------------------COMMENTAIRE------------------------------    
class Commentaire(models.Model):
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
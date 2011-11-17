from django.contrib import admin
from JustDoThat.apps.reponse.models import Reponse
from JustDoThat.apps.reponse.models import Commentaire
from JustDoThat.apps.reponse.models import Noter

admin.site.register(Noter)
admin.site.register(Commentaire)
admin.site.register(Reponse)
 
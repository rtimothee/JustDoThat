from django.contrib import admin
from JustDoThat.apps.reponse.models import Reponse
from JustDoThat.apps.reponse.models import Commenaire
from JustDoThat.apps.reponse.models import Noter

admin.site.register(Noter)
admin.site.register(Commenaire)
admin.site.register(Reponse)
 
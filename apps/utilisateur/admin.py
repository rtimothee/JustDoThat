from django.contrib import admin
from JustDoThat.apps.utilisateur.models import Utilisateur
from JustDoThat.apps.utilisateur.models import MessagePrive
from JustDoThat.apps.utilisateur.models import Badge
from JustDoThat.apps.utilisateur.models import Gagner


admin.site.register(Utilisateur)
admin.site.register(MessagePrive)
admin.site.register(Badge)
admin.site.register(Gagner)

 
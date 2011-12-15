from django.conf.urls.defaults import patterns, include, url
#from django.contrib.auth.views import login, logout
from JustDoThat.apps.reponse.views import *

urlpatterns = patterns('',
  url(r'^reponse/(?P<int>[\w-]+)/$',  reponse_view, name="reponse"),
  url(r'^update_users/$',  update_users_view, name="update_users"),
  url(r'^notation_ajax/(?P<userNotation>[\w-]+)/(?P<note_user>[\w-]+)/(?P<rep>[\w-]+)/$', notation_view, name='notation_view'),
 )


from django.conf.urls.defaults import patterns, include, url
#from django.contrib.auth.views import login, logout
from JustDoThat.apps.reponse.views import *

urlpatterns = patterns('',
  url(r'^reponse/(?P<int>[\w-]+)/$',  reponse_view, name="reponse"),
 
 )


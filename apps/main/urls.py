from django.conf.urls.defaults import patterns, include, url
#from django.contrib.auth.views import login, logout
from JustDoThat.apps.main.views import *

urlpatterns = patterns('',
  url(r'^index/', index, name='index'),
  url(r'^search/', recherche, name='recherche'),
  #url(r'^advanced_search/', recherche_av, name='recherche_av'),
)


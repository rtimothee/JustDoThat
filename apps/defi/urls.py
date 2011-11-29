from django.conf.urls.defaults import patterns, include, url
#from django.contrib.auth.views import login, logout
from JustDoThat.apps.defi.views import *

urlpatterns = patterns('',
  url(r'^modif_challenge/(?P<int>[\w-]+)/$',  modif_challenge_view, name="modif_challenge"),
  url(r'^delete_challenge/(?P<int>[\w-]+)/$',  delete_challenge_view, name="delete_challenge"),
  url(r'^create_challenge/$',  create_challenge_view, name="create_challenge"),
  url(r'^display_challenge/(?P<int>[\w-]+)/$',  display_challenge_view, name="display_challenge"),
  url(r'^challenges/$',  challenges_view, name="challenges"),
)

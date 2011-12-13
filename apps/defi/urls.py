from django.conf.urls.defaults import patterns, include, url
#from django.contrib.auth.views import login, logout
from JustDoThat.apps.defi.views import *

urlpatterns = patterns('',
  url(r'^modif_challenge/(?P<int>[\w-]+)/$',  modif_challenge_view, name="modif_challenge"),
  url(r'^delete_challenge/(?P<int>[\w-]+)/(?P<delete>[\w-]+)/$',  delete_challenge_view, name="delete_challenge"),
  url(r'^create_challenge/$',  create_challenge_view, name="create_challenge"),
  url(r'^display_challenge/(?P<int>[\w-]+)/$',  display_challenge_view, name="display_challenge"),
  url(r'^list_challenges/$',  challenges_view, name="list_challenges"),
  url(r'^create_reponse/(?P<int>[\w-]+)/$',  create_reponse_view, name="create_reponse"),
  url(r'^modif_reponse/(?P<int>[\w-]+)/$',  modif_reponse_view, name="modif_reponse"),
  url(r'^delete_reponse/(?P<int>[\w-]+)/$',  delete_reponse_view, name="delete_reponse"),
)


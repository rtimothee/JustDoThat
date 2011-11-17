from django.conf.urls.defaults import patterns, include, url
#from django.contrib.auth.views import login, logout
from JustDoThat.apps.utilisateur.views import *

urlpatterns = patterns('',
  url(r'^login/$',  login_view, name="login"),
  url(r'^logout/$',  logout_view, name="logout"),
  #url(r'^login/$',  login),
  #url(r'^logout/$', logout),
  url(r'^delete/(?P<pseudo>[\w-]+)$', delete_account, name='delete_account'),
)


from django.conf.urls.defaults import patterns, include, url
#from django.contrib.auth.views import login, logout
from JustDoThat.apps.utilisateur.views import *

urlpatterns = patterns('',
  url(r'^login/$',  login_view, name="login"),
  url(r'^logout/$',  logout_view, name="logout"),
  url(r'^register/$',  register_view, name="register"),
  url(r'^delete/(?P<pseudo>[\w-]+)$', delete_account, name='delete_account'),
  url(r'^profile/(?P<pseudo>[\w-]+)',  display_profile, name="profile"),
  url(r'^edit-profile/$',  edit_profile, name="edit_profile"),
)


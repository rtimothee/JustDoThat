from django.conf.urls.defaults import patterns, include, url
#from django.contrib.auth.views import login, logout
from JustDoThat.apps.utilisateur.views import *

urlpatterns = patterns('',
  url(r'^login/$',  login_view, name="login"),
  url(r'^logout/$',  logout_view, name="logout"),
  url(r'^register/$',  register_view, name="register"),
  url(r'^profile/(?P<pseudo>[\w-]+)/$',  display_profile, name="profile"),
  url(r'^send_message/(?P<pseudo>[\w-]+)$',  send_message_view, name="send_message"),
  url(r'^inbox/$',  inbox_view, name="inbox"),
  url(r'^conversation/(?P<pseudo>[\w-]+)/$',  conversation_view, name="outbox"),
  url(r'^delete_account/$', delete_account, name='delete_account'),
  url(r'^edit-profile/$',  edit_profile, name="edit_profile"),
)


from django.conf.urls import patterns

urlpatterns = patterns('',
#url(r'^main/$', 'example.views.main'),
(r'^login/$', 'auth.views.login_user'),
)
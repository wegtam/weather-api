from django.conf.urls import patterns, url

urlpatterns = patterns('view.views',
                        url(r'^$', 'index', name='view_index'),
                        url(r'^ws/(?P<ws_id>[-\w]+)/$', 'detail', name='view-detail'),
                        url(r'^user/(?P<user_id>[-\w]+)/$', 'user_ws', name='view-user_ws'),
                        #
                        # url(r'^save_wd/', 'save_wd'),
                        url(r'^save_wd/(?P<humidity>(\d+(?:\.\d+)?))/(?P<temperature>(\d+(?:\.\d+)?))/(?P<altitude>(\d+(?:\.\d+)?))/(?P<air_pressure>(\d+(?:\.\d+)?))/(?P<lightness>(\d+(?:\.\d+)?))/(?P<weatherstation_id>(\d+))/(?P<user_id>(\d+))/$', 'save_wd'),
)
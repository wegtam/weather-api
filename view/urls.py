from django.conf.urls import patterns, url

urlpatterns = patterns('view.views',
                        url(r'^$', 'index', name='view_index'),
                        url(r'^ws/(?P<ws_id>[-\d]+)/$', 'detail', name='view-detail'),
                        url(r'^user/(?P<user_id>[-\w]+)/$', 'user_ws', name='view-user_ws'),
                        url(r'^save_wd/', 'save_wd'),
                        url(r'^city_wd/$', 'city_wd')
)
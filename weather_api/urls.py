from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'weather_api.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       #url(r'^test/', 'api.views.my_view'),
                       #url(r'^login/', 'api.views.login'),
                       url(r'^$', 'api.views.index'),
                       url(r'^ws/(?P<ws_id>[-\w]+)/$', 'api.views.detail'),
                       url(r'^user/(?P<user_id>[-\w]+)/$', 'api.views.user_ws'),
                       url(r'^test/(?P<user_id>[-\w]+)/$', 'api.views.test_wd')
                       #url(r'^ws/', 'api.views.detail')
)

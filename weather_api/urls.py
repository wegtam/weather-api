from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'weather_api.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('view.urls')),

                       #url(r'^test/', 'view.views.my_view'),
                       #url(r'^login/', 'view.views.login'),
                       #url(r'^$', 'view.views.index'),
                       #url(r'^ws/(?P<ws_id>[-\w]+)/$', 'view.views.detail'),
                       #url(r'^user/(?P<user_id>[-\w]+)/$', 'view.views.user_ws')
)

from django.conf.urls import *
from tastypie.api import Api
from .resources import UserResource, WSResource, WDResource


v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(WSResource())
v1_api.register(WDResource())

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
)
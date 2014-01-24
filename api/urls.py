from django.conf.urls import *
from tastypie.api import Api
from .resources import UserResource,EntryResource, WsResource

v1_api = Api(api_name='v1')
v1_api.register(WsResource())
v1_api.register(UserResource())
v1_api.register(EntryResource())

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
)
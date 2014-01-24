from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from .models import Weatherstation, Weatherdata


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        filtering = {
            'username': ALL,
        }


class WsResource(ModelResource):
    class Meta:
        queryset = Weatherstation.objects.all()
        resource_name = 'weatherstation'
        excludes = ['user']
        filtering = {
            'name': ALL,
        }
        object_class = 'name'


class EntryResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    weatherstation = fields.ForeignKey(WsResource, 'weatherstation')

    class Meta:
        queryset = Weatherdata.objects.all()
        """queryset = User.objects.all()"""
        resource_name = 'weatherdata'
        authorization = Authorization()
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'weatherstation': ALL_WITH_RELATIONS,
        }
from django.contrib.auth.models import User
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


class WSResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Weatherstation.objects.all()
        resource_name = 'ws'
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'id': 'exact',
        }


class WDResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    weatherstation = fields.ForeignKey(WSResource, 'weatherstation')

    class Meta:
        queryset = Weatherdata.objects.all()
        resource_name = 'wd'
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'weatherstation': ALL_WITH_RELATIONS,
        }
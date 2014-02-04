from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.exceptions import Unauthorized

from .models import Weatherstation, Weatherdata


class UserObjectsOnlyAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list.filter(user=bundle.request.user)

    def read_detail(self, object_list, bundle):
        # Is the requested object owned by the user?
        return bundle.obj.user == bundle.request.user

    def create_list(self, object_list, bundle):
        # Assuming they're auto-assigned to ``user``.
        return object_list

    def create_detail(self, object_list, bundle):
        return bundle.obj.user == bundle.request.user

    def update_list(self, object_list, bundle):
        allowed = []

        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if obj.user == bundle.request.user:
                allowed.append(obj)

        return allowed

    def update_detail(self, object_list, bundle):
        return bundle.obj.user == bundle.request.user

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")


class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        filtering = {
            'username': ALL,
        }


class WSResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Weatherstation.objects.all()
        resource_name = 'ws'
        authentication = ApiKeyAuthentication()
        authorization = UserObjectsOnlyAuthorization()
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'id': ['exact'],
        }


class WDResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    weatherstation = fields.ForeignKey(WSResource, 'weatherstation')

    class Meta:
        queryset = Weatherdata.objects.all()
        resource_name = 'wd'
        authentication = ApiKeyAuthentication()
        authorization = UserObjectsOnlyAuthorization()
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'weatherstation': ['exact'],
        }
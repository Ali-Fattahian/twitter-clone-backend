from urllib import request
from django.core.exceptions import PermissionDenied
from rest_framework import permissions


# only the user has access to edit-profile page specific to that user
class OnlySameUserCanEditMixin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user

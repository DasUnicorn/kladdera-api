from rest_framework import permissions


class IsSuperUserOrSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow superusers to perform any action
        if request.user.is_superuser:
            return True

        # Allow users to perform actions on their own profile
        return obj == request.user
        

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

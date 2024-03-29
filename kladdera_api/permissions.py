from rest_framework import permissions

class IsOwner(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.owner == request.user

class IsUser(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.self == request.user

class IsAdmin(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.self.is_admin == request.user.is_admin
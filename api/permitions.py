from rest_framework.permissions import BasePermission


class UserListAPIPermition(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class UserAPIPermition(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user

from rest_framework import permissions


class ProductPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
            or request.user.is_saller
        )

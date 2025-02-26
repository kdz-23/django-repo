from rest_framework.permissions import BasePermission

class IsAdminOrSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user  # Admins or self

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user  # Only post owner can modify

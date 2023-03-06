from rest_framework import permissions


# PERMISSION SO THAT ONLY THE OWNER OF A PROJECT CAN EDIT
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
           	return True
        return obj.owner == request.user
from rest_framework import permissions

class IsStaffOrReadOnly(permissions.IsAdminUser):
    message = "You don't have permission to perform this action! (by Feanor)"

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)

class IsOwnerAndStaffOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user.is_staff and (obj.create_user == request.user))





from rest_framework import permissions


class CanInteractWithBookAPI(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return request.user.username == request.data["author"]
        return request.user.is_authenticated

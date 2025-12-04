from rest_framework.permissions import BasePermission
from Admin.models.user import CLIENT, DRIVER


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == CLIENT

class IsDriver(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == DRIVER

# TODO здесь производится настройка пермишенов для нашего проекта

from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsOwner(BasePermission):
    message = "Вы не владелец объекта"

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'owner'):
            owner = obj.owner
        elif hasattr(obj, 'author'):
            owner = obj.author
        else:
            raise Exception("error")
        return owner == request.user


class IsStaff(BasePermission):
    message = "Вы не администратор"

    def has_permission(self, request, view):
        return request.user.role in [UserRoles.ADMIN]

from rest_framework import permissions
from rest_framework.exceptions import MethodNotAllowed


class AuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Разрешение на доступ только администраторам для создания объектов,
    остальным пользователям доступно только чтение.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user or not request.user.is_staff:
            raise MethodNotAllowed(
                request.method,
                detail='Создание объектов доступно только администратору.'
            )

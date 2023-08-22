from rest_framework import permissions

from app.curriculums.models import Category


class BelongsToUserOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_admin:
            return True
        return obj.user == request.user


class BelongsToUserByCategoryOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_admin:
            return True
        return obj.category.user == request.user


class CategoryBelongsToUserOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        categoryId = request.data.get('category')
        category = Category.objects.get(id=categoryId)
        return request.user.is_admin or category.user == request.user

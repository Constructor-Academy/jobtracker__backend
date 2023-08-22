from rest_framework import permissions


class JobsBelongToUserOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        jobs = request.data['jobs']
        if request.user.is_admin:
            return True
        for job in jobs:
            if job['user'] != request.user.id:
                return False
        return True


class JobBelongsToUserOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user or request.user.is_admin:
            return True
        return False


class JobsNotEmpty(permissions.BasePermission):
    def has_permission(self, request, view):
        jobs = request.data['jobs']
        if len(jobs) == 0:
            if request.method == 'DELETE':
                return True
            return False
        return True

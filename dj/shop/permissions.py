from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import Group


def _is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None


def _has_group_permission(user, required_groups):
    return any([_is_in_group(user, group_name) for group_name in required_groups])


class GroupBasePermission(BasePermission):
    def has_permission(self, request, view):
        if self.required_groups is None:
            return False
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return has_group_permission







class IsContentGroup(GroupBasePermission):
    required_groups = ['content']





class IsContentOrReadOnly:
    def has_permission(self, request, view):
        return (
            IsContentGroup().has_permission(request, view)
            or
            request.method in SAFE_METHODS
        )

    def has_object_permission(self, request, view, obj):
        return True

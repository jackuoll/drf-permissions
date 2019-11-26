from rest_framework import permissions
from .models import UserFeedPermissions


class TestPermissions(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        feed_permissions = UserFeedPermissions.objects.filter(user=user)
        return obj.owned_by in feed_permissions

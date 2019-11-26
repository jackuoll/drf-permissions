from rest_framework import permissions
from .models import UserFeedPermissions


class TestPermissions(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        return UserFeedPermissions.objects.filter(
            user=user,
            feed=obj.owned_by
        ).exists()

    def has_permission(self, request, view):
        if not request.POST:
            return super(TestPermissions, self).has_permission(request, view)

        return UserFeedPermissions.objects.filter(user=request.user, feed_id=request.POST['owned_by'])

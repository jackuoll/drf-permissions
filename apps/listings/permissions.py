from rest_framework import permissions
from .models import UserFeedPermissions


class TestPermissions(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_superuser:
            return True
        return UserFeedPermissions.objects.filter(
            user=user,
            feed=obj.owned_by
        ).exists()

    def has_permission(self, request, view):
        """
            view.action = create, retrieve, update, partial_update, destroy, list
        :param request:
        :param view:
        :return:
        """
        if request.user.is_superuser:
            return True
        # create is the only action where there is no current object
        if not view.action == 'create':
            return super(TestPermissions, self).has_permission(request, view)

        # these will be handled by `has_object_permission` or `view.get_queryset`
        return UserFeedPermissions.objects.filter(user=request.user, feed_id=request.data['owned_by'])

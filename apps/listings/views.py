from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Listing, UserFeedPermissions
from .serializers import ListingSerializer
from .permissions import TestPermissions


class ListingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()
    permission_classes = (permissions.DjangoModelPermissions, TestPermissions, )

    def get_queryset(self):
        request = self.request
        qs = super(ListingViewSet, self).get_queryset()
        if not request or not request.user:
            return qs

        user = request.user
        feed_perms = UserFeedPermissions.objects.filter(user=user)
        return qs.filter(owned_by__in=feed_perms.values('feed'))

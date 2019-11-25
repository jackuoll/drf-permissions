from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing
from .serializers import ListingSerializer
from .permissions import TestPermissions


class ListingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()
    permission_classes = (TestPermissions, )

    def get_queryset(self):
        request = self.request
        qs = super(ListingViewSet, self).get_queryset()
        if not request or not request.user:
            return qs

        user = request.user
        return qs.filter(owned_by=6)

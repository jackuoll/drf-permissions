from django.shortcuts import render
from rest_framework import viewsets
from .models import TestModel
from .serializers import TestModelSerializer
from .permissions import TestPermissions


class TestModelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = TestModelSerializer
    queryset = TestModel.objects.all()
    permission_classes = (TestPermissions, )

    def get_queryset(self):
        request = self.request
        qs = super(TestModelViewSet, self).get_queryset()
        if not request or not request.user:
            return qs

        user = request.user
        return qs.filter(owned_by=6)

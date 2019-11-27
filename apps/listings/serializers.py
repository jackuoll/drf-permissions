from rest_framework import serializers
from .models import Listing, Feed


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'

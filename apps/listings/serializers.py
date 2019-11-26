from rest_framework import serializers
from .models import Listing, UserFeedPermissions


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'

    # def create(self, validated_data):
    #     feed = validated_data['owned_by']
    #     user = self.context['request'].user
    #     has_permission = UserFeedPermissions.objects.filter(user=user, feed=feed).exists()
    #     if not has_permission:
    #         return False
    #     return super(ListingSerializer, self).create(validated_data)

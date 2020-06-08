from django.contrib import admin
from django.contrib.auth.models import User

from .models import UserFeedPermissions, Feed, Listing


@admin.register(UserFeedPermissions)
class UserFeedPermissionsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'feed')
    pass


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    pass


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'data', 'owned_by', )


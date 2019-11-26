from django.contrib import admin
from .models import UserFeedPermissions, Feed, Listing


@admin.register(UserFeedPermissions)
class UserFeedPermissionsAdmin(admin.ModelAdmin):
    pass


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    pass


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('data', 'owned_by', )

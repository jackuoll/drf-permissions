from django.db import models
from django.contrib.auth.models import User


class Feed(models.Model):
    name = models.CharField(max_length=255)


class UserFeedPermissions(models.Model):
    user = models.ForeignKey(User)
    feed = models.ForeignKey(Feed)


class Listing(models.Model):
    owned_by = models.ForeignKey(Feed)
    data = models.TextField()

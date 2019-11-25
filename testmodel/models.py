from django.db import models


class TestModel(models.Model):
    owned_by = models.IntegerField()
    data = models.TextField()

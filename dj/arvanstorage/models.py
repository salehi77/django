from django.db import models
from django.conf import settings
from .storage import MyStorage


class Document(models.Model):
    title = models.CharField(max_length=255)
    upload = models.FileField(storage=MyStorage)

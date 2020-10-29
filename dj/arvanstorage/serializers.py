from rest_framework import serializers
from . import models
from django.core import exceptions


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Document
        fields = '__all__'

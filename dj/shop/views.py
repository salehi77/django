from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from . import serializers
from . import models


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from . import serializers
from . import models
from . import permissions


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            return serializers.WriteCategorySerializer
        else:
            return serializers.ReadCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()



class SetCategory(views.APIView):

    def post(self, request):

        print(request.data)

        return Response({'a': 'b'})

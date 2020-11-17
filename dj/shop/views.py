from rest_framework import viewsets, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from . import serializers, models, permissions
from django.db.models import Avg, Count, Max, Min


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            return serializers.WriteCategorySerializer
        else:
            return serializers.ReadCategorySerializer



class CategoryView(views.APIView):
    def get(self, request, slug_title):
        instance = models.Category.objects.get(slug_title=slug_title)
        serializer = serializers.ReadCategorySerializer(instance, context={'request': request})
        return Response(serializer.data)



class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()



class ProductView(views.APIView):
    def get(self, request, slug_title):
        instance = models.Product.objects.get(slug_title=slug_title)
        serializer = serializers.ProductSerializer(instance, context={'request': request})
        return Response(serializer.data)

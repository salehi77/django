from rest_framework import serializers
from . import models
from django.core import exceptions



class ReadCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        # fields = ('id', 'parent', 'products', 'subcat')
        fields = '__all__'

    def get_fields(self):
        fields = super(ReadCategorySerializer, self).get_fields()
        # fields['parent'] = ReadCategorySerializer()
        # fields['subcat'] = ReadCategorySerializer(many=True, read_only=True)
        # fields['products'] = ProductSerializer(many=True, read_only=True)
        return fields


class WriteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
        read_only_fields = ('slug_title',)





class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        # fields = ('id',)
        fields = '__all__'
        read_only_fields = ('slug_title',)

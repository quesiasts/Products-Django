from rest_framework import serializers
from django.contrib.auth.models import Product, ProductHistory


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['historic_model', 'barcode', 'brand', 'title', 
                'description', 'status', 'height', 'width', 'length',
                'weight', 'region', 'active', 'errors']


class ProductHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductHistory
        fields = ['product', 'data']

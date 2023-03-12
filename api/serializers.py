from rest_framework import serializers

from api import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')


class ProductSerializer(serializers.Serializer):
    category = CategorySerializer()

    class Meta:
        model = models.Product
        fields = '__all__'

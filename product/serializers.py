from rest_framework import serializers
from product.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('title', 'desc_ru', 'desc_en', 'price', 'preview', 'id', 'category')


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class ProductFilterSerializer(serializers.ModelSerializer):
    max = serializers.CharField(required=True)
    min = serializers.CharField(required=True)
    class Meta:
        model = Product
        fields = ('max', 'min')


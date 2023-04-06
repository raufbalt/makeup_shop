from rest_framework import serializers
from product.models import Product, ProductImages, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        exclude = ('id', 'title')



class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('title', 'desc_ru', 'desc_en', 'price', 'preview', 'id', 'category')


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        product = Product.objects.create(**validated_data)
        images_data = request.FILES.getlist('images')
        images_objects = [ProductImages(product=product, image=image) for image in images_data]
        ProductImages.objects.bulk_create(images_objects)
        return product

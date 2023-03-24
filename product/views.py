from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from rest_framework.generics import ListAPIView, GenericAPIView

from .models import Product, Category
from . import serializers
from .serializers import CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductListSerializer
        if self.action in ('update', 'create', 'partial_update'):
            return serializers.ProductSerializer
        return serializers.ProductDetailSerializer

    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        category = self.request.data.get('category', None)
        cat1 = get_object_or_404(Category, id=category)
        serializer.save(
            availability = self.request.data.get('availability', None),
            category = cat1
        )


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryCreateAPIView(GenericAPIView):
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not request.data['name_ru'] or not request.data['name_eng']:
            return Response('Bad request', status=403)
        serializer.save(
            name_ru = request.data['name_ru'],
            name_eng = request.data['name_eng']
        )
        return Response('Created', status=201)

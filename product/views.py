from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import Product
from . import serializers

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
        serializer.save(
            availability = self.request.data.get('availability', None)
        )

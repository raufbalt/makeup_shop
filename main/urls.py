"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from product.views import ProductViewSet, CategoryListAPIView, CategoryCreateAPIView, ProductFilterAPIView
from order.views import OrderCreateAPIView

schema_view = get_schema_view(
   openapi.Info(
      title="MakeUp shop",
      default_version='v1',
      description="Test REST API backend at django",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = SimpleRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    #JWT TOKEN
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #main
    path('api/v1/', include(router.urls)),
    path('api/v1/accounts/', include('account.urls')),
    #order
    path('api/v1/order/', view=OrderCreateAPIView.as_view(), name="register"),
    #categ
    path('api/v1/categorylist/', view=CategoryListAPIView.as_view(), name='categorylist'),
    path('api/v1/categorycreate/', view=CategoryCreateAPIView.as_view(), name='categorycreate'),
    #filter
    path('api/v1/productfilter/', view=ProductFilterAPIView.as_view(), name='productfilter')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


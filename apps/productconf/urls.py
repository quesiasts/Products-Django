from django.urls import path, include
from rest_framework import routers
from ..product.views import ProductHistoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'product_history', ProductHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

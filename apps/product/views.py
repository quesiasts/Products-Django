import django_filters
from .serializers import ProductSerializer, ProductHistorySerializer
from rest_framework import viewsets
from django.contrib.auth.models import Product, ProductHistory


class ProductFilterSet(django_filters.FilterSet):
    brand = django_filters.CharFilter(method="filter_brand")
    class Meta:
        model = Product
        fields = ("active", "status", "brand")

class ProductHistoryFilterSet(django_filters.FilterSet):
    barcode = django_filters.CharFilter(field_name="data__barcode", help_text="Filter by barcode")

    class Meta:
        model = ProductHistory
        fields = ("barcode",)

class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductHistoryViewSet(
    viewsets.PageNumberLimitOffsetModelViewSetMixin,
    viewsets.ReadOnlyModelViewSet,
):
    queryset = ProductHistory.objects.select_related("product").all()
    serializer_class = ProductHistorySerializer
    filterset_class = ProductHistoryFilterSet
    ordering = ("-created_at",)

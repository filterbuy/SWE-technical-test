from __future__ import annotations

from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """API endpoint for managing products."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
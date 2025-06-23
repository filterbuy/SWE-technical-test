from __future__ import annotations

from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_name(self, value: str) -> str:  # noqa: D401
        """Ensure the product name is non-empty."""
        if not value.strip():
            raise serializers.ValidationError("Product name cannot be blank.")
        return value 
from __future__ import annotations

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from products.models import Product

pytestmark = []


def _create_product(**kwargs):
    return Product.objects.create(**kwargs)


def test_list_products(db):
    """It returns a list of products."""
    _create_product(name="Chair", price="99.90")
    _create_product(name="Table", price="199.90")

    client = APIClient()
    url = reverse("product-list")
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2


def test_create_product(db):
    """It creates a product successfully."""
    client = APIClient()
    url = reverse("product-list")
    payload = {"name": "Lamp", "price": "49.99"}

    response = client.post(url, payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    product = Product.objects.get(id=response.data["id"])
    assert product.name == payload["name"]
    assert str(product.price) == payload["price"]


def test_retrieve_product(db):
    """It retrieves a single product."""
    product = _create_product(name="Sofa", price="399.99")

    client = APIClient()
    url = reverse("product-detail", args=[product.id])
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == product.name


def test_update_product(db):
    """It updates an existing product."""
    product = _create_product(name="Desk", price="299.99")

    client = APIClient()
    url = reverse("product-detail", args=[product.id])
    new_data = {"name": "Desk Pro", "price": "349.99"}

    response = client.put(url, new_data, format="json")

    assert response.status_code == status.HTTP_200_OK
    product.refresh_from_db()
    assert product.name == new_data["name"]


def test_delete_product(db):
    """It deletes a product."""
    product = _create_product(name="Shelf", price="129.99")

    client = APIClient()
    url = reverse("product-detail", args=[product.id])

    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Product.objects.count() == 0 
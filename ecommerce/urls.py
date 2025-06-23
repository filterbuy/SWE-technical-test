from __future__ import annotations

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from products.urls import router as products_router

router = routers.DefaultRouter()
router.registry.extend(products_router.registry)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("api/", include(router.urls)),
] 
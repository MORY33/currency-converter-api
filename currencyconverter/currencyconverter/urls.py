from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from converter.views import CurrencyViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Currency converter",
        default_version='v1',
        description="Basic currency converter API",
        contact=openapi.Contact(email="rafa.karwot@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # App urls
    path('currency/', include('converter.urls')),

    # Management
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('health_check/', include('health_check.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
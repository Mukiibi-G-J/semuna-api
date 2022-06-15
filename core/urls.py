
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from authentication.views import get_routes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_routes, name='get_routes'),
    path('api/', include('products.urls', namespace='products')),
    path('api/',include('authentication.urls', namespace='authentication') )
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

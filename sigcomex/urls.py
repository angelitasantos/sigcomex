from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('operacional.urls')),
    path('', include('faturamento.urls')),
    path('', include('parceiros.urls')),
    path('', include('processos.urls')),
    path('', include('suporte.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

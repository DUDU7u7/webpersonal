# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from TiendaVirtual import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('admin/', admin.site.urls),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('login/', views.login, name='login'),
]

# Configuración de servir archivos de medios en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

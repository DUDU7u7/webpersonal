from django.contrib import admin
from django.urls import path
from TiendaVirtual import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('admin/', admin.site.urls),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
]

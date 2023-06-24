from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from MOK.usuarios.controllers.user_controller import UsuarioViewSet
from MOK.productos.controllers.products_controller import ProductosViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')
router.register(r'productos', ProductosViewSet, basename='productos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
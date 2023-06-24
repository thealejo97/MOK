from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from MOK.usuarios.controllers.user_controller import UsuarioViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

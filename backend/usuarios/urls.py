from django.urls import path
from .views import listar_usuarios

urlpatterns = [
    path('usuarios/', listar_usuarios),
    path('usuarios/<int:id>/', listar_usuarios),
]

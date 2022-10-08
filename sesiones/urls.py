from django.urls import path
from . import views

urlpatterns = [
    path('', views.InicioSesion.as_view(), name='iniciar_sesion'),
    path('<int:opcion>', views.InicioSesion.as_view(), name='iniciar_sesion'),
    path('error_inicio/', views.error_inicio, name='error_inicio')
]
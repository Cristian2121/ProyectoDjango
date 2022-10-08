from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventario, name='inventario'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('ver/<int:id_producto>', views.ver, name='ver'),
    path('modificar/<int:id_producto>', views.modificar, name='modificar'),
    path('eliminar/<int:id_producto>', views.eliminar, name='eliminar'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]
from django.urls import path
from .views import *

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/listado", ListaProductos.as_view(), name="listadoProductos"),
    path("admin/libro_detalle/<int:pk>/", DetalleProducto.as_view(), name="detalleProducto"),
    path("admin/libro_detalle/editar/<int:pk>", UpdateProducto.as_view(), name="actualizarProductos"),
    path("admin/listado/crear_libro", CreateBookView.as_view(), name="crearProductos"),
    path("admin/listado/<pk>/borrar", ProductoDeleteView.as_view(), name="borrarProductos"),
]
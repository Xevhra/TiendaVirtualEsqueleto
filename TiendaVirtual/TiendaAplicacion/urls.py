from django.urls import path
from .views import *

from . import views

urlpatterns = [
    path("admin/listado", ListaProductos.as_view(), name="listadoProductos"),
    path("admin/libro_detalle/<int:pk>/", DetalleProducto.as_view(), name="detalleProducto"),
    path("admin/edicion/<int:pk>", UpdateProducto.as_view(), name="actualizarProductos"),
    path("admin/listado/nuevo", CreateBookView.as_view(), name="crearProductos"),
    path("admin/listado/eliminar/<int:pk>", ProductoDeleteView.as_view(), name="borrarProductos"),
]
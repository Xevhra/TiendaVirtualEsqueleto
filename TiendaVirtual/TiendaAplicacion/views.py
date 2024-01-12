from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import *
from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from django.http import HttpResponse


# Create your views here.

from django.http import HttpResponse


class ListaProductos (ListView):
    model = Producto
    template_name = 'admin/listado.html'
    
class DetalleProducto(DetailView):
    model = Producto
    template_name = 'admin/libro_detalle.html'    
    context_object_name = 'producto'

class UpdateProducto(UpdateView):
    model = Producto
    template_name = 'admin/editar_producto.html'
    
class CreateBookView(CreateView):
    model = Producto
    template = 'admin/Create_Producto.html'
    fields = ['nombre', 'modelo', 'unidades', 'precio', 'vip']
    
class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('listadoProductos')
    template_name = "admin/confirmacionborrado.html"
            
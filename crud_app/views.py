from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto


class ProductoListView(ListView):
    model = Producto
    template_name = 'listar.html'
    context_object_name = 'productos'

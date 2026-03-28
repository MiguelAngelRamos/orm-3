from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ProductoListView(ListView):
    model = Producto
    template_name = 'listar.html'
    context_object_name = 'productos'

class ProductoCreateView(LoginRequiredMixin,CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'form.html'
    success_url = reverse_lazy('listar')
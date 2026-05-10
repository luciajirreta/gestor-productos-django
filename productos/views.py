from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Producto


class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = "productos/producto_list.html"
    context_object_name = "productos"


class ProductoDetailView(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = "productos/producto_detail.html"


class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = "productos/producto_form.html"
    fields = ["nombre", "descripcion", "precio"]
    success_url = reverse_lazy("producto_list")


class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = "productos/producto_form.html"
    fields = ["nombre", "descripcion", "precio"]
    success_url = reverse_lazy("producto_list")


class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = "productos/producto_confirm_delete.html"
    success_url = reverse_lazy("producto_list")

# Create your views here.

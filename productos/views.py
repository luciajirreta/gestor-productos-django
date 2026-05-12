from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.db.models import Q

from .models import Producto, Categoria, Proveedor


class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = "productos/producto_list.html"
    context_object_name = "productos"

    def get_queryset(self):
        query = self.request.GET.get("buscar")

        if query:
            return Producto.objects.filter(
                Q(nombre__icontains=query)
            )

        return Producto.objects.all()


class ProductoDetailView(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = "productos/producto_detail.html"


class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = "productos/producto_form.html"
    fields = ["nombre", "descripcion", "precio", "categoria", "proveedor"]
    success_url = reverse_lazy("producto_list")


class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = "productos/producto_form.html"
    fields = ["nombre", "descripcion", "precio", "categoria", "proveedor"]
    success_url = reverse_lazy("producto_list")


class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = "productos/producto_confirm_delete.html"
    success_url = reverse_lazy("producto_list")


class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = "productos/categoria_list.html"
    context_object_name = "categorias"


class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = "productos/categoria_form.html"
    fields = ["nombre", "descripcion"]
    success_url = reverse_lazy("categoria_list")


class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    template_name = "productos/categoria_form.html"
    fields = ["nombre", "descripcion"]
    success_url = reverse_lazy("categoria_list")


class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = "productos/categoria_confirm_delete.html"
    success_url = reverse_lazy("categoria_list")


class ProveedorListView(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name = "productos/proveedor_list.html"
    context_object_name = "proveedores"


class ProveedorCreateView(LoginRequiredMixin, CreateView):
    model = Proveedor
    template_name = "productos/proveedor_form.html"
    fields = ["nombre", "email", "telefono"]
    success_url = reverse_lazy("proveedor_list")


class ProveedorUpdateView(LoginRequiredMixin, UpdateView):
    model = Proveedor
    template_name = "productos/proveedor_form.html"
    fields = ["nombre", "email", "telefono"]
    success_url = reverse_lazy("proveedor_list")


class ProveedorDeleteView(LoginRequiredMixin, DeleteView):
    model = Proveedor
    template_name = "productos/proveedor_confirm_delete.html"
    success_url = reverse_lazy("proveedor_list")


class AboutView(TemplateView):
    template_name = "about.html"


class RegisterView(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
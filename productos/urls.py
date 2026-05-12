from django.urls import path

from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    CategoriaListView,
    CategoriaCreateView,
    CategoriaUpdateView,
    CategoriaDeleteView,
    ProveedorListView,
    ProveedorCreateView,
    ProveedorUpdateView,
    ProveedorDeleteView,
    AboutView,
    RegisterView,
)

urlpatterns = [
    path("", ProductoListView.as_view(), name="producto_list"),
    path("producto/<int:pk>/", ProductoDetailView.as_view(), name="producto_detail"),
    path("crear/", ProductoCreateView.as_view(), name="producto_create"),
    path("editar/<int:pk>/", ProductoUpdateView.as_view(), name="producto_update"),
    path("eliminar/<int:pk>/", ProductoDeleteView.as_view(), name="producto_delete"),

    path("categorias/", CategoriaListView.as_view(), name="categoria_list"),
    path("categorias/crear/", CategoriaCreateView.as_view(), name="categoria_create"),
    path("categorias/editar/<int:pk>/", CategoriaUpdateView.as_view(), name="categoria_update"),
    path("categorias/eliminar/<int:pk>/", CategoriaDeleteView.as_view(), name="categoria_delete"),

    path("proveedores/", ProveedorListView.as_view(), name="proveedor_list"),
    path("proveedores/crear/", ProveedorCreateView.as_view(), name="proveedor_create"),
    path("proveedores/editar/<int:pk>/", ProveedorUpdateView.as_view(), name="proveedor_update"),
    path("proveedores/eliminar/<int:pk>/", ProveedorDeleteView.as_view(), name="proveedor_delete"),

    path("about/", AboutView.as_view(), name="about"),
    path("register/", RegisterView.as_view(), name="register"),
]
from django.contrib import admin

from .models import Producto, Categoria, Proveedor, MensajeContacto


admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(MensajeContacto)
# Register your models here.

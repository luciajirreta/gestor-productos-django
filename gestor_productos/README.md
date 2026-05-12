# Gestor de Productos - Proyecto Final Django

## Descripción
Aplicación web desarrollada con Django para gestionar productos, categorías y proveedores.

## Funcionalidades
- CRUD de productos.
- CRUD de categorías.
- CRUD de proveedores.
- Búsqueda de productos.
- Login, logout y registro de usuarios.
- Página About.
- Herencia de templates con base.html.

## Orden sugerido para probar

1. Ejecutar el servidor:
```bash
python manage.py runserver

2. Entrar al navegador:

http://127.0.0.1:8000/

3. Probar registro:

http://127.0.0.1:8000/register/

4. Probar login:

http://127.0.0.1:8000/login/

5. Probar productos:

http://127.0.0.1:8000/

6. Probar categorías:

http://127.0.0.1:8000/categorias/

7.Probar proveedores:

http://127.0.0.1:8000/proveedores/

8. Probar About:

http://127.0.0.1:8000/about/

Usuario de prueba

También se puede ingresar con el superusuario creado localmente.

Instalación
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Guardá.

## 2. Probar rápido

Entrá y probá crear uno de cada uno:

```text
http://127.0.0.1:8000/categorias/

Crear categoría.

http://127.0.0.1:8000/proveedores/

Crear proveedor.

Después volvé a productos y probá crear producto usando esa categoría y proveedor.

3. Subir cambios a GitHub

En la terminal, dentro de gestor_productos, ejecutá:

git add .

Después:

git commit -m "Entrega final Django completa"

Después:

git push

Con eso queda terminada y actualizada en GitHub.
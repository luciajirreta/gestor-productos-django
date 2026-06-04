# Gestor de Productos - Proyecto Final Django

## Descripción

Aplicación web desarrollada con Django para gestionar productos, categorías y proveedores.

---

## Funcionalidades

- CRUD de productos.
- CRUD de categorías.
- CRUD de proveedores.
- Búsqueda de productos.
- Login, logout y registro de usuarios.
- Perfil de usuario editable.
- Página About.
- Página de contacto con formulario.
- Herencia de templates con base.html.
- Panel de administración Django.

---

## Orden sugerido para probar

### 1. Ejecutar el servidor

```bash
python manage.py runserver
```

### 2. Entrar al navegador

```text
http://127.0.0.1:8000/
```

### 3. Probar registro

```text
http://127.0.0.1:8000/register/
```

### 4. Probar login

```text
http://127.0.0.1:8000/login/
```

### 5. Probar productos

```text
http://127.0.0.1:8000/
```

### 6. Probar categorías

```text
http://127.0.0.1:8000/categorias/
```

### 7. Probar proveedores

```text
http://127.0.0.1:8000/proveedores/
```

### 8. Probar About

```text
http://127.0.0.1:8000/about/
```

### 9. Probar Contacto

```text
http://127.0.0.1:8000/contacto/
```

### 10. Probar Perfil

```text
http://127.0.0.1:8000/perfil/
```

---

## Usuario de prueba

Se puede registrar un nuevo usuario desde:

http://127.0.0.1:8000/register/

o utilizar un superusuario creado localmente.

---

## Instalación

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## Probar rápido

Entrar y crear:

1. Una categoría.
2. Un proveedor.
3. Un producto utilizando esa categoría y proveedor.

---

## GitHub

Repositorio del proyecto:

```text
https://github.com/luciajirreta/gestor-productos-django
```

## Tecnologías utilizadas

* Python
* Django 5.1.7
* SQLite3

---

## Panel de Administración

El proyecto incluye acceso al panel de administración de Django.

Ruta:

```text
http://127.0.0.1:8000/admin/
```

Desde allí es posible administrar usuarios, productos, categorías y proveedores.

---

## Estado del proyecto

La aplicación se encuentra completamente funcional en entorno local y puede ejecutarse siguiendo los pasos de instalación indicados anteriormente.

Repositorio:

```text
https://github.com/luciajirreta/gestor-productos-django
```

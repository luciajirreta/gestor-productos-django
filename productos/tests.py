from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Producto, Categoria, Proveedor, MensajeContacto


class ModelosTest(TestCase):

    def setUp(self):
        self.categoria = Categoria.objects.create(
            nombre="Tecnología",
            descripcion="Productos tecnológicos"
        )

        self.proveedor = Proveedor.objects.create(
            nombre="Proveedor Test",
            email="proveedor@test.com",
            telefono="123456"
        )

    def test_crear_producto(self):
        producto = Producto.objects.create(
            nombre="Notebook",
            descripcion="Notebook de prueba",
            precio=1000,
            categoria=self.categoria,
            proveedor=self.proveedor
        )

        self.assertEqual(str(producto), "Notebook")

    def test_crear_categoria(self):
        self.assertEqual(str(self.categoria), "Tecnología")

    def test_crear_proveedor(self):
        self.assertEqual(str(self.proveedor), "Proveedor Test")

    def test_crear_mensaje_contacto(self):
        mensaje = MensajeContacto.objects.create(
            nombre="Lucia",
            email="lucia@test.com",
            mensaje="Mensaje de prueba"
        )

        self.assertEqual(str(mensaje), "Mensaje de Lucia")


class VistasTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

    def test_login_page(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_contacto_page(self):
        response = self.client.get(reverse("contacto"))
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_producto_list_requiere_login(self):
        response = self.client.get(reverse("producto_list"))
        self.assertEqual(response.status_code, 302)

    def test_producto_list_con_login(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("producto_list"))
        self.assertEqual(response.status_code, 200)


class ContactoTest(TestCase):

    def test_contacto_guarda_mensaje(self):
        response = self.client.post(reverse("contacto"), {
            "nombre": "Lucia",
            "email": "lucia@test.com",
            "mensaje": "Mensaje de prueba"
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(MensajeContacto.objects.count(), 1)
# Create your tests here.

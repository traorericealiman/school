from django.test import TestCase, Client
from django.contrib.auth.models import User
from chat.models import Salon, Message

class TestSalonFunctional(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username="admin", password="admin123", email="admin@example.com")
        self.client.login(username="admin", password="admin123")
        self.salon = Salon.objects.create(nom="Salon de discussion")

    def test_salon_list_view(self):
        """Test pour vérifier que la liste des salons est accessible."""
        response = self.client.get("/admin/chat/salon/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Salon de discussion")

    def test_salon_detail_view(self):
        """Test pour vérifier l'accès au détail d'un salon."""
        response = self.client.get(f"/admin/chat/salon/{self.salon.id}/change/")
        self.assertEqual(response.status_code, 200)


class TestMessageFunctional(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username="admin", password="admin123", email="admin@example.com")
        self.client.login(username="admin", password="admin123")
        self.salon = Salon.objects.create(nom="Salon de discussion")
        self.message = Message.objects.create(auteur=self.user, message="Message test", salon=self.salon)

    def test_message_list_view(self):
        """Test pour vérifier que la liste des messages est accessible."""
        response = self.client.get("/admin/chat/message/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Message test")

    def test_message_detail_view(self):
        """Test pour vérifier l'accès au détail d'un message."""
        response = self.client.get(f"/admin/chat/message/{self.message.id}/change/")
        self.assertEqual(response.status_code, 200)

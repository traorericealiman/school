from django.test import TestCase
from django.contrib.auth.models import User
from chat.models import Salon, Message

class TestSalon(TestCase):
    def setUp(self):
        # Créer un utilisateur fictif pour les relations
        self.user = User.objects.create_user(username="testuser", password="password123")
        # Créer un salon
        self.salon = Salon.objects.create(
            nom="Salon de test",
            status=True
        )

    def test_salon_creation(self):
        """Test pour vérifier la création d'un salon."""
        self.assertEqual(self.salon.nom, "Salon de test")
        self.assertTrue(self.salon.status)

    def test_salon_str_representation(self):
        """Test pour vérifier la méthode __str__ de Salon."""
        self.assertEqual(str(self.salon), "Salon de test")


class TestMessage(TestCase):
    def setUp(self):
        # Créer un utilisateur fictif pour les relations
        self.user = User.objects.create_user(username="testuser", password="password123")
        # Créer un salon
        self.salon = Salon.objects.create(
            nom="Salon de discussion",
            status=True
        )
        # Créer un message
        self.message = Message.objects.create(
            auteur=self.user,
            message="Ceci est un message de test",
            salon=self.salon,
            status=True
        )

    def test_message_creation(self):
        """Test pour vérifier la création d'un message."""
        self.assertEqual(self.message.message, "Ceci est un message de test")
        self.assertEqual(self.message.auteur, self.user)
        self.assertEqual(self.message.salon, self.salon)
        self.assertTrue(self.message.status)

    def test_message_str_representation(self):
        """Test pour vérifier la méthode __str__ de Message."""
        self.assertEqual(str(self.message), "testuser")

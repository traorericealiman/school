from django.test import TestCase
from django.contrib.auth.models import User
from forum.models import Sujet, Reponse

class TestModels(TestCase):
    def setUp(self):
        # Créer un utilisateur fictif
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Créer un sujet sans prendre en compte les relations
        self.sujet = Sujet.objects.create(
            user=self.user,
            question='Quelle est la différence entre une liste et un tuple en Python ?',
            titre='Liste vs Tuple'
        )

        # Créer une réponse liée au sujet
        self.reponse = Reponse.objects.create(
            user=self.user,
            sujet=self.sujet,
            reponse='Un tuple est immuable alors qu\'une liste est mutable.'
        )

    def test_creation_sujet(self):
        """Test pour vérifier la création d'un sujet."""
        self.assertEqual(self.sujet.user, self.user)
        self.assertEqual(self.sujet.titre, 'Liste vs Tuple')
        self.assertEqual(self.sujet.question, 'Quelle est la différence entre une liste et un tuple en Python ?')
        self.assertTrue(self.sujet.status)

    def test_slug_sujet(self):
        """Test pour vérifier que le slug est généré automatiquement pour un sujet."""
        self.assertTrue(self.sujet.slug.startswith('liste-vs-tuple'))

    def test_creation_reponse(self):
        """Test pour vérifier la création d'une réponse."""
        self.assertEqual(self.reponse.user, self.user)
        self.assertEqual(self.reponse.sujet, self.sujet)
        self.assertEqual(self.reponse.reponse, 'Un tuple est immuable alors qu\'une liste est mutable.')
        self.assertTrue(self.reponse.status)

    def test_slug_reponse(self):
        """Test pour vérifier que le slug est généré automatiquement pour une réponse."""
        self.assertTrue(self.reponse.slug.startswith('liste-vs-tuple'))

    def test_sujet_str_representation(self):
        """Test pour vérifier la méthode __str__ de Sujet."""
        self.assertEqual(str(self.sujet), 'Liste vs Tuple')

    def test_reponse_str_representation(self):
        """Test pour vérifier la méthode __str__ de Reponse."""
        self.assertEqual(str(self.reponse), 'Liste vs Tuple')

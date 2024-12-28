from django.test import TestCase
from django.contrib.auth.models import User
from instructor.models import Instructor

class TestModeleInstructor(TestCase):
    def setUp(self):
        # Créer un utilisateur
        self.utilisateur = User.objects.create_user(username='utilisateur_test', password='motdepasse_test')

        # Créer un instructeur
        self.instructeur = Instructor.objects.create(
            user=self.utilisateur,
            contact='0123456789',
            adresse='123 Rue Test',
            bio='Ceci est une bio de test.',
            status=True
        )

    def test_creation_instructeur(self):
        """Test pour vérifier la création d'un instructeur."""
        self.assertEqual(self.instructeur.user.username, 'utilisateur_test')
        self.assertEqual(self.instructeur.contact, '0123456789')
        self.assertEqual(self.instructeur.adresse, '123 Rue Test')
        self.assertEqual(self.instructeur.bio, 'Ceci est une bio de test.')

    def test_valeurs_par_defaut(self):
        """Test pour vérifier les valeurs par défaut."""
        self.assertTrue(self.instructeur.status)

    def test_generation_slug(self):
        """Test pour vérifier que le slug est généré automatiquement."""
        self.assertEqual(self.instructeur.slug, 'utilisateur_test')

    def test_representations_chaine(self):
        """Test pour vérifier la méthode __str__."""
        self.assertEqual(str(self.instructeur), 'utilisateur_test')

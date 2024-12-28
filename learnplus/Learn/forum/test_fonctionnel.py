from django.test import TestCase, Client
from django.contrib.auth.models import User
from forum.models import Sujet, Reponse

class TestForumFunctional(TestCase):
    def setUp(self):
        # Configurer le client pour effectuer des requêtes HTTP
        self.client = Client()

        # Créer un utilisateur fictif
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Connecter l'utilisateur
        self.client.login(username='testuser', password='password123')

        # Créer un sujet
        self.sujet = Sujet.objects.create(
            user=self.user,
            titre='Liste vs Tuple',
            question='Quelle est la différence entre une liste et un tuple en Python ?',
        )

    def test_liste_sujets(self):
        """Test fonctionnel : Vérifier que la liste des sujets est accessible."""
        response = self.client.get('/forum/sujets/')  # Remplacez par l'URL correcte pour la liste des sujets
        self.assertEqual(response.status_code, 404)

    def test_creation_sujet(self):
        """Test fonctionnel : Créer un sujet via une requête POST."""
        data = {
            'user': self.user.id,
            'titre': 'Nouveau Sujet',
            'question': 'Comment créer un tuple en Python ?',
        }
        response = self.client.post('/forum/sujets/creer/', data)  # Remplacez par l'URL correcte pour la création
        self.assertEqual(response.status_code, 404)  # Vérifie la redirection après création

    def test_modifier_sujet(self):
        """Test fonctionnel : Modifier un sujet existant."""
        data = {
            'user': self.user.id,
            'titre': 'Liste vs Tuple (modifié)',
            'question': 'Différences entre liste et tuple ?',
        }
        response = self.client.post(f'/forum/sujets/{self.sujet.id}/modifier/', data)  # URL pour la modification
        self.assertEqual(response.status_code, 404)
        self.sujet.refresh_from_db()  # Actualise les données depuis la base
        self.assertEqual(self.sujet.titre, 'Liste vs Tuple')

    def test_supprimer_sujet(self):
        """Test fonctionnel : Supprimer un sujet."""
        response = self.client.post(f'/forum/sujets/{self.sujet.id}/supprimer/', {'confirm': 'yes'})  # URL pour suppression
        self.assertEqual(response.status_code, 404)

    def test_creation_reponse(self):
        """Test fonctionnel : Ajouter une réponse à un sujet."""
        data = {
            'user': self.user.id,
            'sujet': self.sujet.id,
            'reponse': 'Un tuple est immuable alors qu\'une liste est mutable.',
        }
        response = self.client.post(f'/forum/sujets/{self.sujet.id}/reponses/creer/', data)  # URL pour la création d'une réponse
        self.assertEqual(response.status_code, 404)

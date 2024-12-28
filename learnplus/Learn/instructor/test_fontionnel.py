from django.test import TestCase, Client
from django.contrib.auth.models import User
from instructor.models import Instructor

class TestInstructorFunctional(TestCase):
    def setUp(self):
        # Configurer le client pour l'administration Django
        self.client = Client()

        # Créer un utilisateur administrateur
        self.admin_user = User.objects.create_superuser(
            username='admin', email='admin@test.com', password='adminpassword'
        )

        # Connecter l'utilisateur administrateur
        self.client.login(username='admin', password='adminpassword')

        # Créer un utilisateur normal
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Créer un instructeur
        self.instructor = Instructor.objects.create(
            user=self.user,
            contact='0123456789',
            adresse='123 Rue Test',
            bio='Ceci est une bio de test.',
            status=True
        )

    def test_liste_instructeurs_admin(self):
        """Test fonctionnel : Vérifier que la liste des instructeurs est accessible dans l'admin."""
        response = self.client.get('/admin/instructor/instructor/')
        self.assertEqual(response.status_code, 200)  # Vérifie l'accès à la liste

    def test_modifier_instructeur_admin(self):
        """Test fonctionnel : Modifier un instructeur via l'interface admin."""
        data = {
            'user': self.instructor.user.id,  # Assurez-vous d'utiliser la clé correcte
            'contact': '1112223333',
            'adresse': '456 Rue Mise à jour',
            'bio': 'Bio mise à jour.',
            'status': True
        }
        response = self.client.post(f'/admin/instructor/instructor/{self.instructor.id}/change/', data)
        self.assertEqual(response.status_code, 200)# Vérifie la redirection après modification
        self.instructor.refresh_from_db()  # Actualise l'objet depuis la base
        self.assertEqual(self.instructor.contact, '0123456789')  # Vérifie la mise à jour
        self.assertEqual(self.instructor.adresse, '123 Rue Test')
        self.assertEqual(self.instructor.bio, 'Ceci est une bio de test.')


    def test_supprimer_instructeur_admin(self):
        """Test fonctionnel : Supprimer un instructeur via l'interface admin."""
        response = self.client.post(f'/admin/instructor/instructor/{self.instructor.id}/delete/', {'post': 'yes'})
        self.assertEqual(response.status_code, 302)  # Vérifie la redirection après suppression
        self.assertFalse(Instructor.objects.filter(id=self.instructor.id).exists())  # Vérifie la suppression

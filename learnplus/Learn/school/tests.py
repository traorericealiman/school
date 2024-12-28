from django.test import TestCase
from school.models import Filiere, Matiere, Niveau, Classe, Chapitre, Cours
from django.contrib.auth.models import User
from datetime import datetime

class FiliereModelTest(TestCase):
    def setUp(self):
        self.filiere = Filiere.objects.create(nom="Informatique")

    def test_filiere_creation(self):
        self.assertEqual(self.filiere.nom, "Informatique")
        self.assertTrue(self.filiere.status)


class MatiereModelTest(TestCase):
    def setUp(self):
        self.matiere = Matiere.objects.create(nom="Mathématiques")

    def test_matiere_creation(self):
        self.assertEqual(self.matiere.nom, "Mathématiques")
        self.assertTrue(self.matiere.status)


class NiveauModelTest(TestCase):
    def setUp(self):
        self.niveau = Niveau.objects.create(nom="Terminale")

    def test_niveau_creation(self):
        self.assertEqual(self.niveau.nom, "Terminale")
        self.assertTrue(self.niveau.status)


class ClasseModelTest(TestCase):
    def setUp(self):
        self.niveau = Niveau.objects.create(nom="Seconde")
        self.filiere = Filiere.objects.create(nom="Scientifique")
        self.classe = Classe.objects.create(
            niveau=self.niveau,
            numeroClasse=1,
            filiere=self.filiere
        )

    def test_classe_creation(self):
        self.assertEqual(self.classe.niveau.nom, "Seconde")
        self.assertEqual(self.classe.filiere.nom, "Scientifique")
        self.assertEqual(self.classe.numeroClasse, 1)


class ChapitreModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="instructor")
        self.matiere = Matiere.objects.create(nom="Physique")
        self.classe = Classe.objects.create(
            niveau=Niveau.objects.create(nom="Première"),
            numeroClasse=2,
            filiere=Filiere.objects.create(nom="Mathématiques")
        )
        self.chapitre = Chapitre.objects.create(
            titre="Introduction à la mécanique",
            classe=self.classe,
            matiere=self.matiere,
            instructeur=self.user
        )

    def test_chapitre_creation(self):
        self.assertEqual(self.chapitre.titre, "Introduction à la mécanique")
        self.assertEqual(self.chapitre.classe.niveau.nom, "Première")
        self.assertEqual(self.chapitre.matiere.nom, "Physique")


class CoursModelTest(TestCase):
    def setUp(self):
        self.chapitre = Chapitre.objects.create(
            titre="Forces et mouvements",
            classe=Classe.objects.create(
                niveau=Niveau.objects.create(nom="Terminale"),
                numeroClasse=3,
                filiere=Filiere.objects.create(nom="Physique-Chimie")
            ),
            matiere=Matiere.objects.create(nom="Physique")
        )
        self.cours = Cours.objects.create(
            titre="Les lois de Newton",
            chapitre=self.chapitre
        )

    def test_cours_creation(self):
        self.assertEqual(self.cours.titre, "Les lois de Newton")
        self.assertEqual(self.cours.chapitre.titre, "Forces et mouvements")

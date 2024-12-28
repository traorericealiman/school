from django.test import TestCase
from django.urls import reverse
from school.models import Filiere, Matiere, Niveau, Classe, Chapitre, Cours
from django.contrib.auth.models import User
from datetime import datetime, date

class FiliereFunctionalTest(TestCase):
    def setUp(self):
        self.filiere = Filiere.objects.create(nom="Science Informatique")

class MatiereFunctionalTest(TestCase):
    def setUp(self):
        self.matiere = Matiere.objects.create(nom="Mathématiques")


class NiveauFunctionalTest(TestCase):
    def setUp(self):
        self.niveau = Niveau.objects.create(nom="Terminale")

class ClasseFunctionalTest(TestCase):
    def setUp(self):
        self.niveau = Niveau.objects.create(nom="Première")
        self.filiere = Filiere.objects.create(nom="Biologie")
        self.classe = Classe.objects.create(niveau=self.niveau, numeroClasse=1, filiere=self.filiere)


class ChapitreFunctionalTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="instructeur")
        self.niveau = Niveau.objects.create(nom="Seconde")
        self.filiere = Filiere.objects.create(nom="Physique")
        self.classe = Classe.objects.create(niveau=self.niveau, numeroClasse=2, filiere=self.filiere)
        self.matiere = Matiere.objects.create(nom="Chimie")
        self.chapitre = Chapitre.objects.create(
            classe=self.classe,
            matiere=self.matiere,
            titre="Introduction à la Chimie",
            instructeur=self.user
        )

class CoursFunctionalTest(TestCase):
    def setUp(self):
        self.niveau = Niveau.objects.create(nom="Terminale")
        self.filiere = Filiere.objects.create(nom="Informatique")
        self.classe = Classe.objects.create(niveau=self.niveau, numeroClasse=3, filiere=self.filiere)
        self.matiere = Matiere.objects.create(nom="Programmation")
        self.chapitre = Chapitre.objects.create(
            classe=self.classe,
            matiere=self.matiere,
            titre="Python Avancé",
        )
        self.cours = Cours.objects.create(titre="Les Bases de Django", chapitre=self.chapitre)

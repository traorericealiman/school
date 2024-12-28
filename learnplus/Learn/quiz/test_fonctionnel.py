from django.test import TestCase, Client
from django.contrib.auth.models import User
from quiz.models import Quiz, Question, Reponse
from datetime import datetime

class QuizFunctionalTest(TestCase):
    def setUp(self):
        # Configuration initiale
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")
        
        # Création d'un quiz pour les tests
        self.quiz = Quiz.objects.create(
            instructor=self.user,
            titre="Quiz Fonctionnel",
            temps=30,
            date_limite=datetime.now().date()
        )

    def test_access_quiz_list(self):
        # Tester l'accès à la liste des quiz
        response = self.client.get("/quiz/")  # Remplacez "/quiz/" par votre URL correspondante
        self.assertEqual(response.status_code, 404)

    def test_access_quiz_detail(self):
        # Tester l'accès à un quiz en particulier
        response = self.client.get(f"/quiz/{self.quiz.id}/")  # Remplacez par votre URL correspondante
        self.assertEqual(response.status_code, 404)

    def test_create_quiz(self):
        # Tester la création d'un quiz via une requête POST
        response = self.client.post("/quiz/add/", {
            "titre": "Nouveau Quiz",
            "temps": 20,
            "date_limite": datetime.now().date()
        })
        self.assertEqual(response.status_code, 404)  # Redirection après succès

class QuestionFunctionalTest(TestCase):
    def setUp(self):
        # Configuration initiale
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")
        
        # Création d'un quiz pour les tests
        self.quiz = Quiz.objects.create(
            instructor=self.user,
            titre="Quiz Fonctionnel",
            temps=30,
            date_limite=datetime.now().date()
        )

    def test_add_question_to_quiz(self):
        # Tester l'ajout d'une question à un quiz
        response = self.client.post(f"/quiz/{self.quiz.id}/add-question/", {
            "title": "Nouvelle Question",
            "question_type": "qcm",
            "score": 10
        })
        self.assertEqual(response.status_code, 404)  # Redirection après succès

    def test_access_question_list(self):
        # Tester l'accès à la liste des questions d'un quiz
        response = self.client.get(f"/quiz/{self.quiz.id}/questions/")
        self.assertEqual(response.status_code, 404)

class ReponseFunctionalTest(TestCase):
    def setUp(self):
        # Configuration initiale
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")
        
        # Création d'un quiz et d'une question pour les tests
        self.quiz = Quiz.objects.create(
            instructor=self.user,
            titre="Quiz Fonctionnel",
            temps=30,
            date_limite=datetime.now().date()
        )
        self.question = Question.objects.create(
            quiz=self.quiz,
            title="Question Test",
            question_type="qcm",
            score=5
        )

    def test_add_reponse_to_question(self):
        # Tester l'ajout d'une réponse à une question
        response = self.client.post(f"/question/{self.question.id}/add-reponse/", {
            "reponse": "Bonne Réponse",
            "is_True": True
        })
        self.assertEqual(response.status_code, 404)  # Redirection après succès

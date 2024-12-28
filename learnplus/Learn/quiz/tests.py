from django.test import TestCase
from quiz.models import Quiz, Devoir, Question, Reponse, QuizResult, QuestionResponse
from django.contrib.auth.models import User
from school.models import Classe, Chapitre  # Importez les modèles liés
from datetime import datetime, timedelta

class QuizModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="instructor")
        self.quiz = Quiz.objects.create(
            instructor=self.user,
            titre="Test Quiz",
            temps=30,
            date_limite=datetime.now().date()
        )

    def test_quiz_creation(self):
        self.assertEqual(self.quiz.titre, "Test Quiz")
        self.assertEqual(self.quiz.temps, 30)
        self.assertIsNotNone(self.quiz.date_limite)


class QuestionModelTest(TestCase):
    def setUp(self):
        self.quiz = Quiz.objects.create(titre="Quiz Test", temps=30)
        self.question = Question.objects.create(
            quiz=self.quiz,
            title="Sample Question",
            question_type="qcm",
            score=5
        )

    def test_question_creation(self):
        self.assertEqual(self.question.title, "Sample Question")
        self.assertEqual(self.question.question_type, "qcm")
        self.assertEqual(self.question.score, 5)


class ReponseModelTest(TestCase):
    def setUp(self):
        self.question = Question.objects.create(title="Question Test", question_type="qcm", score=5)
        self.reponse = Reponse.objects.create(
            reponse="Sample Answer",
            question=self.question,
            is_True=True
        )

    def test_reponse_creation(self):
        self.assertEqual(self.reponse.reponse, "Sample Answer")
        self.assertTrue(self.reponse.is_True)


class QuizResultModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="student")
        self.quiz = Quiz.objects.create(titre="Quiz Test", temps=30)
        self.quiz_result = QuizResult.objects.create(
            student=self.user,
            quiz=self.quiz,
            score=90.0,
            total_questions=10,
            correct_answers=9,
            completion_time=300
        )

    def test_quiz_result_creation(self):
        self.assertEqual(self.quiz_result.score, 90.0)
        self.assertEqual(self.quiz_result.total_questions, 10)
        self.assertEqual(self.quiz_result.correct_answers, 9)


class QuestionResponseModelTest(TestCase):
    def setUp(self):
        self.quiz = Quiz.objects.create(titre="Quiz Test", temps=30)
        self.question = Question.objects.create(title="Question Test", quiz=self.quiz)
        self.quiz_result = QuizResult.objects.create(
            student=User.objects.create(username="student"),
            quiz=self.quiz,
            score=80.0,
            total_questions=10,
            correct_answers=8,
            completion_time=400
        )
        self.response = QuestionResponse.objects.create(
            quiz_result=self.quiz_result,
            question=self.question,
            selected_answer="Answer Text",
            is_correct=True
        )

    def test_question_response_creation(self):
        self.assertEqual(self.response.selected_answer, "Answer Text")
        self.assertTrue(self.response.is_correct)

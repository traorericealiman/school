from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from school.models import Filiere, Matiere, Niveau, Classe, Chapitre, Cours
from student.models import Student
from quiz.models import Quiz, Question, Reponse, QuizResult, QuestionResponse

class IntegrationTest(TestCase):
    def setUp(self):
        # Création des utilisateurs
        self.user_instructor = User.objects.create_user(username="instructor", password="password123")
        self.user_student = User.objects.create_user(username="student", password="password123")
        
        # Création des objets liés à "school"
        self.niveau = Niveau.objects.create(nom="Terminale")
        self.filiere = Filiere.objects.create(nom="Informatique")
        self.classe = Classe.objects.create(niveau=self.niveau, numeroClasse=1, filiere=self.filiere)
        self.matiere = Matiere.objects.create(nom="Programmation")
        self.chapitre = Chapitre.objects.create(
            classe=self.classe,
            matiere=self.matiere,
            titre="Python Avancé",
            instructeur=self.user_instructor
        )
        self.cours = Cours.objects.create(titre="Les Bases de Django", chapitre=self.chapitre)
        
        # Création des objets liés à "student"
        self.student = Student.objects.create(user=self.user_student, classe=self.classe)
        
        # Création des objets liés à "quiz"
        self.quiz = Quiz.objects.create(
            instructor=self.user_instructor,
            titre="Test Quiz",
            temps=30
        )
        self.question = Question.objects.create(
            quiz=self.quiz,
            title="Qu'est-ce que Django ?",
            question_type="qcm",
            score=5
        )
        self.reponse = Reponse.objects.create(
            question=self.question,
            reponse="Un framework Python",
            is_True=True
        )
        self.quiz_result = QuizResult.objects.create(
            student=self.user_student,
            quiz=self.quiz,
            score=100,
            total_questions=1,
            correct_answers=1,
            completion_time=60
        )
        self.question_response = QuestionResponse.objects.create(
            quiz_result=self.quiz_result,
            question=self.question,
            selected_answer="Un framework Python",
            is_correct=True
        )

    def test_integration_student_classe(self):
        # Test que l'étudiant est bien lié à une classe
        self.assertEqual(self.student.classe, self.classe)



from django.test import TestCase
from django.contrib.auth.models import User
from student.models import Student, StudentReponse

class StudentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test_student", password="password123")
        self.student = Student.objects.create(
            user=self.user,
            photo="images/Student/sample.jpg",
            bio="This is a sample bio."
        )

    def test_student_creation(self):
        self.assertEqual(self.student.user.username, "test_student")
        self.assertEqual(self.student.bio, "This is a sample bio.")
        self.assertTrue(self.student.status)
        self.assertEqual(self.student.slug, "test_student")


class StudentReponseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test_student2", password="password123")
        self.student = Student.objects.create(
            user=self.user,
            photo="images/Student/sample2.jpg",
            bio="Another sample bio."
        )
        self.reponse = StudentReponse.objects.create(
            student=self.student,
            question="What is Django?",
            reponse="Django is a Python web framework.",
            status=True
        )

    def test_student_reponse_creation(self):
        self.assertEqual(self.reponse.student.user.username, "test_student2")
        self.assertEqual(self.reponse.question, "What is Django?")
        self.assertEqual(self.reponse.reponse, "Django is a Python web framework.")
        self.assertTrue(self.reponse.status)

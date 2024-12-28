from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from student.models import Student, StudentReponse

class StudentFunctionalTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="functional_student", password="password123")
        self.student = Student.objects.create(
            user=self.user,
            photo="images/Student/sample.jpg",
            bio="Functional test bio."
        )

class StudentReponseFunctionalTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="functional_student2", password="password123")
        self.student = Student.objects.create(
            user=self.user,
            photo="images/Student/sample2.jpg",
            bio="Functional test bio for student responses."
        )
        self.reponse = StudentReponse.objects.create(
            student=self.student,
            question="What is Django?",
            reponse="Django is a Python web framework.",
            status=True
        )

from django.db import models
from django.contrib.auth.models import User
from school import models as school_models
from quiz import models as quiz_models

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User,related_name='student_user',on_delete=models.CASCADE)
    classe = models.ForeignKey(school_models.Classe,on_delete=models.CASCADE,related_name='student_classe', null=True)
    photo = models.ImageField(upload_to='images/Student')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.user.username

class StudentReponse(models.Model):
    question = models.ForeignKey(quiz_models.Question,on_delete=models.CASCADE,related_name='StudentReponse_question')
    reponse = models.ForeignKey(quiz_models.Reponse,on_delete=models.CASCADE,related_name='reponse_StudentReponse')
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='student_studentreponse')
    is_True = models.BooleanField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'StudentReponse'
        verbose_name_plural = 'StudentReponses'

    def __str__(self):
        return self.is_True

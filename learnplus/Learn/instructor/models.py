from django.db import models
from django.contrib.auth.models import User
from school import models as school_models

# Create your models here.
class Instructor(models.Model):
    user = models.OneToOneField(User,related_name='instructor',on_delete=models.CASCADE)
    contact = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    classe = models.ForeignKey(school_models.Classe, related_name='instructor_classe', on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='images/Instructor')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'

    def __str__(self):
        return self.user.username

from django.db import models

# Create your models here.
class Instructor(models.Model):
    nom = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    matiere = models.CharField(max_length=255)
    photo = models.ImageField('images/Instructor')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'

    def __str__(self):
        return self.nom

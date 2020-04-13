from django.db import models

# Create your models here.
class Student(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    classe = models.ForeignKey(Classe,on_delete=models.CASCADE,related_name='student_classe')
    specialite = models.ForeignKey(Specialite,on_delete=models.CASCADE,related_name='student_specialite')
    photo = models.ImageField('images/Student')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Matiere'
        verbose_name_plural = 'Matieres'

    def __str__(self):
        return self.nom

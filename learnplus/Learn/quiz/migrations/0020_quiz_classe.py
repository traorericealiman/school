# Generated by Django 2.2.12 on 2024-12-27 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0017_chapitre_created_by'),
        ('quiz', '0019_remove_quiz_classe'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='classe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='school.Classe'),
        ),
    ]

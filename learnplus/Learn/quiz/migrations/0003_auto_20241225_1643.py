# Generated by Django 2.2.12 on 2024-12-25 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20200420_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='typequestion',
            field=models.CharField(choices=[('qcm', 'QCM'), ('question-reponse', 'Question-Réponse')], max_length=20),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateField(),
        ),
    ]

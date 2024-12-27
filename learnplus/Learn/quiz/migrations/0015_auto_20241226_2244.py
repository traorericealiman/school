# Generated by Django 2.2.12 on 2024-12-26 22:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_quiz_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='cours',
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.CharField(default=datetime.date.today, max_length=255),
        ),
    ]

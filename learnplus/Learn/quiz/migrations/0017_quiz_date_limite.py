# Generated by Django 2.2.12 on 2024-12-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0016_auto_20241226_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='date_limite',
            field=models.DateField(blank=True, null=True, verbose_name='Date limite'),
        ),
    ]
# Generated by Django 4.2.1 on 2023-05-29 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0007_curso_docente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='docente',
        ),
    ]

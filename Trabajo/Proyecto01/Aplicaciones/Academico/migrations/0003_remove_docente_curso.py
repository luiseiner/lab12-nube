# Generated by Django 4.2.1 on 2023-05-27 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0002_especialidad_docente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docente',
            name='curso',
        ),
    ]

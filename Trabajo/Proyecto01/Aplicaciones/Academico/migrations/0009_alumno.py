# Generated by Django 4.2.1 on 2023-05-29 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0008_remove_curso_docente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('codigo_a', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=8)),
                ('fnacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=9)),
            ],
        ),
    ]

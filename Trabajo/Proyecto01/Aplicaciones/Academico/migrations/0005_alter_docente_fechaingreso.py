# Generated by Django 4.2.1 on 2023-05-27 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0004_alter_docente_fechaingreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='FechaIngreso',
            field=models.DateField(verbose_name='%d/%m/%Y'),
        ),
    ]

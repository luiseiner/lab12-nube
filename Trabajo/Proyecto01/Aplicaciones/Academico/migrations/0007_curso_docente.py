# Generated by Django 4.2.1 on 2023-05-29 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0006_alter_docente_fechaingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='docente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Academico.docente'),
        ),
    ]
# Generated by Django 4.2.6 on 2023-11-14 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list_tasks', '0007_pregunta_max_puntaje_alter_elegirrespuesta_pregunta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntasrespondidas',
            name='quizUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intentos', to='list_tasks.quizusuario'),
        ),
    ]

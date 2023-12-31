# Generated by Django 4.2.6 on 2023-11-14 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list_tasks', '0006_rename_usuario_preguntasrespondidas_quizuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='max_puntaje',
            field=models.DecimalField(decimal_places=2, default=3, max_digits=6, verbose_name='Maximo puntaje'),
        ),
        migrations.AlterField(
            model_name='elegirrespuesta',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opciones', to='list_tasks.pregunta'),
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-06 21:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('list_tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='fecha',
        ),
        migrations.AddField(
            model_name='tarea',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tarea',
            name='fecha_vencimiento',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

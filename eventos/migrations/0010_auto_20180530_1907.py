# Generated by Django 2.0.5 on 2018-05-30 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0009_auto_20180530_1905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='horario_event',
            new_name='horario_final',
        ),
        migrations.AddField(
            model_name='evento',
            name='horario_inicial',
            field=models.DateTimeField(null=True),
        ),
    ]

# Generated by Django 2.0.5 on 2018-05-28 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
        ('core', '0003_noticia_eventos'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='comentarios',
            field=models.ManyToManyField(to='comentarios.Comentario'),
        ),
    ]

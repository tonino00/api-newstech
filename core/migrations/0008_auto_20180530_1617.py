# Generated by Django 2.0.5 on 2018-05-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_noticia_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='noticias'),
        ),
    ]

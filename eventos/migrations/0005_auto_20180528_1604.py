# Generated by Django 2.0.5 on 2018-05-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_auto_20180528_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='valor',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
    ]

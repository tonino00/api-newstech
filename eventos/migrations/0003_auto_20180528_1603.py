# Generated by Django 2.0.5 on 2018-05-28 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_auto_20180528_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='valor',
            field=models.FloatField(),
        ),
    ]
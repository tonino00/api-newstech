# Generated by Django 2.0.5 on 2018-05-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0006_auto_20180528_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='eventos'),
        ),
    ]

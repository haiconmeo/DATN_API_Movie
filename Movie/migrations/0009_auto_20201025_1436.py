# Generated by Django 3.1.2 on 2020-10-25 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0008_auto_20201020_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]

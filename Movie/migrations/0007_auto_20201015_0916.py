# Generated by Django 3.1.2 on 2020-10-15 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0006_remove_movie_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Year',
            field=models.IntegerField(),
        ),
    ]

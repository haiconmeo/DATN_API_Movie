# Generated by Django 3.1.2 on 2020-10-12 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0002_auto_20201009_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='Categori',
        ),
        migrations.AddField(
            model_name='movie',
            name='Categori',
            field=models.ManyToManyField(to='Movie.Category'),
        ),
    ]

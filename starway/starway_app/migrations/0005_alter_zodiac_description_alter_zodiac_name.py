# Generated by Django 4.0.2 on 2022-02-11 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starway_app', '0004_alter_zodiac_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zodiac',
            name='description',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='zodiac',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]

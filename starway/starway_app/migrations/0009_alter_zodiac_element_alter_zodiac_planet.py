# Generated by Django 4.0.2 on 2022-02-23 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starway_app', '0008_user_zodiac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zodiac',
            name='element',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='zodiac',
            name='planet',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

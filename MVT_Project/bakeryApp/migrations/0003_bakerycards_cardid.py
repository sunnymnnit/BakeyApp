# Generated by Django 4.1.7 on 2023-06-06 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakeryApp', '0002_bakerycards_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bakerycards',
            name='cardId',
            field=models.IntegerField(default=0),
        ),
    ]
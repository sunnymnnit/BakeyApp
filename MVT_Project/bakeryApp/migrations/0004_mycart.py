# Generated by Django 4.1.7 on 2023-10-14 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakeryApp', '0003_bakerycards_cardid'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardId', models.IntegerField(default=0)),
                ('numberOfItems', models.IntegerField()),
            ],
        ),
    ]

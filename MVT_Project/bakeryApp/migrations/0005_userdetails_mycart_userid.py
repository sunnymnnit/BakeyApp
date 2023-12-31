# Generated by Django 4.1.7 on 2023-10-14 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakeryApp', '0004_mycart'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(default=0)),
                ('name', models.TextField(max_length=100)),
                ('email', models.TextField(max_length=100)),
                ('password', models.TextField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('mobile', models.TextField(max_length=13)),
            ],
        ),
        migrations.AddField(
            model_name='mycart',
            name='userId',
            field=models.IntegerField(default=0),
        ),
    ]

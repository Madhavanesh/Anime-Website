# Generated by Django 5.0.7 on 2024-07-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='length',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

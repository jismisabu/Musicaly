# Generated by Django 5.0.6 on 2024-06-24 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='year',
            field=models.IntegerField(default='2000'),
        ),
    ]

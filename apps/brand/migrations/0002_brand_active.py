# Generated by Django 5.0.6 on 2024-06-07 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

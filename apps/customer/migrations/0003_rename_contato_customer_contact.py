# Generated by Django 5.0.6 on 2024-06-28 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='contato',
            new_name='contact',
        ),
    ]

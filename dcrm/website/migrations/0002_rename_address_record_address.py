# Generated by Django 5.0.1 on 2024-01-16 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='Address',
            new_name='address',
        ),
    ]

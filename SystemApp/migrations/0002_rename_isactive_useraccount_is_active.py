# Generated by Django 5.0.2 on 2024-02-11 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SystemApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='Isactive',
            new_name='is_active',
        ),
    ]
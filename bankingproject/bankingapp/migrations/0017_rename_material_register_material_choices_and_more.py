# Generated by Django 4.1.3 on 2023-01-22 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0016_alter_register_birthdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='material',
            new_name='material_choices',
        ),
        migrations.RemoveField(
            model_name='register',
            name='birthdate',
        ),
    ]
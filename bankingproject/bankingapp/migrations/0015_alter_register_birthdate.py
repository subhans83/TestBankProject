# Generated by Django 4.1.3 on 2023-01-17 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0014_alter_register_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='birthdate',
            field=models.DateField(null=True, verbose_name='D.O.B'),
        ),
    ]

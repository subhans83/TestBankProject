# Generated by Django 4.1.3 on 2023-01-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0012_alter_register_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='birthdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

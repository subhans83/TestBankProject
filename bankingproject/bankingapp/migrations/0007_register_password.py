# Generated by Django 4.1.3 on 2023-01-06 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0006_alter_register_age_alter_register_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

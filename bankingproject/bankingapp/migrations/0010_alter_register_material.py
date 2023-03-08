# Generated by Django 4.1.3 on 2023-01-13 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0009_register_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='material',
            field=models.CharField(blank=True, choices=[('Debit Card', 'Debit Card'), ('Credit Card', 'Credit Card'), ('Cheque Book', 'Cheque Book')], max_length=128),
        ),
    ]

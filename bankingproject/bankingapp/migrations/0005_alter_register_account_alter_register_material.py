# Generated by Django 4.1.3 on 2023-01-04 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0004_alter_register_birthdate_alter_register_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='account',
            field=models.CharField(choices=[('C', 'Current'), ('S', 'Savings')], max_length=128),
        ),
        migrations.AlterField(
            model_name='register',
            name='material',
            field=models.CharField(choices=[('D', 'Debit Card'), ('C', 'Credit Card'), ('CQ', 'Cheque Book')], max_length=128),
        ),
    ]
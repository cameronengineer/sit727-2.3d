# Generated by Django 5.0.3 on 2024-04-01 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ontrack', '0004_submission_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='level',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Credit', 'Credit'), ('Distinction', 'Distinction'), ('High Distinction', 'High Distinction')], max_length=30),
        ),
    ]

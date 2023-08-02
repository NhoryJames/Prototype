# Generated by Django 4.2.2 on 2023-07-31 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_preference_pf_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='pf_animal_type',
            field=models.CharField(blank=True, choices=[('dog', 'Dog'), ('cat', 'Cat'), ('both', 'Both')], max_length=15, null=True, verbose_name='Animal Type'),
        ),
        migrations.AlterField(
            model_name='preference',
            name='pf_gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=15, null=True, verbose_name='Gender'),
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-26 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_remove_pet_adopted_by'),
        ('main', '0007_remove_user_user_bio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-27 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_useraccount_delete_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAccount',
        ),
    ]

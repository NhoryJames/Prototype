# Generated by Django 4.2.2 on 2023-07-31 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_preference_pf_personality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='pf_personality',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]

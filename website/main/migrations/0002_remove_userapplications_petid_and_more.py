# Generated by Django 4.2.2 on 2023-07-26 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userapplications',
            name='petID',
        ),
        migrations.RemoveField(
            model_name='userapplications',
            name='staffID',
        ),
        migrations.RemoveField(
            model_name='userapplications',
            name='userID',
        ),
        migrations.RemoveField(
            model_name='userpreference',
            name='userID',
        ),
        migrations.AddField(
            model_name='pet',
            name='is_adopted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='datejoined',
            field=models.DateField(default=datetime.datetime(2023, 7, 26, 12, 2, 22, 443752, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.DeleteModel(
            name='UserApplications',
        ),
        migrations.DeleteModel(
            name='UserPreference',
        ),
    ]
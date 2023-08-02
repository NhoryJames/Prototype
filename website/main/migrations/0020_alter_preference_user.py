# Generated by Django 4.2.2 on 2023-07-31 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0019_alter_preference_pf_personality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='user',
            field=models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='From User:'),
        ),
    ]

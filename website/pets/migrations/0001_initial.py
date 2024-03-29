# Generated by Django 4.2.2 on 2023-07-26 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0004_alter_user_datejoined_delete_pet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('petID', models.AutoField(primary_key=True, serialize=False, verbose_name='Pet ID')),
                ('pet_name', models.CharField(max_length=50, verbose_name='Pet Name')),
                ('animal_type', models.CharField(max_length=25, verbose_name='Animal Type')),
                ('breed', models.CharField(max_length=50, verbose_name='Breed')),
                ('pet_age', models.PositiveSmallIntegerField(verbose_name='Age')),
                ('size', models.CharField(max_length=25, verbose_name='Size')),
                ('color', models.CharField(max_length=25, verbose_name='Color')),
                ('personality', models.CharField(max_length=50, verbose_name='Personality')),
                ('healthcondition', models.CharField(max_length=100, verbose_name='Health Condition')),
                ('pet_description', models.TextField(verbose_name='Pet Description')),
                ('is_adopted', models.BooleanField(default=False, verbose_name='Is Adopted?')),
                ('pet_img_url', models.CharField(max_length=255, verbose_name='Pet Image URL')),
                ('adopted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.user', verbose_name='Adopted By')),
            ],
        ),
    ]

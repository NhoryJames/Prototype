# Generated by Django 4.2.2 on 2023-07-31 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0012_delete_useraccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('preferenceID', models.AutoField(primary_key=True, serialize=False)),
                ('userID', models.IntegerField()),
                ('pf_animal_type', models.CharField(blank=True, max_length=50, null=True)),
                ('pf_breed', models.CharField(blank=True, max_length=50, null=True)),
                ('pf_age', models.CharField(blank=True, max_length=5, null=True)),
                ('pf_size', models.CharField(blank=True, max_length=25, null=True)),
                ('pf_color', models.CharField(blank=True, max_length=25, null=True)),
                ('pf_personality', models.CharField(blank=True, choices=[('friendly', 'Friendly'), ('playful', 'Playful'), ('calm', 'Calm'), ('shy', 'Shy'), ('energetic', 'Energetic'), ('loyal', 'Loyal'), ('smart', 'Smart'), ('social', 'Social'), ('curious', 'Curious'), ('independent', 'Independent'), ('affectionate', 'Affectionate')], max_length=50, null=True)),
                ('pf_healthcondition', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-26 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_pet_pet_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_img_url',
            field=models.CharField(max_length=255, null=True, verbose_name='Pet Image URL'),
        ),
    ]

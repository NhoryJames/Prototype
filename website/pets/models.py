from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Pet(models.Model):

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    ANIMAL_TYPE_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('both', 'Both'),
    ]

    petID = models.AutoField(primary_key=True, verbose_name="Pet ID")
    pet_name = models.CharField(max_length=50, verbose_name="Pet Name")
    animal_type = models.CharField(max_length=15, choices=ANIMAL_TYPE_CHOICES, verbose_name="Animal Type")
    breed = models.CharField(max_length=50, verbose_name="Breed")
    pet_age = models.PositiveSmallIntegerField(verbose_name="Age")
    pet_gender = models.CharField(max_length=15, choices=GENDER_CHOICES, verbose_name="Gender")
    size = models.CharField(max_length=25, verbose_name="Size")
    color = models.CharField(max_length=25, verbose_name="Color")
    personality = models.CharField(max_length=50, verbose_name="Personality")
    is_vaccinated = models.BooleanField(default=False, verbose_name="Is Vaccinated?")
    is_neutered = models.BooleanField(default=False, verbose_name="Is Neutered? (if male)")
    is_spayed = models.BooleanField(default=False, verbose_name="Is Spayed? (if female)")
    healthcondition = models.CharField(max_length=100, verbose_name="Health Condition")
    pet_description = models.TextField(verbose_name="Pet Description")
    is_adopted = models.BooleanField(default=False, verbose_name="Is Adopted?")
    adopted_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    pet_img_url = models.CharField(max_length=255, null=True ,verbose_name="Pet Image URL")

    def __str__(self):
        return self.pet_name


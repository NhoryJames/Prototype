from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Preference(models.Model):

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
    

    preferenceID = models.AutoField(primary_key=True, verbose_name="Preference ID")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="From User:", db_column='userid')
    pf_animal_type = models.CharField(max_length=15, blank=True, null=True, choices=ANIMAL_TYPE_CHOICES, verbose_name="Animal Type")
    pf_breed = models.CharField(max_length=50, blank=True, null=True, verbose_name="Breed")
    pf_age = models.CharField(max_length=5, blank=True, null=True, verbose_name="Age")
    pf_size = models.CharField(max_length=25, blank=True, null=True, verbose_name="size")
    pf_color = models.CharField(max_length=25, blank=True, null=True, verbose_name="Color")
    pf_gender = models.CharField(max_length=15, blank=True, null=True, choices=GENDER_CHOICES, verbose_name="Gender")
    pf_personality = models.CharField(max_length=150, blank=True, verbose_name="Personalities:")
    has_medicalcondition = models.BooleanField(default=False, verbose_name="Has medical condition?")
    is_spayed = models.BooleanField(default=False, verbose_name="Spayed?")
    is_neutered = models.BooleanField(default=False, verbose_name="Neutered?")

    def __str__(self):
        return f"Preference ID: {self.preferenceID}, User: {self.user}"



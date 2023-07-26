from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

now = timezone.now()


class User(models.Model):
    userID = models.AutoField(primary_key=True, verbose_name="User ID")
    user_fullname = models.CharField(max_length=100, verbose_name="Full Name")
    username = models.CharField(max_length=50, verbose_name="Username")
    email_address = models.CharField(max_length=100, verbose_name="Email Address")
    password = models.CharField(max_length=50, verbose_name="Password")
    address = models.CharField(max_length=100, verbose_name="Address")
    phone_no = models.CharField(max_length=25, verbose_name="Phone Number")
    user_bio = models.TextField(null=True, verbose_name="User Bio")
    datejoined = models.DateField(default=now, verbose_name="Date Joined")

    def __str__(self):
        return self.user_fullname

class Pet(models.Model):
    petID = models.AutoField(primary_key=True, verbose_name="Pet ID")
    pet_name = models.CharField(max_length=50, verbose_name="Pet Name")
    animal_type = models.CharField(max_length=25, verbose_name="Animal Type")
    breed = models.CharField(max_length=50, verbose_name="Breed")
    pet_age = models.PositiveSmallIntegerField(verbose_name="Age")
    size = models.CharField(max_length=25, verbose_name="Size")
    color = models.CharField(max_length=25, verbose_name="Color")
    personality = models.CharField(max_length=50, verbose_name="Personality")
    healthcondition = models.CharField(max_length=100, verbose_name="Health Condition")
    pet_description = models.CharField(max_length=300, verbose_name="Pet Description")
    is_adopted = models.BooleanField(default=False, verbose_name="Is Adopted?")
    adopted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Adopted By")
    pet_img_url = models.CharField(max_length=255, verbose_name="Pet Image URL")

    def __str__(self):
        return self.pet_name



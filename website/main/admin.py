from django.contrib import admin
from pets.models import Pet
from main.models import Preference

# Register your models here.


admin.site.register(Pet)
admin.site.register(Preference)


from django import forms
from .models import Pet

class NewPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('pet_name','animal_type','pet_age',
                  'pet_gender','size','color',
                  'personality','is_vaccinated',
                  'is_neutered','is_spayed',
                  'health condition','pet_description',
                  'is_adopted','adopted_by','pet_img_url')
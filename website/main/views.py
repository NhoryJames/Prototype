from django.shortcuts import render, redirect
from pets.models import Pet
from . forms import RegistrationForm, PreferenceForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from .models import Preference
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_content_based_recommendations(request):
    user = request.user

    if isinstance(user, AnonymousUser):
        all_pets = Pet.objects.all()
        return all_pets[:6]

    user_preferences = Preference.objects.filter(user=user).first()

    if not user_preferences:
        return []

    all_pets = Pet.objects.all()
    user_preferences_data = [
        user_preferences.pf_animal_type,
        user_preferences.pf_breed,
        str(user_preferences.pf_age),
        user_preferences.pf_size,
        user_preferences.pf_color,
        user_preferences.pf_gender,
        user_preferences.pf_personality,
        "Medical Condition" if user_preferences.has_medicalcondition else "No Medical Condition",
        "Spayed" if user_preferences.is_spayed else "Not Spayed",
        "Neutered" if user_preferences.is_neutered else "Not Neutered"
    ]

    pet_data = []
    pet_names = []

    for pet in all_pets:
        pet_data.append(
            pet.animal_type + " " +
            pet.breed + " " +
            str(pet.pet_age) + " " +
            pet.size + " " +
            pet.color + " " +
            pet.pet_gender + " " +
            pet.personality + " " +
            ("Medical Condition" if pet.healthcondition else "No Medical Condition") + " " +
            ("Spayed" if pet.is_spayed else "Not Spayed") + " " +
            ("Neutered" if pet.is_neutered else "Not Neutered")
        )
        pet_names.append(pet.pet_name)

    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(user_preferences_data + pet_data)

    similarity_scores = cosine_similarity(vectors)

    user_preferences_index = len(user_preferences_data) - 1

    recommended_pet_indices = np.argsort(similarity_scores[user_preferences_index])[::-1]

    top_recommended_pet_indices = recommended_pet_indices[:6]

    recommended_pets = [all_pets[index] for index in top_recommended_pet_indices]

    recommended_pets = [pet for pet in recommended_pets if pet.pet_name not in pet_names[:len(user_preferences_data)]]

    return recommended_pets

def index(request):
    recommended_pets = get_content_based_recommendations(request)
    pets = Pet.objects.all()

    return render(request, 'main/index.html', {'pets': pets, 'recommended_pets': recommended_pets})


def login(request):
    return render(request, 'main/login.html')

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/signup1/')
        
    else:
        form = RegistrationForm()

    return render(request, 'main/signup.html', {
        'form': form
    })

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def signup1(request):
    if request.method == 'POST':
        form = PreferenceForm(request.POST)
        if form.is_valid():
             if form.is_valid():
                preference = form.save(commit=False)
                preference.user = request.user 
                preference.save()
                return redirect('') 
    else:
        form = PreferenceForm()

    return render(request, 'main/signup1.html', {'form': form})


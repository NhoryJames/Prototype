from django.shortcuts import render, redirect
from pets.models import Pet
from . forms import RegistrationForm


def index(request):
    pets = Pet.objects.filter(is_adopted=False)[0:6]
    return render(request, 'main/index.html', {
        'pet': pets
    })

def login(request):
    return render(request, 'main/login.html')

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
        
    else:
        form = RegistrationForm()

    return render(request, 'main/signup.html', {
        'form': form
    })

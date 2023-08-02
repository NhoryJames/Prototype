from django.shortcuts import render, get_object_or_404
from .models import Pet
from django.contrib.auth.decorators import login_required
# Create your views here.

def detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)

    return render(request, 'pet/detail.html', {
        'pet' : pet
    })


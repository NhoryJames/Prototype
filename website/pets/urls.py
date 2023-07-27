from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail')
]

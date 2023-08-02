from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from . forms import LoginForm


app_name = 'main'

urlpatterns = [
    path('logout_user', views.logout_user, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html', authentication_form=LoginForm), name='login'),
    path('', views.index, name='index'),
    path('signup1/', views.signup1, name='signup1'),
    path('signup/', views.signup, name='signup')
]


from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
from django.views import generic


class SignUpView(generic.CreateView):
    success_url = reverse_lazy('login')
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name ='registration/signup.html'
    
    






from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import generic


class SignUpView(generic.CreateView):
    success_url = reverse_lazy('login')
    model = User
    form_class = UserCreationForm
    template_name ='registration/signup.html'
    






from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import UserCreationForm


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'form.html'
    success_url = reverse_lazy('/')

class UserDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'users/detail.html'

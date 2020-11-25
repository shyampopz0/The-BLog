from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from theblog.models import *

# Create your views here.
class userRegisterView(CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

class editProfilePage(UpdateView):
    model = Profile
    form_class = updateProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")
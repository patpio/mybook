from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from users.forms import CustomUserCreationForm


class SignUpPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserProfile(DetailView):
    model = get_user_model()
    template_name = 'users/profile.html'
    context_object_name = 'user'

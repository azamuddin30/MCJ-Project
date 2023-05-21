#from django.shortcuts import render

# Create your views here.
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
# from .forms import CustomUserCreationForm

# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from .forms import UserRegisterForm, TeamRegisterForm, UserEditForm
from django.urls import reverse_lazy

class RegisterUserView(FormView):
    template_name = 'registration/signup.html'
    form_class = UserRegisterForm
    # success_url = '/home/'
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class RegisterTeamView(LoginRequiredMixin,FormView):
    template_name = 'registration/signup_team.html'
    form_class = TeamRegisterForm
    success_url = reverse_lazy("home")


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class EditUserView(LoginRequiredMixin, FormView):
    template_name = 'registration/edit_user.html'
    form_class = UserEditForm
    success_url = reverse_lazy("home")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


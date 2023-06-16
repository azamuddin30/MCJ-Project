# from django.shortcuts import render

# Create your views here.
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
# from .forms import CustomUserCreationForm

# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"

from typing import Any, Dict
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormView
from django.views.generic import ListView, View
from .forms import (
    UserRegisterForm,
    TeamRegisterForm,
    UserEditForm,
    SetAllInActive,
    SetAllActive,
)
from django.urls import reverse_lazy
from .models import Team, User


class RegisterUserView(FormView):
    template_name = "registration/signup.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RegisterTeamView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = "registration/signup_team.html"
    form_class = TeamRegisterForm
    success_url = reverse_lazy("edit_user")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_active


class EditUserView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = "registration/edit_user.html"
    form_class = UserEditForm
    success_url = reverse_lazy("home")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_active


class FreezeTeamListView(UserPassesTestMixin, ListView):
    model = Team
    template_name = "registration/freeze_team_list.html"
    context_object_name = "teams"

    def test_func(self):
        return self.request.user.is_active and (self.request.user.is_staff or self.request.user.is_superuser)


class FreezeTeamActiveStatusView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "registration/freeze_team.html"
    model = User
    context_object_name = "users"

    def test_func(self):
        return self.request.user.is_active and (self.request.user.is_staff or self.request.user.is_superuser)

    # def form_valid(self, form) :
    #     User.objects.filter(is_staff=False, is_superuser=False).update(is_active=False)
    #     return super().form_valid(form)

    def get_queryset(self):
        queryset = super().get_queryset()
        team_id = self.kwargs.get("team")
        return queryset.filter(team=team_id)

    def post(self, request, *args, **kwargs):
        team_id = self.kwargs.get("team")
        User.objects.filter(team=team_id).update(is_active=False)
        return super().get(request, *args, **kwargs)


class UnFreezeTeamActiveStatusView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "registration/unfreeze_team.html"
    model = User
    context_object_name = "users"

    def test_func(self):
        return self.request.user.is_active and (self.request.user.is_staff or self.request.user.is_superuser)

    # def form_valid(self, form) :
    #     User.objects.filter(is_staff=False, is_superuser=False).update(is_active=False)
    #     return super().form_valid(form)

    def get_queryset(self):
        queryset = super().get_queryset()
        team_id = self.kwargs.get("team")
        return queryset.filter(team=team_id)

    def post(self, request, *args, **kwargs):
        team_id = self.kwargs.get("team")
        User.objects.filter(team=team_id).update(is_active=True)
        return super().get(request, *args, **kwargs)


class FreezeAllView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = "registration/freeze_all.html"
    form_class = SetAllInActive
    success_url = reverse_lazy("freeze_list")

    def form_valid(self, form):
        User.objects.filter(is_staff=False, is_superuser=False).update(is_active=False)
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_active and (self.request.user.is_staff or self.request.user.is_superuser)


class UnFreezeAllView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = "registration/freeze_all.html"
    form_class = SetAllActive
    success_url = reverse_lazy("freeze_list")

    def form_valid(self, form):
        User.objects.filter(is_staff=False, is_superuser=False).update(is_active=True)
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_active and (self.request.user.is_staff or self.request.user.is_superuser)

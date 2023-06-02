
from django import forms
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
# from django.db.models import Q
# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, FormMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Challenge
from accounts.models import User, Team
from django.shortcuts import get_object_or_404, redirect
from scoreboards.models import ScoreboardUser, ScoreboardTeam, AcceptedSolution


class ChallengeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Challenge
    fields = ["title", "category", "description", "flag", "point", "challenge_file_link"]
    template_name = "challenges/challenge_form.html"
    success_url = reverse_lazy("view_challenge")

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class ChallengeListView(LoginRequiredMixin, ListView):
    model = Challenge
    template_name = "challenges/challenge_list.html"
    context_object_name = "challenge_list"


# class ChallengeDetailView(LoginRequiredMixin, DetailView):
#     model = Challenge
#     template_name = "challenges/challenge_detail.html"


# class ChallengeSubmitFlagView(LoginRequiredMixin, FormView):
#     template_name = 'challenges/challenge_detail.html'
#     form_class = SubmitFlagChallengeForm

#     def form_valid(self, form,request):
#         challenge = Challenge.objects.get(id=self.kwargs['pk'])
#         points = challenge.point
#         user_id = request.user.id
#         team_id = User.objects.get(id=user_id).team
#         scoreboardUser = ScoreboardUser.objects.get(user=user_id)
#         scoreboardTeam = ScoreboardTeam.objects.get(team=team_id)
#         notAdmin = not request.user.is_superuser or not request.user.is_staff
#         entry_existed = AcceptedSolution.objects.filter(Q(team=team_id) & Q(challenge = challenge.id)).exists
#         if  notAdmin and not entry_existed :
#             scoreboardUser.score+=points
#             scoreboardTeam.score+=points
#             new_entry = AcceptedSolution.objects.create(team=team_id, challenge = challenge.id)

#             scoreboardUser.save()
#             scoreboardTeam.save()
#             new_entry.save()


#         return super().form_valid(form)
# TODO create scoreboard model and use id of user to add point to player and team


# class ChallengeSubmitFlagView(LoginRequiredMixin, FormMixin, DetailView):
#     template_name = "challenges/challenge_detail.html"
#     form_class = SubmitFlagChallengeForm
#     model = Challenge

#     def get_success_url(self):
#         return reverse("challenge_detail", kwargs={"pk": self.object.pk})

#     def get_context_data(self, **kwargs):
#         context = super(ChallengeSubmitFlagView, self).get_context_data(**kwargs)
#         context["form"] = ChallengeSubmitFlagView(initial={"challenge": self.object})
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

#     def form_valid(self, form):
#         flag = form.cleaned_data.get('flag')
#         hashed_flag = make_password(flag)

#         if hashed_flag == self.object.flag :

#             challenge = get_object_or_404(Challenge, id=self.kwargs["pk"])
#             points = challenge.point
#             user_id = self.request.user.id
#             team_id = self.request.user.team.id
#             scoreboard_user = ScoreboardUser.objects.get(user=user_id)
#             scoreboard_team = ScoreboardTeam.objects.get(team=team_id)
#             entry_existed = AcceptedSolution.objects.filter(
#                 team=team_id, challenge=challenge.id
#             ).exists()
#             if (
#                 not self.request.user.is_superuser
#                 and not self.request.user.is_staff
#                 and not entry_existed
#             ):
#                 scoreboard_user.score += points
#                 scoreboard_team.score += points
#                 new_entry = AcceptedSolution.objects.create(
#                     team=team_id, challenge=challenge
#                 )
#                 new_entry.save()
#                 scoreboard_user.save()
#                 scoreboard_team.save()
#         else :
#             messages.error(self.request, 'Incorrect flag. Please try again.')

#         return super(ChallengeSubmitFlagView, self).form_valid(form)

class ChallengeForm(forms.Form):
    flag = forms.CharField(label='Flag', max_length=255)

class ChallengeDetailView(LoginRequiredMixin,UserPassesTestMixin,FormView):
    template_name = 'challenges/challenge_detail.html'
    form_class = ChallengeForm
    success_url = reverse_lazy('view_challenge')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        challenge_id = self.kwargs['pk']
        challenge = Challenge.objects.get(id=challenge_id)
        context['challenge'] = challenge
        return context

    def form_valid(self, form):
        challenge_id = self.kwargs['pk']
        challenge = Challenge.objects.get(id=challenge_id)
        submitted_flag = form.cleaned_data['flag']
        if submitted_flag == challenge.flag:
            user = self.request.user
            if not user.is_staff and not user.is_superuser:
                team = user.team
                if not AcceptedSolution.objects.filter(team=team, challenge=challenge).exists():
                    AcceptedSolution.objects.create(team=team, challenge=challenge)
                    scoreboard_user, created = ScoreboardUser.objects.get_or_create(user=user)
                    scoreboard_user.score += challenge.point
                    scoreboard_user.save()
                    scoreboard_team, created = ScoreboardTeam.objects.get_or_create(team=team)
                    scoreboard_team.score += challenge.point
                    scoreboard_team.save()
                    # Flag is correct and entry added to AcceptedSolution and score updated
                    messages.success(self.request, 'Flag is correct')

                else:
                    # Flag is correct but entry already exists in AcceptedSolution
                    messages.warning(self.request, 'Flag is correct but already submitted')
            else :
                # Flag is correct but user is staff or superuser
                messages.warning(self.request, 'Flag is correct')
        else:
            # Flag is incorrect
                messages.error(self.request, 'Flag is incorrect')
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.team is not None or self.request.user.is_staff or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.warning(self.request, 'Please register yourself into team or register your team')
        return redirect('edit_user')



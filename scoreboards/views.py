
# Create your views here.
from django.views.generic.list import ListView
from .models import ScoreboardUser, ScoreboardTeam


class ScoreboardUserListView(ListView):
    model = ScoreboardUser
    template_name = "scoreboards/user_rank.html"
    context_object_name = "user_scores"
    ordering = ["-score"]

class ScoreboardTeamListView(ListView):
    model = ScoreboardTeam
    template_name = "scoreboards/team_rank.html"
    context_object_name = "team_scores"
    ordering = ["-score"]
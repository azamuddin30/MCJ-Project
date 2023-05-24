from django.urls import path
from .views import ScoreboardUserListView, ScoreboardTeamListView
from . import views

urlpatterns = [
    path("user_rank/", ScoreboardUserListView.as_view(), name="scoreboard_user_list"),
    path("team_rank/", ScoreboardTeamListView.as_view(), name="scoreboard_team_list"),
    
]

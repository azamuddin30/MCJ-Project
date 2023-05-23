from django.urls import path
from .views import ChallengeCreateView, ChallengeListView, ChallengeDetailView
from django.views.generic.base import TemplateView

urlpatterns = [
    path("", ChallengeListView.as_view(), name="view_challenge"),
    path("add_challenge/", ChallengeCreateView.as_view(), name="create_challenge"),
    path("<uuid:pk>", ChallengeDetailView.as_view(), name="detail_challenge"),
]

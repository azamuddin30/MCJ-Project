from django.urls import path
from .views import (
    RegisterUserView,
    RegisterTeamView,
    EditUserView,
    FreezeTeamActiveStatusView,
    FreezeTeamListView,
    UnFreezeTeamActiveStatusView,
    FreezeAllView,
    UnFreezeAllView
)
from django.views.generic.base import TemplateView

urlpatterns = [
    path("signup/", RegisterUserView.as_view(), name="signup"),
    path('team/', RegisterTeamView.as_view(), name='register_team'),
    path('edit_user/', EditUserView.as_view(), name='edit_user'),
    path('freeze/list', FreezeTeamListView.as_view(), name='freeze_list'),
    path('freeze_teams/<int:team>/', FreezeTeamActiveStatusView.as_view(), name='freeze_team'),
    path('unfreeze_teams/<int:team>/', UnFreezeTeamActiveStatusView.as_view(), name='unfreeze_team'),
    path('freeze_all/', FreezeAllView.as_view(), name='freeze_all'),
    path('unfreeze_all/', UnFreezeAllView.as_view(), name='unfreeze_all'),



]

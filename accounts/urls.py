from django.urls import path
from .views import RegisterUserView, RegisterTeamView, EditUserView
from django.views.generic.base import TemplateView  

urlpatterns = [
    path("signup/", RegisterUserView.as_view(), name="signup"),
    path('team/', RegisterTeamView.as_view(), name='register_team'),
    path('edit_user/', EditUserView.as_view(), name='edit_user'),
    

]

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser  #, Team


class CustomUserCreationForm(UserCreationForm):
    #team = forms.ModelChoiceField(queryset=Team.objects.all())

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("email",)


class CustomUserChangeForm(UserChangeForm):
    #team = forms.ModelChoiceField(queryset=Team.objects.all())

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


# class RegisterTeamForm(forms.Form):
#     team_name = forms.CharField(max_length=255, unique=True)

#     def clean_team_name(self):
#         team_name = self.cleaned_data["team_name"]

#         if Team.objects.filter(team_name=team_name).exists():
#             raise forms.ValidationError("Team name already exists.")

#         return team_name

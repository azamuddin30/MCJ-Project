# # class ChallengeForm(forms.ModelForm):
# #     class Meta:
# #         model = Challenge
# #         fields = ['title', 'description', 'flag', 'point', 'challenge_file']
# from django import forms

# from .models import Challenge


# class ChallengeSubmitFlagView(forms.ModelForm):
#     # flag = forms.CharField(max_length=255)

#     # def __init__(self, *args, **kwargs):
#     #     challenge_id = kwargs.pop('id')
#     #     super().__init__(*args, **kwargs)
#     #     self.fields['id'] = forms.UUIDField(initial=challenge_id, widget=forms.HiddenInput())

#     # def clean_flag(self):
#     #     flag = self.cleaned_data["flag"]
#     #     hashed_flag = make_password(flag)
#     #     # TODO get id
#     #     if hashed_flag == Challenge.objects.get(id=self.kwargs["pk"]).flag:
#     #         return flag
#     #     else:
#     #         raise forms.ValidationError("Incorrect flag.")
#     class Meta:
#         model = Challenge
#         fields = ['title', 'category', 'description', 'challenge_file', 'point']
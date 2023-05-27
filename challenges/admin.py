from django.contrib import admin
from .models import Challenge

class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'flag', 'description', 'challenge_file', 'created_at', 'point')

admin.site.register(Challenge, ChallengeAdmin)
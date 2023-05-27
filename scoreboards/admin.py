from django.contrib import admin
from .models import ScoreboardUser, ScoreboardTeam, AcceptedSolution


# Register your models here.


class ScoreboardUserAdmin(admin.ModelAdmin):
    list_display = ("user", "score")


class ScoreboardTeamAdmin(admin.ModelAdmin):
    list_display = ("team", "score")


class AcceptedSolutionAdmin(admin.ModelAdmin):
    list_display = ("team", "challenge")


admin.site.register(ScoreboardUser, ScoreboardUserAdmin)
admin.site.register(ScoreboardTeam, ScoreboardTeamAdmin)
admin.site.register(AcceptedSolution, AcceptedSolutionAdmin)

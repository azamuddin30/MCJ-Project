from django.contrib import admin
from.models import ScoreboardUser, ScoreboardTeam, AcceptedSolution
# Register your models here.
admin.site.register(ScoreboardUser)
admin.site.register(ScoreboardTeam)
admin.site.register(AcceptedSolution)

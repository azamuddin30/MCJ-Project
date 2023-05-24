from django.db import models
from accounts.models import User, Team
from challenges.models import Challenge
# Create your models here.

class ScoreboardUser(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username


class ScoreboardTeam(models.Model) :
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return self.team.name

class AcceptedSolution(models.Model) :
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)


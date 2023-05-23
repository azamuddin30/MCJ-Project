import uuid 
from django.db import models
from django.urls import reverse
# Create your models here.


class Challenge(models.Model):
    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    flag = models.CharField(max_length=255, blank=True, default="")
    description = models.TextField()
    challenge_file = models.FileField(upload_to="challenges/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    point = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail_challenge", args=[str(self.id)])

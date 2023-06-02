from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.


class Head(models.Model) :
    title = models.CharField(max_length=255)
    author = models.ForeignKey( get_user_model(), on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self) :
        return reverse("head_detail", kwargs={"pk":self.pk})


class Comment(models.Model) :
    head = models.ForeignKey(Head, on_delete=models.CASCADE)
    author = models.ForeignKey( get_user_model(), on_delete=models.CASCADE, null=True)
    body = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self) :
        return reverse("head_detail", kwargs={"pk":self.head.pk})





from django.urls import path

from .views import (
    HeadListView,
    HeadDetailView,
    HeadUpdateView,
    HeadDeleteView,
    HeadCreateView,
    CommentDeleteView,
)



urlpatterns = [
    path("<int:pk>/", HeadDetailView.as_view(), name="head_detail"),
    path("<int:pk>/edit/", HeadUpdateView.as_view(), name="head_edit"),
    path("<int:pk>/delete/", HeadDeleteView.as_view(), name="head_delete"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
    path("new/", HeadCreateView.as_view(), name="head_new"),  # new
    path("", HeadListView.as_view(), name="head_list"),
]
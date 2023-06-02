from django.shortcuts import render
from .forms import CommentForm
from .models import *

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, DetailView, FormView  
from django.views.generic.detail import SingleObjectMixin  
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse  



# Create your views here.
class HeadListView(LoginRequiredMixin, ListView):  
    model = Head
    template_name = "forums/forum_list.html"

class HeadCreateView(LoginRequiredMixin, CreateView):  
    model = Head
    template_name = "forums/forum_new.html"
    fields = ("title", "description")  

    def form_valid(self, form):  
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class HeadDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Head
    template_name = "forums/forum_delete.html"
    success_url = reverse_lazy("forum_list")

    def test_func(self):  
        obj = self.get_object()
        return obj.author == self.request.user

class HeadUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  
    model = Head
    fields = (
        "title",
        "description",
    )
    template_name = "forums/forum_edit.html"

    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user
    


class CommentGet(DetailView):  
    model = Head
    template_name = "forums/forum_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):  
    model = Head
    form_class = CommentForm
    template_name = "forums/forum_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.head = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        head = self.get_object()
        return reverse("head_detail", kwargs={"pk": head.pk})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Comment
    template_name = "forums/comment_delete.html"
    success_url = reverse_lazy("forum_list")

    def test_func(self):  
        obj = self.get_object()
        return obj.author == self.request.user 

class HeadDetailView(LoginRequiredMixin, View):  
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)

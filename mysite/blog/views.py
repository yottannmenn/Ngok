from typing import List
from django.shortcuts import render
from .mixins import SuperuserRequiredMixin

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Post
from .forms import PostCreateForm
from django.views import generic
from django.urls import reverse_lazy


class PostCreateView(SuperuserRequiredMixin, generic.CreateView):
    mode = "Create"
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('blog:post_list')


class PostDetailView(generic.DetailView):
    model = Post


class PostUpdateView(SuperuserRequiredMixin, generic.UpdateView):
    mode = "Update"
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('blog:post_detail')


class PostDeleteView(SuperuserRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

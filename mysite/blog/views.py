from typing import List
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Post
from .forms import PostCreateForm
from django.views import generic
from django.urls import reverse_lazy


class PostCreateView(generic.CreateView):  # 追加
    model = Post  # 作成したい model を指定
    form_class = PostCreateForm  # 作成した form クラスを指定
    success_url = reverse_lazy('blog:post_list')

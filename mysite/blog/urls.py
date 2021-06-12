from django.urls import path
from django.views.generic import TemplateView
from django.views.generic import ListView

from . import views
from .models import Post

app_name = 'blog'
urlpatterns = [
    path("", TemplateView.as_view(template_name="blog/index.html"), name="index"),
    path('post_list/', ListView.as_view(model=Post), name='post_list'),
]

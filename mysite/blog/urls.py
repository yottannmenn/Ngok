from django.urls import path
from django.views.generic import TemplateView
from django.views.generic import ListView

from . import views
from .models import Post

app_name = 'blog'
urlpatterns = [
    path("", TemplateView.as_view(template_name="blog/index.html"), name="index"),
    path('post_list/', ListView.as_view(model=Post), name='post_list'),
    path('post_create/', views.PostCreateView.as_view(), name='post_create'),
    path('post_detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post_update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('post_delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
]

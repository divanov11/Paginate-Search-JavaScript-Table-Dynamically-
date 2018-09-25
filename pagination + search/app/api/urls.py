
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('posts_dynamic/<int:page>/', views.posts, name="posts_dynamic"),
]

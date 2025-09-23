from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog'),
    path('create/', views.create_post, name='blog_create'),
    path('blog/<int:blog_id>/view/', views.view_detalhe, name='blog_detalhe'),
]
from django.urls import path
from .import views



urlpatterns = [
    path('', views.post_view, name='post-list'),
    path('like/', views.like_post, name='like-post')
]

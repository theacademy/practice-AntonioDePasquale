from django.urls import path
from .views import blog_home, blog_detail
from . import views


urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('post/<int:post_id>/', views.blog_detail, name='blog_detail'),  # Blog detail URL
    path('create/', views.create_blog_post, name='create_blog_post'),
]

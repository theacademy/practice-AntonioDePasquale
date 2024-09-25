from django.urls import path
from .views import blog_home, blog_detail
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('post/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('create/', views.create_blog_post, name='create_blog_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
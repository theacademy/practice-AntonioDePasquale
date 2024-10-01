"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from diaryapp import views
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'signInDetail', views.SignInDetailViewSet, basename='SignInDetailListCreate')
router.register(r'users', views.UserViewSet, basename='UserListCreate')
router.register(r'diary', views.EntryViewSet, basename='EntryListCreate')
router.register(r'locker', views.MemoViewSet, basename='MemoListCreate') 
# router.register(r'diaries', views.DiaryViewSet, basename='DiaryListCreate')
# router.register(r'Locker', views.LockerViewSet, basename='LockerListCreate') 

urlpatterns = [
    # path('api/', include('diaryapp.urls')), 
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include the app's URLs
    # path('auth/register/', views.CreateUserAPIView.as_view({'post': 'register'}), name='auth_user_create'),
    # path('auth/login/', views.CustomObtainAuthToken.as_view(), name='auth_user_login'),
    # path('auth/logout/', views.LogoutUserAPIView.as_view(), name='auth_user_logout'),
]

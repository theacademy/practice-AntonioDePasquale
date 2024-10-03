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
from diaryapp.views import CustomObtainAuthToken  # Ensure this is uncommentedS


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='UserListCreate')
router.register(r'diary', views.DiaryViewSet, basename='DiaryListCreate')
router.register(r'locker', views.LockerViewSet, basename='LockerListCreate')
router.register(r'entries', views.EntryViewSet, basename='EntryListCreate')
router.register(r'memos', views.MemoViewSet, basename='MemoListCreate')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/register/', views.RegisterView.as_view(), name='register'),  # Ensure this is the correct register view
    path('api/', include(router.urls)),
    path('auth/login/', CustomObtainAuthToken.as_view(), name='custom_api_token_auth'),  # Uncommented the login view
]



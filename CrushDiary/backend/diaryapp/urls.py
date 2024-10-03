from django.urls import path, include
from diaryapp import views
# from .views import EntryListCreate, EntryDetail
from diaryapp.views import MoodChoicesView 



urlpatterns = [
    # path('entries/', EntryListCreate.as_view(), name='entry-list-create'),
    # path('entries/<int:pk>/', EntryDetail.as_view(), name='entry-detail'),
    # path('locker/', .as_view(), name=''),
    #path('auth/', include('diaryapp.urls')),
    #path('login/', views.CustomObtainAuthToken.as_view(), name='auth_user_login')
    path('mood-choices/', MoodChoicesView.as_view(), name='mood-choices'),
    
]
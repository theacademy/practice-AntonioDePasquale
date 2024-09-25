from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This is your homepage
    path('add-contact/', views.add_contact, name='add_contact'),  # URL for add contact
    path('contacts/', views.contact_list, name='contact_list'),  # URL for contact list
]
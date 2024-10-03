# admin.py

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import (
    PlayerCharacter,
    Diary,
    Crush,
    Locker,
    Entry,
    Memo,
    CustomUser,
)

# Define a custom admin for the CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser  # Specify your custom user model here
    list_display = ['username', 'email', 'password']
    search_fields = ['email', 'username']

# Register your models
@admin.register(PlayerCharacter)
class PlayerCharacterAdmin(admin.ModelAdmin):
    # Display fields in the list view of PlayerCharacter
    list_display = ('id', 'inGameName', 'user', 'eyeColour', 'hairColour')
    # Enable search by in-game name or the associated user's username
    search_fields = ('inGameName', 'user__username')

@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    # Display fields in the list view of Diary
    list_display = ('diaryId', 'author', 'playerCharacterId', 'noOfEntries')
    # Enable search by author's name or player character's in-game name
    search_fields = ('author', 'playerCharacterId__inGameName')

@admin.register(Crush)
class CrushAdmin(admin.ModelAdmin):
    list_display = ('crushName', 'mood', 'matchingMoodEntries')
    search_fields = ('crushName',)

@admin.register(Locker)
class LockerAdmin(admin.ModelAdmin):
    list_display = ('lockerId', 'diaryId')  # You can add more fields if necessary
    search_fields = ('diaryId',)  # This will allow searching by diary author

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'diaryId', 'mood', 'createdAt')
    search_fields = ('title', 'diaryId__author')

@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    list_display = ('title', 'locker')
    search_fields = ('title',)

# Register your custom user model with the custom user admin
User = get_user_model()
admin.site.register(User, CustomUserAdmin)  # Register the custom user admin class





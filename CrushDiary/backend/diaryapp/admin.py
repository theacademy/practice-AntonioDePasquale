from django.contrib import admin
from .models import Entry, Diary, SignInDetail, User, Crush

class DiaryAdmin(admin.ModelAdmin):
    list_display = ('diaryId', 'author', 'noOfEntries', 'userId')
    list_display_links = ('diaryId', 'author')

class EntryAdmin(admin.ModelAdmin):
    list_display = ('entryId', 'diaryId', 'title', 'content', 'mood', 'createdAt','updatedAt')
    list_display_links = ('entryId', 'title')

# Admin configuration for the SignInDetails model
class SignInDetailAdmin(admin.ModelAdmin):
    list_display = ('email',)  # Only display the email field
    search_fields = ('email',)  # Allow searching by email

# Admin configuration for the User model
class UserAdmin(admin.ModelAdmin):
    list_display = ('userId', 'username','eyeColour','hairColour', 'email')  # Display these fields
    search_fields = ('username', 'email__email')  # Allow searching by username and email

class CrushAdmin(admin.ModelAdmin):
    list_display = ('crushId','crushName','mood', 'matchingMoodEntries' )  # Display these fields
    search_fields = ('username', 'email__email')  # Allow searching by username and email

# Register your models with the admin site
admin.site.register(SignInDetail, SignInDetailAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Diary, DiaryAdmin)
admin.site.register(Crush, CrushAdmin)
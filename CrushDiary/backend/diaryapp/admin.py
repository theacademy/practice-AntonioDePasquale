from django.contrib import admin
from .models import Entry, Diary, SignInDetail, User, Crush ,Locker, Memo #################################

class DiaryAdmin(admin.ModelAdmin):
    list_display = ('diaryId', 'author', 'noOfEntries', 'userId')
    list_display_links = ('diaryId', 'author')

class EntryAdmin(admin.ModelAdmin):
    list_display = ('entryId', 'diaryId', 'title', 'content', 'mood', 'createdAt','updatedAt')
    list_display_links = ('entryId', 'title')

# Admin configuration for the SignInDetails model
class SignInDetailAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')  # Only display the email field
    search_fields = ('email',)  # Allow searching by email

# Admin configuration for the User model
class UserAdmin(admin.ModelAdmin):
    list_display = ('userId', 'username','eyeColour','hairColour', 'email')  # Display these fields
    search_fields = ('username', 'email__email')  # Allow searching by username and email

class CrushAdmin(admin.ModelAdmin):
    list_display = ('crushId','crushName','mood', 'matchingMoodEntries' )  # Display these fields
    search_fields = ('username', 'email__email')  # Allow searching by username and email

# Create an inline model for Memo to show them within the Locker
class MemoInline(admin.TabularInline):################################
    model = Memo
    extra = 0  # No extra blank memo forms will be shown

# Customize Locker admin to include the related memos
# @admin.register(Locker) #########################
class LockerAdmin(admin.ModelAdmin):
    list_display = ('lockerId', 'diaryID', 'get_memos')
    inlines = [MemoInline]  # Inline view for memos related to locker

    def get_memos(self, obj): ####################
        """Displays a count of memos in the locker."""
        # return ", ".join([memo.title for memo in obj.diaryID.memo_set.all()])
        # return ", ".join([memo.title for memo in obj.memo_set.all()])
        return ", ".join([memo.title for memo in obj.memos.all()])
    get_memos.short_description = 'Memos'

# Optionally, you can also register Memo itself
# @admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):################################
    list_display = ('memoId', 'title', 'content')

# Register your models with the admin site
admin.site.register(SignInDetail, SignInDetailAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Diary, DiaryAdmin)
admin.site.register(Crush, CrushAdmin)
admin.site.register(Locker, LockerAdmin)  #####################################
admin.site.register(Memo, MemoAdmin) #####################################

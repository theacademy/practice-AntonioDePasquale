from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField() # TextField does not require the max_length()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # uses the django.contrib.auth.models library for logged user
    date_time = models.DateTimeField(default=timezone.now)
    attachment = models.FileField(upload_to="static/attachments/%Y/%m/%d")

    def __str__(self):
        return f"({self.date_time}) {self.title} by {self.author}: {self.description}"

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    commentAuthor = models.TextField()  # Make sure this matches the form
    commentContent = models.TextField()
    commentDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment on ({self.commentDate}) by {self.commentAuthor}: {self.commentContent}"

#TODO
class User(models.Model):
    pass
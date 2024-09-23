from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    attachment = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # New field for image upload
    date_posted = models.DateTimeField(auto_now_add=True)  # Automatically adds the timestamp when created

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)  # Automatically adds the timestamp when created

    def __str__(self):
        return f"Comment by {self.author} on {self.blog_post.title}"  # More descriptive string representation



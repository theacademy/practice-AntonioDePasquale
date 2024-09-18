from rest_framework import serializers
from .models import Comment, Blog

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'commentAuthor', 'commentContent', 'commentDate', 'blog']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'description', 'author', 'date_time', 'attachment')
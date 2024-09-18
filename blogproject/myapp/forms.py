from django import forms
from .models import Comment, Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields = ['title', 'description', 'author', 'date_time', 'attachment']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['commentAuthor', 'commentContent']

    #Creates a hidden blog_id so it can be associated with a blog, but does not display it
    def __init__(self, *args, **kwargs):
        self.blog = kwargs.pop('blog', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        if self.blog:
            comment.blog = self.blog
        if commit:
            comment.save()
        return comment
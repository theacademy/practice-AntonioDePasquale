from django import forms
from .models import Comment, BlogPost
from django.core.exceptions import ValidationError

# Custom validation for image size
def validate_image(image):
    if image.size > 5 * 1024 * 1024:  # Limit size to 5MB
        raise ValidationError("Image file too large ( > 5MB )")
    return image


class BlogPostForm(forms.ModelForm):
    attachment = forms.ImageField(validators=[validate_image], required=False)  # Add the image field with validation

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'attachment']  # Fields to include from the BlogPost model


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']  # Fields for comment form

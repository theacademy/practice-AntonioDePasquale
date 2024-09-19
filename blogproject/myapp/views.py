# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

# Hard-coded blog posts
BLOG_POSTS = [
    {
        "id": 1,
        "title": "First Post",
        "content": "This is the first blog post.",
        "date_posted": "2024-09-19",
        "comments": [
            {"author": "Alice", "content": "Great post!"},
            {"author": "Bob", "content": "Very informative."}
        ]
    },
    {
        "id": 2,
        "title": "Second Post",
        "content": "This is the second blog post.",
        "date_posted": "2024-09-18",
        "comments": []
    }
]

def blog_home(request):
    blog_posts = BlogPost.objects.order_by('-date_posted')
    return render(request, 'blog_home.html', {'blog_posts': blog_posts})

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_post = form.save()  # Save the form and get the new blog post instance
            return redirect('blog_detail', post_id=new_post.id)  # Redirect to the newly created post
    else:
        form = BlogPostForm()

    return render(request, 'create_blog_post.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comments.all()  # Retrieve comments related to the post

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog_post = post  # Associate comment with the blog post
            new_comment.save()
            return redirect('blog_detail', post_id=post.id)  # Refresh the page to display the new comment
    else:
        comment_form = CommentForm()

    return render(request, 'blog_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })
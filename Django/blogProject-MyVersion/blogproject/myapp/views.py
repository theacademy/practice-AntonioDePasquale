from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm, CommentForm

def blog_home(request):
    blog_posts = BlogPost.objects.order_by('-date_posted')
    return render(request, 'blog_home.html', {'blog_posts': blog_posts})


def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)  # Handle file upload
        if form.is_valid():
            new_post = form.save()  # Save the form and get the new blog post instance
            return redirect('blog_detail', post_id=new_post.id)  # Redirect to the newly created post
    else:
        form = BlogPostForm()

    return render(request, 'create_blog_post.html', {'form': form})


def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comments.all().order_by('-date_posted')  # Order comments by date, newest first

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog_post = post
            new_comment.save()
            return redirect('blog_detail', post_id=post.id)
    else:
        comment_form = CommentForm()

    return render(request, 'blog_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })

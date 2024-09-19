# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm

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
    return render(request, 'blog_home.html', {'blog_posts': BLOG_POSTS})

def blog_detail(request, blog_id):
    blog_post = next((post for post in BLOG_POSTS if post["id"] == blog_id), None)
    if blog_post is None:
        return render(request, '404.html')  # Handle not found

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Normally save the comment, but here we'll just append it for simplicity
            new_comment = {
                "author": form.cleaned_data['author'],
                "content": form.cleaned_data['content']
            }
            blog_post['comments'].append(new_comment)
            return redirect('blog_detail', blog_id=blog_id)
    else:
        form = CommentForm()

    return render(request, 'blog_detail.html', {
        'blog_post': blog_post,
        'form': form,
        'comments': blog_post['comments']
    })


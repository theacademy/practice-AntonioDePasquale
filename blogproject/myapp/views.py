from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from .forms import BlogForm, CommentForm
from .models import Blog, Comment
#from .forms import CommentForm
from .serializers import CommentSerializer, BlogSerializer

#TODO: finish this
class BlogList(generics.ListCreateAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        queryset = Blog.objects.all()
        title = self.request.query_params.get('title')
        description = self.request.query_params.get('description')
        author = self.request.query_params.get('author')
        date_time = self.request.query_params.get('date_time')
        attachment = self.request.query_params.get('attachment')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if description:
            queryset = queryset.filter(description__icontains=description)
        if author:
            queryset = queryset.filter(author__icontains=author)
        if date_time:
            queryset = queryset.filter(date_time__icontains=date_time)
        if attachment:
            queryset = queryset.filter(email__icontains=attachment)
        return queryset

    def blog_posts(self, request):
        blog = Blog.objects.all().order_by('last_name')
        return render(request, 'templates/home.html', {'blog': blog})

    def blog_create(self, request):
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('blog_posts')
        else:
            form = BlogForm()
        return render(request, 'templates/blog_form.html', {'form': form})

    def blog_update(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        if request.method == 'POST':
            form = BlogForm(request.POST, instance=blog)
            if form.is_valid():
                form.save()
                return redirect('blog_posts')
        else:
            form = BlogForm(instance=blog)
        return render(request, 'templates/blog_form.html', {'form': form})

    def blog_delete(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        if request.method == 'POST':
            blog.delete()
            return redirect('blog_posts')
        return render(request, 'templates/blog_confirm_delete.html', {'blog': blog})


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

#TODO
#finish this
class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        blog_id = self.request.query_params.get('blog_id')
        if blog_id is not None:
            queryset = queryset.filter(blog_id=blog_id)
        return queryset

    def perform_create(self, serializer):
        blog_id = self.request.data.get('blog_id')
        blog = get_object_or_404(Blog, id=blog_id)
        serializer.save(blog=blog)


def blog_comments(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, blog=blog)  # Pass blog instance
        if form.is_valid():
            form.save()
            return redirect('blog_comments_test', blog_id=blog.id)
    else:
        form = CommentForm()

    comments = blog.comments.all()

    return render(request, 'comment_form.html', {
        'blog': blog,
        'form': form,
        'comments': comments
    })

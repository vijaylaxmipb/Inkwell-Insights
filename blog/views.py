from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/post.html"

# Function-based view
# def my_blog(request):
#     posts = Post.objects.all()
#     return render(request, 'post.html', {'posts': posts})
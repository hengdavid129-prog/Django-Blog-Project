from django.shortcuts import render, get_object_or_404
from post.models import Post
from post.models import Tag

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-created_at')

    all_tag = Tag.objects.all()
    context = {
        'data': posts,
        'all_tag': all_tag
    }

    return render(request, 'blog/index.html', context)

def detail(request, item_id):
    post = get_object_or_404(Post, id=item_id)
    all_tag = Tag.objects.all()
    context = {
        'data': post,
        'all_tag': all_tag
    }

    return render(request, 'blog/blog_detail.html', context)
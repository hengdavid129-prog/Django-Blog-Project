from django.shortcuts import render, redirect, get_object_or_404
from category.models import Category
from tag.models import Tag
from post.models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-id')
    context = {
        'data': posts
    }
    return render(request, 'post/index.html', context)

def create(request):
    category = Category.objects.all().order_by('id')
    tag = Tag.objects.all().order_by('id')
    context = {
        'category': category,
        'tag': tag
    }

    if request.method == 'POST':
        # print("POST DATA:", request.POST)
        # print("FILES DATA:", request.FILES)
        title = request.POST.get('title')
        content = request.POST.get('content')
        thumbnail = request.FILES.get('thumbnail')
        category_id = request.POST.get('category')
        tag_id = request.POST.getlist('tags')

        if not title or title.strip() == '' or not content or content.strip() == '' or not category_id:
            return redirect('post:create')
        post = Post.objects.create(
           title = title,
           content = content,
           thumbnail = thumbnail,
           category_id = category_id,
        )

        if tag_id:
            post.tag.set(tag_id)
        return redirect('post:index')

    return render(request, 'post/create.html', context)

def edit(request, item_id):
    post = get_object_or_404(Post, id=item_id)
    category = Category.objects.all().order_by('id')
    tag = Tag.objects.all().order_by('id')
    context = {
        'category': category,
        'tag': tag,
        'post': post
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        thumbnail = request.FILES.get('thumbnail')
        category_id = request.POST.get('category')
        tag_id = request.POST.getlist('tags')

        if not title or title.strip() == '' or not content or content.strip() == '':
            return redirect('post:edit', item_id)
        post.title = title
        post.content = content
        if thumbnail:
            if post.thumbnail:
                post.thumbnail.delete(save=False)
            post.thumbnail = thumbnail
        post.category_id = category_id
        if tag_id:
            post.tag.set(tag_id)
        post.save()
        return redirect('post:index')

    return render(request, 'post/edit.html', context)


def delete(request, item_id):
    post = get_object_or_404(Post, id=item_id)
    if post.thumbnail:
        post.thumbnail.delete(save=False)
    post.delete()
    return redirect('post:index')
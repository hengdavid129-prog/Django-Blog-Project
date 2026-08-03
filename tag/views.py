from django.shortcuts import render, redirect, get_object_or_404
from .models import Tag

# Create your views here.
def index(request):
    tags = Tag.objects.all().order_by('-id')
    context = {
        'data': tags
    }
    return render(request, 'tag/index.html', context)

def create(request):
    if request.method == 'POST':
        tag_name = request.POST.get('tag')
        if not tag_name or tag_name.strip() == '':
            return redirect('tag:create')
        Tag.objects.create(
            name = tag_name
        )
        return redirect('tag:index')
    return render(request, 'tag/create.html')

def edit(request, item_id):
    tag = get_object_or_404(Tag, id=item_id)
    if request.method == 'POST':
        tag_name = request.POST.get('tag')
        if not tag_name or tag_name.strip() == '':
            return redirect('tag:edit', item_id)
        tag.name = tag_name
        tag.save()
        return redirect('tag:index')
    
    return render(request, 'tag/edit.html', {'data': tag})

def delete(request, item_id):
    tag = get_object_or_404(Tag, id=item_id)
    tag.delete()
    return redirect('tag:index')
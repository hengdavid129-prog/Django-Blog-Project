from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_require

# Create your views here.
@login_required(login_url='accounts:login')
@role_require('admin')
def index(request):
    categories = Category.objects.all().order_by('-id')
    context = {
        'data': categories
    }
    return render(request, 'category/index.html', context)

@login_required(login_url='accounts:login')
@role_require('admin')
def create(request):
    if request.method == 'POST':
        cate_name = request.POST.get('name')

        if not cate_name or cate_name.strip() == '':
            return redirect('category:create')
    
        Category.objects.create(
            name = cate_name
        )
        return redirect('category:index')
    return render(request, 'category/create.html')

@login_required(login_url='accounts:login')
@role_require('admin')
def edit(request, item_id):
    category = get_object_or_404(Category, id=item_id)
    if request.method == 'POST':
        cate_name = request.POST.get('name')

        if not cate_name or cate_name.strip() == '':
            return redirect('category:edit', item_id)
        
        category.name = cate_name
        category.save()
        return redirect('category:index')
    return render(request, 'category/edit.html', {'data': category})

@login_required(login_url='accounts:login')
@role_require('admin')
def delete(request, item_id):
    category = get_object_or_404(Category, id=item_id)
    category.delete()
    return redirect('category:index')

from category.models import Category

def nav_categories(request):
    categories = Category.objects.all().order_by('-id')

    return {'nav_categories': categories}
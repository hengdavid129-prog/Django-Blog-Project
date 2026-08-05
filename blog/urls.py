from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/detail/<int:item_id>>', views.detail, name='detail'),
    path('blog/<int:category_id>>', views.retrieve_by_category, name='retrieve_by_category')
]
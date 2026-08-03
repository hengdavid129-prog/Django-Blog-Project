from django.urls import path
from . import views
app_name = 'post'

urlpatterns = [
    path('post/', views.index, name='index'),
    path('post/create', views.create, name='create'),
    path('post/edit/<int:item_id>', views.edit, name='edit'),
    path('post/delete/<int:item_id>', views.delete, name='delete')
]
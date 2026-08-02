from django.urls import path
from . import views
app_name = 'tag'

urlpatterns = [
    path('tag/', views.index, name='index'),
    path('tag/create', views.create, name='create'),
    path('tag/edit/<int:item_id>', views.edit, name='edit'),
    path('tag/delete/<int:item_id>', views.delete, name='delete')
]
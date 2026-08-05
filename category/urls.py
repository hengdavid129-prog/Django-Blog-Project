from django.urls import path
from . import views
app_name = 'category'

urlpatterns = [
    path('category/', views.index, name='index'),
    path('category/create', views.create, name='create'),
    path('category/edit/<int:item_id>', views.edit, name='edit'),
    path('category/delete/<int:item_id>', views.delete, name='delete'),
]

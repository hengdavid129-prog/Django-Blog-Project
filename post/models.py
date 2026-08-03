from django.db import models
from category.models import Category
from tag.models import Tag

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='post')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
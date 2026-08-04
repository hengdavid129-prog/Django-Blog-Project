from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('reader', 'Reader'),
        ('writer', 'Writer'),
        ('admin', 'Admin')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='reader')

    def __str__(self):
        return f"{self.user.first_name} - f{self.role}"

    def save(self, *args, **kwargs):
        if self.role == 'admin':
            self.user.is_staff = True
            self.user.is_superuser = True
        else:
            self.user.is_staff = False
            self.user.is_superuser = False
        self.user.save()
        super().save(*args, **kwargs)


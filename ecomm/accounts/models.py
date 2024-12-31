from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel

class Profile(BaseModel):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name="profile"
    )
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(
        max_length=100, 
        null=True, 
        blank=True
    )
    profile_image = models.ImageField(
        upload_to='profile/', 
        null=True, 
        blank=True  # Adding `blank=True` for optional upload
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"

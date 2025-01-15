from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from base.models import BaseModel
from base.emails import send_account_activation_email  # Import your email-sending function

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
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Signal to automatically create Profile and send email
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        if created:
            # Generate a unique email token
            email_token = str(uuid.uuid4())
            
            # Create a Profile instance
            profile = Profile.objects.create(
                user=instance, 
                email_token=email_token
            )
            
            # Send activation email
            email = instance.email
            send_account_activation_email(email, email_token)
    
    except Exception as e:
        # Log the error (replace with proper logging in production)
        print(f"Error in creating profile or sending email: {e}")

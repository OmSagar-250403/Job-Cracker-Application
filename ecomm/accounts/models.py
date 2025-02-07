from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from base.models import BaseModel
from base.emails import send_account_activation_email  # Import your email-sending function
from products.models import Product, ColorVariant, SizeVariant, Coupon  # Corrected import statement

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

class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    is_paid = models.BooleanField(default=False)

    def get_cart_total(self):
        cart_items = self.cart_items.all()
        total_price = 0
        for cart_item in cart_items:
            total_price += cart_item.get_product_price()
        return total_price

class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    color_variant = models.ForeignKey(ColorVariant, on_delete=models.SET_NULL, null=True, blank=True)
    size_variant = models.ForeignKey(SizeVariant, on_delete=models.SET_NULL, null=True, blank=True)

    def get_product_price(self):
        price = self.product.price
        if self.color_variant:
            price += self.color_variant.price
        if self.size_variant:
            price += self.size_variant.price
        return price * self.quantity

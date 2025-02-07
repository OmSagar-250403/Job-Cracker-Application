from django.contrib import admin  # Import for admin interface
from django.urls import path, include  # Import for routing URLs
from django.conf import settings  # Import for accessing settings
from django.conf.urls.static import static  # Import for serving static and media files
from accounts.views import *

urlpatterns = [
    path('login/' , login_page , name="login" ),
    path('register/' , register_page , name="register" ),
    path('admin/', admin.site.urls), 
    path('cart/' , cart , name="cart" ),
    path('cart/remove/<str:uid>/', remove_from_cart, name='remove_cart'),
    path('activate/<email_token>/' , activate_email , name="activate_email"), # Admin URL
    path('cart/add/<slug:product_slug>/', add_to_cart, name='add_to_cart'),
    # path('', include('home.urls')),  # Example: Include app-specific URLs
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

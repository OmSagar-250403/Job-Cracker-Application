from django.contrib import admin  # Import for admin interface
from django.urls import path, include  # Import for routing URLs
from django.conf import settings  # Import for accessing settings
from django.conf.urls.static import static  # Import for serving static and media files

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    # path('', include('home.urls')),  # Example: Include app-specific URLs
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

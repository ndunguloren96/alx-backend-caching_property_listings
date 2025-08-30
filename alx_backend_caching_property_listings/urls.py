from django.contrib import admin
from django.urls import path, include # Import 'include' here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('properties/', include('properties.urls')),
]

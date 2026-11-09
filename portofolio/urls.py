from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    
    # Routing khusus untuk endpoint API (Tugas 6)
    path("api/v1/", include("main.api_urls")),
]
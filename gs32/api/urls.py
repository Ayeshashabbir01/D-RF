from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', include('api.urls')),  # ✅ this line must be here
]

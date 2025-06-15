# gs10/gs10/urls.py

from django.contrib import admin
from django.urls import path
from api import views  # ✅ Correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.student_api, name='student_api'),  # ✅ FIXED
    path('studentapi/<int:pk>', views.student_api, name='student_api'),
]

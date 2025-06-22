

from django.contrib import admin
from django.urls import path
from api import views  # Uncomment if you have views to include in the URLs

urlpatterns = [
    path('admin/', admin.site.urls),

    path('studentapi/', views.StudentList.as_view()),  # Ensure this view is defined in your views.py
]

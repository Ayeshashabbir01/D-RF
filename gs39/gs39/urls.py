

from django.contrib import admin
from django.urls import path
from api import views 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('studentapi/', views.StudentList.as_view()),  # Ensure this view is defined in your views.py
]

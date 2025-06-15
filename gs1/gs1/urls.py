from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface URL
    path('stuinfo/<int:pk>', views.student_detail),
    path('stuinfo/', views.student_list),  # URL for the student_detail view
]

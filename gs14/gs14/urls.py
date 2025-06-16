from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.LCStudentAPI.as_view()),  # List and Create
    path('studentapi/<int:pk>/', views.RUDStudentAPI.as_view()),  # Retrieve, Update, Delete
   

]

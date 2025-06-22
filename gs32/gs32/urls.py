from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentList.as_view()),  # List and Create
    path('studentapi/', views.StudentCreate.as_view()),  # List and Create
    #path('studentapi/<int:pk>/', views.StudentRetrieve.as_view()),  # Retrieve
    path('studentapi/<int:pk>/', views.StudentUpdate.as_view()),  # Update
    #path('studentapi/<int:pk>/', views.StudentDestroy.as_view()),  # Delete
  
]

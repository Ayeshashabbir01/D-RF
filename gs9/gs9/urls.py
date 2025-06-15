from django.urls import path
from django.urls import admin
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.hello_world, name='hello_world'),
]   
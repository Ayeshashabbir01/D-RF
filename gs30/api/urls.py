# api/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StudentModelViewSet

router = DefaultRouter()
router.register('', StudentModelViewSet, basename='student')  # Handles /studentapi/

urlpatterns = router.urls

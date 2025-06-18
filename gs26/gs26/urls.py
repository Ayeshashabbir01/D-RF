from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from api.auth import CustomAuthToken
# Create a router and register our viewset with it.
router = DefaultRouter()

#Register studentviewset with the router
router.register('studentapi', views.StudentModelViewSet, basename='student')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the router's URLs
    path('', include(router.urls)),
    # Include the API URLs
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Include the token authentication URLs
    path('gettoken/', CustomAuthToken.as_view()),
]
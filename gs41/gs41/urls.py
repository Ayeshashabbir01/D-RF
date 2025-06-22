
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register('singer', views.SingerModelViewSet, basename='singer')
router.register('song', views.SongModelViewSet, basename='song')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

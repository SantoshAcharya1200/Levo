from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, get_holidays,UserViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('holidays/', get_holidays, name='get_holidays'),
]

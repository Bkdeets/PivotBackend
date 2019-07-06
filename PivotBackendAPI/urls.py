from django.urls import path, include
from . import views
from rest_framework import routers
from .views import UserViewSet, ProfileViewSet, StrategyViewSet

router = routers.DefaultRouter()
router.register('strategy', StrategyViewSet)
router.register('profile', ProfileViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

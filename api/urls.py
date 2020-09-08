from django.urls import path, include
# from django.views.decorators.csrf import csrf_exempt
from .views import PriceInMinutesViewSet, HistoricalDataViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'price', views.PriceInMinutesViewSet)
router.register(r'data', views.HistoricalDataViewSet)

urlpatterns = [
  path('', include(router.urls)),
]

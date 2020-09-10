from django.urls import path
from .views import home, ChartsView
from authentication.views import profile


urlpatterns = [
  path('home/', home, name="home"),
  path('profile/', profile, name="profile"),
  path('charts/', ChartsView.as_view(), name="charts")
]


from django.urls import path
from .views import home
from authentication.views import profile


urlpatterns = [
  path('home/', home, name="home"),
  path('profile/', profile, name="profile"),
]


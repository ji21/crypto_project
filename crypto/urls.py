from django.urls import path
from .views import home, ChartsView, LandingView
from authentication.views import profile
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
  path('home/', home, name="home"),
  path('profile/', profile, name="profile"),
  path('charts/', csrf_exempt(ChartsView.as_view()), name="charts"),
  path('', LandingView.as_view(), name="landing")
]


from .views import UserValidView, LoginView,RegView
from django.urls import path


urlpatterns = [
  path('register/', RegView.as_view(), name="register"),
  path('login/', LoginView.as_view(), name="login"),
  path('validate-username/', UserValidView.as_view(), name="validate-username")
]

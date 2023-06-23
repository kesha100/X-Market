from django.urls import path

from . import views
from .views import RegisterAPIView, LogInAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterAPIView.as_view()),
    path('login/', LogInAPIView.as_view()),
    path('', views.index, name='index'),
]
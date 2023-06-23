from  django.urls import path
from .views import CardListAPIView, CardDetailAPIView
urlpatterns = [
    path('card/', CardListAPIView.as_view()),
    path('card/<int:pk>/', CardDetailAPIView.as_view())
]
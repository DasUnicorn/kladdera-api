from django.urls import path
from .views import MoodList, MoodDetail

urlpatterns = [
    path('mood/', MoodList.as_view(), name='mood-list-create'),
    path('mood/<int:pk>/', MoodDetail.as_view(), name='mood-detail'),
]

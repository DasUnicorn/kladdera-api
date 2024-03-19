from django.urls import path
from profiles import views

urlpatterns = [
    path('accounts/', views.UserListView.as_view()),
]

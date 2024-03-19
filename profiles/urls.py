from django.urls import path
from Profiles import views

urlpatterns = [
    path('accounts/', views.UserListView.as_view()),
]

from django.urls import path
from .views import CustomUserViewSet, CreateUserView

urlpatterns = [
    path('user/', CustomUserViewSet.as_view({
        'get': 'list',     # Endpoint to list all users
        'post': 'create'   # Endpoint to create a new user
    }), name='user-list'),

    path('user/<int:pk>/', CustomUserViewSet.as_view({
        'get': 'retrieve',    # Endpoint to retrieve a specific user
        'put': 'update',      # Endpoint to update a specific user
        'patch': 'partial_update',  # Endpoint to partially update a specific user
        'delete': 'destroy'   # Endpoint to delete a specific user
    }), name='user-detail'),

    # New registration endpoint
    path('register/', CreateUserView.as_view(), name='user-register'),
]

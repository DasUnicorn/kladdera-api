from django.urls import path
from .views import CreateUserView

urlpatterns = [
    # New registration endpoint
    path('register/', CreateUserView.as_view(), name='user-register'),
]

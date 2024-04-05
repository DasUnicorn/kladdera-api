from django.urls import path
from .views import TaskList, TaskDetail

urlpatterns = [
    path('task/', TaskList.as_view(), name='task-list-create'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.tasks, name = 'tasks' ),
    path('tasks/<int:pk>/', views.taskdetails, name = "taskdetails")
]
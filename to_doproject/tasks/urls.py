from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('add_task/', views.add_task, name= 'add_task'),
    path('edit_task/<int:id>/', views.edit_task, name = 'edit_task'),
    path('delete_task/<int:id>/', views.delete_task, name = 'delete_task'),
    path('completed_task/<int:id>/', views.completed_task, name = 'completed_task'),
]

# from datetime import datetime

# current_date_time = datetime.now()
# print(current_date_time)
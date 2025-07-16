from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-task/', views.add_task, name='add_task'),  # Мына жолды қостық
    path('unlock/<int:task_id>/', views.unlock_task, name='unlock_task'),
]


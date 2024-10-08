from django.urls import path
from .views import task_summary

urlpatterns = [
    path('/task-summary',task_summary, name='Task summary' )
]
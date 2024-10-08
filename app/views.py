from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render
from .models import Task

def task_summary(request):
    """
    View to summarize tasks.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML response with task statistics.
    """
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(status='completed').count()
    pending_tasks = Task.objects.filter(status='pending').count()
    canceled_tasks = Task.objects.filter(status='canceled').count()
    today = timezone.now().date()
    overdue_tasks = Task.objects.filter(due_date__lt=today).count()
    tasks_due_today = Task.objects.filter(due_date__date=today).count()
    last_week_tasks = Task.objects.filter(created_at__gte=today - timedelta(days=7)).count()
    low_priority_tasks = Task.objects.filter(priority='low').count()
    medium_priority_tasks = Task.objects.filter(priority='medium').count()
    high_priority_tasks = Task.objects.filter(priority='high').count()

    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'canceled_tasks': canceled_tasks,
        'overdue_tasks': overdue_tasks,
        'tasks_due_today': tasks_due_today,
        'last_week_tasks': last_week_tasks,
        'completion_rate': (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0,
        'low_priority_tasks': low_priority_tasks,
        'medium_priority_tasks': medium_priority_tasks,
        'high_priority_tasks': high_priority_tasks,
    }
    
    return render(request, 'summary.html', context)

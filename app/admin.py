from django.urls import path
from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render
from django.contrib.admin import register, ModelAdmin

from .models import Task


@register(Task)
class TaskAdmin(ModelAdmin):
    """
    Admin interface for managing tasks.

    Attributes:
        list_per_page (int): Number of tasks to display per page.
        list_filter (tuple): Filters available in the task list.
        list_editable (tuple): Fields that can be edited directly in the list view.
        list_display (tuple): Fields to display in the task list.
    """
    
    list_per_page = 10
    list_filter = ('status', 'priority')
    list_editable =('status',)
    list_display = ('title', 'priority', 'due_date', 'created_at', 'status')
    
    save_on_top = True
    date_hierarchy = 'due_date'
    ordering = ['status', 'due_date']
    search_fields = ('title', 'description')
    search_help_text = "Enter a title or description to search for tasks."
    
    actions_on_top = False
    actions_on_bottom = True
    actions_selection_counter = True
    actions = ['mark_completed', 'mark_pending', 'mark_canceled']
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'priority'),
            'classes' : ('wide',)
        }),
        ('Status', {
            'fields': ('status', 'due_date'),
            'classes' : ('wide',)
        }),
    )
    
    def mark_completed(self, request, queryset):
        """Mark selected tasks as completed."""
        queryset.update(status='completed')
    mark_completed.short_description = "Mark selected tasks as completed"
    
    def mark_pending(self, request, queryset):
        """Mark selected tasks as pending."""
        queryset.update(status='pending')
    mark_pending.short_description = "Mark selected tasks as pending"
    
    def mark_canceled(self, request, queryset):
        """Mark selected tasks as canceled."""
        queryset.update(status='canceled')
    mark_canceled.short_description = "Mark selected tasks as canceled"
    
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [path("summary/", self.admin_site.admin_view(self.task_summary))]
        return my_urls + urls

    def task_summary(self, request):
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
    


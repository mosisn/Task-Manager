from .models import Task
from django.urls import path
from django.contrib.admin import register, ModelAdmin


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
    
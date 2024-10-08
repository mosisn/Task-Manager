from django.db import models


STATUS_CHOICES = (
    ('pending','pending'),
    ('completed', 'completed'),
    ('canceled', 'canceled'),
)

PRIORITY_CHOICES = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
]

class Task(models.Model):
    title = models.CharField(max_length=250, verbose_name='Task Title')
    description = models.TextField(verbose_name='Task Description', help_text='Provide a detailed description of the task.')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='Task Status')
    due_date = models.DateTimeField(verbose_name='Due Date', help_text='Specify the due date and time for the task.')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low', verbose_name='Task Priority')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    
    def __str__(self):
        return self.title

class SubTask(models.Model):
    #TODO
    pass
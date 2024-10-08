from django.db import models

STATUS_CHOICES = (
    ('pending','pending'),
    ('canceled', 'canceled'),
    ('completed', 'completed')
)

class Task(models.Model):
    title = models.CharField(max_length=250, verbose_name='Task Title')
    description = models.TextField(verbose_name='Task Description', help_text='Provide a detailed description of the task.')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='Task Status')
    due_date = models.DateTimeField(verbose_name='Due Date', help_text='Specify the due date and time for the task.')
    
    def __str__(self):
        return self.title
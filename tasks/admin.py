from django.contrib import admin
from .models import Task

# Register the Task model
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')  # Fields to display in the admin list view
    search_fields = ('title', 'description')  # Fields to search by
    list_filter = ('completed',)  # Filter by the 'completed' status

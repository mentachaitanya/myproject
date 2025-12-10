from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "due_date", "due_time", "is_completed")
    list_filter = ("user", "due_date", "is_completed")
    search_fields = ("title", "user__username")

admin.site.register(Task, TaskAdmin)

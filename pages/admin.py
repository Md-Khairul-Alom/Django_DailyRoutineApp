from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display=('task', 'is_completed', 'updated_at')
    list_display_links=('task',)
    search_filters=('task',)
admin.site.register(Task, TaskAdmin)
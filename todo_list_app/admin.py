from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'due_date', 'status')
    list_filter = ('status', 'due_date')
    readonly_fields = ('timestamp',)
    fieldsets = (
        ('Task Details', {
            'fields': ('title', 'description', 'due_date', 'tags')
        }),
        ('Status', {
            'fields': ('status',)
        }),
    )

    def has_delete_permission(self, request, obj=None):
        return True if obj is not None and obj.status != 'DONE' else False

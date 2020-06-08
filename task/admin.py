from django.contrib import admin
from task.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ['pk', 'created']
    fieldsets = [
        (None, {'fields': ['pk', 'title', 'text']}),
        ('FK', {'fields': ['author', 'parent',]}),
        ('Status', {'fields': ['is_done', 'is_archive',]}),
        ('Date', {'fields': ['created',], }),
    ]
    list_display = ('id', 'author', 'title', 'text', 'created', 'is_done', 'is_archive',)
    search_fields = ['title', 'author',]
    list_filter = ['created',]

# admin.site.register(Task, TaskAdmin)

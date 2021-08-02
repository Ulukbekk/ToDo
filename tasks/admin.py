from django.contrib import admin

from tasks.models import Task

#admin.site.register(Task)
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'deadline', 'date_created', 'date_modified', 'done']
    list_editable = ['done']
    list_filter = ['deadline', 'date_created', 'date_modified', 'done']
    search_fields = ['title', 'description']


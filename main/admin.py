from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'status')
    list_display_links = ('id', 'name')
    list_filter = ('status', 'date')
    search_fields = ('name', 'opisanie')
    list_editable = ('status',)

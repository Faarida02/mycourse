from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_unlocked')
    list_filter = ('is_unlocked',)
    search_fields = ('title', 'user__username')


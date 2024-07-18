from django.contrib import admin

from .models import Todo, TodoList


@admin.register(TodoList)
class GenericAdmin(admin.ModelAdmin):
    pass


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'completed', 'favorite')

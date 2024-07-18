from django.contrib import admin

from .models import Todo, TodoList


@admin.register(Todo, TodoList)
class TodoAdmin(admin.ModelAdmin):
    pass

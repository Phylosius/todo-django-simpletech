from django.contrib import admin

from .models import Todo, TodoList


@admin.register(TodoList)
class GenericAdmin(admin.ModelAdmin):
    pass


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass

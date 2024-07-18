from django.contrib import admin

from .models import Todo, TodoList


class TodoInline(admin.TabularInline):
    model = Todo


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (TodoInline,)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'completed', 'favorite')

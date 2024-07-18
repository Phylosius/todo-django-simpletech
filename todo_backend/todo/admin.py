from django.contrib import admin

from todo.models import Todo, TodoList

admin.site.register(Todo)
admin.site.register(TodoList)

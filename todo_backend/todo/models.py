from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)

    list = models.ForeignKey('TodoList', null=False, on_delete=models.CASCADE)


class TodoList(models.Model):

    name = models.CharField(max_length=255)

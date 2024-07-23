from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from todo.models import Todo, TodoList
from todo.serializers import TodoSerializer, TodoListSerializer


class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)


class TodoListViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated,)


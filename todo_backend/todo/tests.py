from datetime import datetime, timezone

from django.test import TestCase

from todo.models import Todo, TodoList


class TodoTestCase(TestCase):
    DUMMY_TODO_TITLE = 'Test Todo Element'

    def setUp(self):
        """
        method for test utilities definition
        """
        self.todoList = TodoList()
        self.todoList.name = "Test Todo List"
        self.todoList.save()

        self.todoListTestElement = Todo()
        self.todoListTestElement.title = self.DUMMY_TODO_TITLE
        self.todoListTestElement.due_date = datetime.today()
        self.todoListTestElement.completed = True
        self.todoListTestElement.favorite = False
        self.todoListTestElement.list = self.todoList
        self.todoListTestElement.save()

    def test_create_todo(self):
        nbr_of_todos_bebore_add = Todo.objects.count()

        new_todo = Todo()
        new_todo.title = "Acheter de l'eau"
        new_todo.due_date = datetime.today()
        new_todo.favorite = True
        new_todo.completed = False
        new_todo.list = self.todoList

        new_todo.save()

        nbr_of_todos_after_add = Todo.objects.count()

        self.assertTrue(nbr_of_todos_bebore_add == nbr_of_todos_after_add - 1)

        # voir combien d'element dans le db
        # ajouter un objet dans la db
        # valider que l'objet à été incrementé

    def test_update_todo(self):
        self.assertEqual(self.todoListTestElement.title, self.DUMMY_TODO_TITLE)

        self.todoListTestElement.title = "Changed"
        self.todoListTestElement.save()

        temp_element = Todo.objects.get(pk=self.todoListTestElement.pk)

        self.assertEqual(temp_element.title, "Changed")

    def test_delete_todo(self):

        nbr_of_todos_bebore_del = Todo.objects.count()

        self.todoListTestElement.delete()

        nbr_of_todos_after_del = Todo.objects.count()

        self.assertTrue(nbr_of_todos_bebore_del == nbr_of_todos_after_del + 1)

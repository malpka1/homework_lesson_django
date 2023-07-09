from django.urls import path
from todo.todos.views.api import todos, todo

urlpatterns = [
    path('', todos, name='todos'),
    path('<int:todo_id>/', todo),
]
from django.urls import path

from . import views

urlpatterns = [
path('/', views.todos, name='todos'),
    path('/<int:todo_id>/', views.todo_view, name='views'),
    path('create-todo/', views.create_todo, name='create-todo'),
]
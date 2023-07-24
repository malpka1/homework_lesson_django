from django.shortcuts import render, redirect
from todo.todos.forms import TodoForm, TodoUpdateForm
from todo.todos.models import Todo


def todos(request):
    todos = Todo.objects.all()
    return render(request, 'todos.html', {'todos': todos})


def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todos")
        else:
            return render(request, "create_todo.html", {"form": form})

    return render(request, "create_todo.html", {"form": TodoForm()})


def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = TodoUpdateForm(instance=todo)

    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()

    return render(request, "update_todo.html", {"form": form, "todo": todo})



def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('todos')

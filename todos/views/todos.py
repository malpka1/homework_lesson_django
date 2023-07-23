from django.shortcuts import render, redirect
from todos.forms import TodoForm, TodoUpdateForm
from django.views.decorators.cache import cache_page
from todos.models import Todo


@cache_page(60 * 15)
def todos(request):
    return render(request, 'todos.html', {'todos':Todo.objects.select_related('todo').all()})
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

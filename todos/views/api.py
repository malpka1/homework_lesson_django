from django.http import JsonResponse
from django.forms.models import model_to_dict
from todos.forms import TodoForm, TodoUpdateForm
from todos.models import Todo


def todos(request):
    if request == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo_object = form.save()
            return JsonResponse({'todo': model_to_dict(todo_object)})
        else:
            return JsonResponse({'status': 400, 'errors': form.errors})
    todos_data = [model_to_dict(todo) for todo in Todo.objects.all()]
    return JsonResponse({'todos': todos_data})


def todo(request, todo_id):
    try:
        todo_object = Todo.object.get(id=todo_id)
    except Exception:
        return JsonResponse({'status': 404, 'errors': 'Todo not found'})
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo_object)
        if form.is_valid():
            todo_object = form.save()
            return JsonResponse({todo: model_to_dict(todo_object)})
        else:
            return JsonResponse({'status': 400, 'error': form.errors})

    elif request.method == 'DELETE':
        todo_object.delete()
        return JsonResponse({'status': 204, 'message': 'Todo successfully deleted'})

    return JsonResponse({'todo': model_to_dict(todo_object)})





import requests
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

TODOS = requests.get("https://jsonplaceholder.typicode.com/todos").json()


def todos(request):
    if request.method == 'GET':
        return render(request, 'todos.html', {'todos': TODOS})
    elif request.method == 'POST':
        todo = dict(request.POST)
        for key in todo:
            todo[key] = todo[key][0]
        todo['title'] = todo['title'][0]
        todo['complete'] = bool(todo['complete'][0])
        todo['id'] = int(todo['id']) if 'id' in todo else 200
        todo.append(todo)
        return render(request, 'todos.html', {'todo': TODOS})


def get_todo(request, todo_id: int):
    global TODOS
    todo = next((todo for todo in TODOS if todo['id'] == todo_id), None)
    if todo:
        if request.method == 'GET':
            return JsonResponse({'todo': todo})
        elif request.method == 'DELETE':
            TODOS = [todo for todo in TODOS if todo['id'] != todo_id]
            return HttpResponse(status=200)
    return HttpResponse(status=404)


def todo_view(request, todo_id: int):
    global TODOS
    todo = next((todo for todo in TODOS if todo['id'] == todo_id), None)
    if todo:
        if request.method == 'GET':
            return JsonResponse({'todo': todo})
        elif request.method == 'DELETE':
            TODOS = [todo for todo in TODOS if todo['id'] != todo_id]
            return HttpResponse(status=200)
    return HttpResponse(status=404)


def create_todo(request):
    return render(request, 'create_todo.html')




from dotenv import load_dotenv
import os
import requests
import json
from typing import List

load_dotenv()
print(f"ENV {os.environ.get('ENV')}")


URL = os.environ.get('URL')

response = requests.get(URL)
print(response.json())

for todo in response.json():
    print(todo["title"])

class Todo:
    def __init__(self, userId, id, title, completed:bool):
        self.userId = userId
        self.id = id
        self.title = title

    def __repr__(self):
        return f"Todo: {self.userId}, id:{self.id}, title:{self.title}, completed:{bool}"

class Todos:
    def __init__(self, todos: List[Todo]):
        self.todos = todos

    def __iter__(self):
        return iter(self.todos)

    def __getitem__(self, id):
        for todo in self.todos:
            if todo.id == id:
                return todo
        raise KeyError(f"Todo with id {id} not found")
    def to_json(self):
            return json.dumps([todo.__dict__ for todo in self.todos])

    @classmethod
    def from_json(cls, json_str):
        todos_json = json.loads(json_str)
        todos = [Todo(**todo) for todo in todos_json]
        return cls(todos)

def get_todos() -> Todos:
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos_json = response.json()
    todos = [Todo(**todo) for todo in todos_json]
    return Todos(todos)

todos = get_todos()
from django_filters.rest_framework import DjangoFilterBackend
from todo.todos.models import Todo
from rest_framework import viewsets, filters, generics
from rest_framework import permissions
from todo.todos.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend, filters.SearchFilter]
    ordering_fields = ['id', 'title', 'description', 'completed']
    filterset_fields = ['id', 'title', 'completed']
    search_fields = ['title']


class TodoList(generics.ListAPIView):
        queryset = Todo.objects.all()
        serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveAPIView):
        queryset = Todo.objects.all()
        serializer_class = TodoSerializer


class TodoCreate(generics.CreateAPIView):
        queryset = Todo.objects.all()
        serializer_class = TodoSerializer


class TodoUpdate(generics.UpdateAPIView):
        queryset = Todo.objects.all()
        serializer_class = TodoSerializer


class TodoDelete(generics.DestroyAPIView):
        queryset = Todo.objects.all()
        serializer_class = TodoSerializer
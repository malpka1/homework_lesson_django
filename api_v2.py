from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, TodoList, TodoDetail, TodoCreate, TodoUpdate, TodoDelete

router = DefaultRouter()
router.register('todo', TodoViewSet)
router.register(r'todos', TodoList)
router.register(r'todos/(?P<pk>\d+)', TodoDetail)
router.register(r'todos/create', TodoCreate)
router.register(r'todos/(?P<pk>\d+)/update', TodoUpdate)
router.register(r'todos/(?P<pk>\d+)/delete', TodoDelete)

urlpatterns = [
    path('', include(router.urls)),
]

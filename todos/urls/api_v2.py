from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
#from todos.serializers import TodoDetail, TodoCreate, TodoUpdate, TodoDelete
from todos.views.api_v2 import TodoViewSet

router = DefaultRouter()
router.register('todo', TodoViewSet)
#router.register(r'todos/(?P<pk>\d+)', TodoDetail)
#router.register(r'todos/create', TodoCreate)
#router.register(r'todos/(?P<pk>\d+)/update', TodoUpdate)
#router.register(r'todos/(?P<pk>\d+)/delete', TodoDelete)


if settings.DEBUG:
    import debug_toolbar


urlpatterns = [
    path('', include(router.urls)),
]

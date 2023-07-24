
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todos', include('api.urls')),
    path('todo', include('todos.urls')),
    path('create-todo', include('todos.urls')),
]

import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todo/', include('todos.urls.api')),
    path('todo/', include('todos.urls.todos')),
    path('api/v2/', include('todos.urls.api_v2')),
    path('auth/', include('rest_authtoken.urls')),
   	path('api/token/', TokenObtainPairView(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView(), name='token_refresh'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
                  ] + urlpatterns
 

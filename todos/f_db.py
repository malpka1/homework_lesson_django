from django.contrib.auth.models import User

from .models import Todo


def create_initial_db():
    user_1 = User.objects.create_user(
        username='Bruno',
        email='bruno@gmail.com',
        password='123',
        is_active=True
    )
    user_2 = User.objects.create_user(
        username='Sara',
        email='s@gmail.com',
        password='123',
        is_active=True
    )
    user_3 = User.objects.create_user(
        username='Gawr',
        email='gawrik@gmail.com',
        password='123',
        is_active=True
    )

    todo_1 = Todo(
        title='to go for a walk',
        description='after breakfast',
        user=user_1
    )
    todo_2 = Todo(
        title='training',
        description='yoga',
        user=user_2
    )
    todo_3 = Todo(
        title='courses',
        description='informatics',
        user=user_3
    )
    todo_1.save()
    todo_2.save()
    todo_3.save()
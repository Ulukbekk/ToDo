from django.urls import path
from .views import (
    main, all_tasks,
    task_detail, task_delete,
    search, complete_task,
    completed_tasks, )

urlpatterns = [
    path('task/complete/<int:pk>', complete_task, name='complete_task'),
    path('task/completed_tasks/', completed_tasks, name='completed_tasks'),
    path('search', search, name='search'),
    path('create-task', main, name='main'),
    path('task/delete<int:pk>', task_delete, name='task_delete'),
    path('task/<int:pk>', task_detail, name='task_detail'),
    path('', all_tasks, name='all_tasks'),

]
from django.urls import path
from .views import taskDelete, taskList, taskUpdate
from .views import taskDetail
from .views import taskCreate

urlpatterns = [
    path('', taskList.as_view(), name='tasks'), 

    ##CRUD Functionality
    path('task/<int:pk>/', taskDetail.as_view(), name='task'),
    path('create-task/', taskCreate.as_view(), name='task-create'),
    path('update-task/<int:pk>/', taskUpdate.as_view(), name='task-update'),
    path('delete-task/<int:pk>/', taskDelete.as_view(), name='task-delete'),

    
]
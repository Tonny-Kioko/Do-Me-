from django.urls import path
from .views import taskList
from .views import taskDetail
from .views import taskCreate

urlpatterns = [
    path('', taskList.as_view(), name='tasks'), 
    path('task/<int:pk>/', taskDetail.as_view(), name='task'),
    path('create-task/', taskCreate.as_view(), name='task-create'),
]
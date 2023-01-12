from django.urls import path
from .views import taskList
from .views import taskDetail

urlpatterns = [
    path('', taskList.as_view(), name='tasks'), 
    path('task/<int:pk>/', taskDetail.as_view(), name='tasks_detail'),
]